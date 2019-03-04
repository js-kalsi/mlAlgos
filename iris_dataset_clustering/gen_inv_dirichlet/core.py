"""
    /*
    *       Coded by : Jaspreet Singh Kalsi.
    *
    *       Clustering of Iris dataset using generalized Inverted Dirichlet Mixture Model.
    *
    *       ```python core.py```
    *
    *
    *   EM Algorithm Generalized Inverted Dirichlet Mixture Model.
    *       1) Pick Iris dataset.
    *       2) Normalize it.
    *       3) Assume Number of Cluster(K) =  10 & apply KMeans clustering algorithm
    *          to obtain K clusters for Initialization purposes.
    *       4) Use `Method of Moments` for obtaining the initial values for Mixing Parameters.
    *       5) Expectation Step:
    *                           => Compute the Posterior Probability.
    *       6) Maximization Step:
    *                           => Update the Mixing Parameter.
    *                           => Update the Alpha and Beta Parameters using `Newton Raphson` Method.
    *       7) If Mixing Parameter of any Cluster < Cluster-Skipping Threshold:
    *                           => Skip that particular Cluster.
    *       8) Compute the Log Likelihood and check for Convergence by comparing the difference
    *          between last two likelihood values with the Convergence Threshold.
    *       9) If algorithm(converge) :terminate
    *       10) Go-to Step 5(Expectation Step).
    */

"""


import sys
from dataSet import iris as IRIS # Importing DataSet
from KMeans import KMeans as KM # contains KNN related functionality.
from lib.helpers import Helper as HELPER  # class contains the logic like performanceMeasure, Precision etc.
from lib.constants import CONST  # contains the constant values.
from gen_inv_dirichlet import GeneralizedInvertedDirichlet as generalized_inverted_dirichlet
from sklearn.preprocessing import normalize as NORMALIZE
from numpy import sum as SUM
from numpy import asarray as ASARRAY
import warnings
warnings.filterwarnings("error")


def initial_algorithm(no_of_clusters):
    ini_data_set, size = IRIS()
    ini_data_set = NORMALIZE(ini_data_set) + sys.float_info.epsilon
    labels_kmeans = ASARRAY(KM(ini_data_set, no_of_clusters).predict()).reshape(1, size)
    clusters, unique_clusters, dimension = HELPER().split_Pixels_Based_On_Label(labels_kmeans[0], ini_data_set)
    ini_data_set = HELPER().geo_transformation(ini_data_set, dimension, size)
    initial_py = ASARRAY(HELPER().mixer_estimator(clusters, size)).reshape(1, no_of_clusters)
    initial_alpha = HELPER().method_of_moment(no_of_clusters, clusters, dimension)
    initial_beta = initial_alpha  # Initially take same values for alpha & beta parameter.
    return initial_alpha, initial_beta, ini_data_set, dimension, size, initial_py


def estimation_step(no_of_clusters, mix, alpha, beta, data_set):
    pdf = generalized_inverted_dirichlet(no_of_clusters, alpha, beta, data_set).pdf_fetcher()
    posterior_e_step = HELPER().posterior_estimator(pdf, mix)
    return posterior_e_step


def maximization_step(K, alpha, beta, data_set, dim, posterior, size):
    mix_m_step = HELPER().mix_updater(posterior, size, K)  # Checked: Working Fine!
    q_alpha, q_beta, q_alpha_sqr, q_beta_sqr, q_alpha_beta_sqr = HELPER().g_estimation(data_set, alpha, beta, posterior, dim, K)  # Checked: Working Fine!
    alpha_m_step, beta_m_step = HELPER().fisher_info_inv(alpha, beta, q_alpha, q_beta, q_alpha_sqr, q_beta_sqr, q_alpha_beta_sqr, K, dim)  # Checked: Working Fine!
    return mix_m_step, alpha_m_step, beta_m_step


if __name__ == '__main__':
    K = CONST["K"]
    obj = {'alpha': []}
    alpha, beta, data_set, dim, data_size, mix = initial_algorithm(K)
    counter = 0
    while True:
        posterior = estimation_step(K, mix, alpha, beta, data_set)
        mix, alpha, beta = maximization_step(K, alpha, beta, data_set, dim, posterior, data_size)
        obj['alpha'].append(alpha)
        converge = HELPER().convergence_test(obj['alpha'], CONST['alg_converge'])
        predict_labels = HELPER().predict_labels(posterior)
        counter = counter + 1
        if converge:
            print("Algorithm converged after " + str(counter) + " iterations.")
            print("Labels : ", predict_labels)
            exit(0)
