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

import numpy as np
from scipy.special import loggamma
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize

from helpers import convergence_test, fisher_info_inv, g_estimation, geo_transformation, method_of_moment, \
    split_data_by_label
from parameters import EPSILON, NO_OF_CLUSTERS


def initial_algorithm():
    dataset = datasets.load_iris().data
    dataset = normalize(dataset) + EPSILON
    labels = KMeans(n_clusters=NO_OF_CLUSTERS, random_state=0).fit(dataset).predict(dataset)
    clusters = split_data_by_label(dataset, labels)
    dataset = geo_transformation(dataset)
    mix = np.asarray([len(clusters[c]) / len(dataset) for c in clusters]).reshape(1, NO_OF_CLUSTERS)
    alpha = method_of_moment(clusters)
    return dataset, alpha, mix


def estimation_step(dataset, mix, alpha, beta):
    pdf = gen_inv_dirichlet(dataset, alpha, beta)
    posterior = np.asarray([(mix * p) / np.sum(mix * p) for p in pdf]).reshape(len(pdf), mix.size)
    return posterior


def maximization_step(dataset, alpha, beta, posterior):
    mix = (np.sum(posterior, axis=0) / len(dataset)).reshape(1, NO_OF_CLUSTERS)
    q_alpha, q_beta, q_alpha_sqr, q_beta_sqr, q_alpha_beta_sqr = g_estimation(dataset, alpha, beta, posterior)
    alpha, bdta = fisher_info_inv(alpha, beta, q_alpha, q_beta, q_alpha_sqr, q_beta_sqr, q_alpha_beta_sqr)
    return mix, alpha, beta


def gen_inv_dirichlet(dataset, alpha, beta):
    result = []
    for d in dataset:
        result.append([np.prod(np.exp(loggamma(a + b) - loggamma(a) - loggamma(b) + (a - 1)
                                      * np.log(d) - (a + b) * np.log(1 + d)))
                       for a, b in zip(alpha, beta)])
    return np.asarray(result)


def main():
    obj = {'alpha': []}
    initial_algorithm()
    data, alpha_parameter, mixing_parameter = initial_algorithm()
    beta_parameter = alpha_parameter
    counter = 0
    while True:
        posterior = estimation_step(data, mixing_parameter, alpha_parameter, beta_parameter)
        mixing_parameter, alpha_parameter, beta_parameter = maximization_step(data, alpha_parameter, beta_parameter,
                                                                              posterior)
        obj['alpha'].append(alpha_parameter)
        converge = convergence_test(obj)
        predict_labels = posterior.argmax(axis=1)
        counter = counter + 1
        if converge:
            print("Algorithm converged after " + str(counter) + " iterations.")
            print("Labels : ", predict_labels)
            break


if __name__ == '__main__':
    main()
