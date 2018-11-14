"""
/*
*       Coded by : Jaspreet Singh Kalsi.
*
*       "Thesis  Chapter-2 Part A
*       (Image Fragmentation using Inverted Dirichlet Distribution using Markov Random Field as a Prior).
*
*       ```python core.py <Image-Name>```
*
*/

"""


import sys
import numpy as np
import pickle
from math import pow as POW
from scipy.special import polygamma as POLYGAMMA
from numpy import sum as SUM
from numpy import log as LOG
from numpy import zeros as ZEROS
from numpy import asarray as ASARRAY
from numpy import mean as MEAN, var as VAR
from numpy import full as FULL
from numpy import concatenate as CONCAT
from sklearn.preprocessing import normalize as NORMALIZE
from numpy import diag as DIAGONAL
from numpy import matmul as MATMUL
from numpy import all as ALL


def display( paramOne, paramTwo, paramThree):
    print(('{0}\'s {1} : {2}').format(paramOne, paramTwo, paramThree))


def logger( data):
    file = open('./dataset/logs.txt', 'wb')
    pickle.dump(data, file)
    file.close()


def mixer_estimator( clusterSet, pixelSize):
    return [len(clusterSet[cluster]) / pixelSize for cluster in clusterSet]


def split_Pixels_Based_On_Label( labels, imgPixels):
    unique_Clusters = np.unique(labels)
    clustersObj = {}
    for index, label in enumerate(labels):
        if not (label in clustersObj):
            clustersObj[label] = []
        clustersObj[label].append(imgPixels[index])
    return clustersObj, unique_Clusters, len(clustersObj[0][0])


def intialMixerEstimator( mix, pixelSize, K):
    return ASARRAY([FULL((pixelSize, 1), pi) for pi in mix]).T.reshape(pixelSize, K)


def method_of_moment(K, cluster_set, dim):
    alpha = ZEROS((K, dim + 1))
    for label in cluster_set:
        alpha_sum = 0
        for d in range(dim):
            cluster_set[label] = ASARRAY(cluster_set[label])
            mean = MEAN(cluster_set[label][:, [d]])
            den = VAR(cluster_set[label][:, [d]]) + sys.float_info.epsilon
            alpha_d_pls_One = ((POW(mean, 2) + mean) / den) + 2
            alpha_sum += alpha_d_pls_One
            alpha[label][d] = mean * (alpha_d_pls_One - 1)
        alpha[label][dim] = MEAN(alpha_sum)
    return NORMALIZE(alpha)


def posterior_estimator( pdf, mix):
    return ASARRAY([(mix * pV) / SUM(mix * pV) for pV in pdf]).reshape(len(pdf), mix.size)


def mix_updater(posterior, size, cluster):
    return (SUM(posterior, axis=0) / size).reshape(1, cluster)


def g_estimation(data_set, size, alpha, posterior, dim, K):
    G = []
    data_set = CONCAT((data_set, FULL((size, 1), 1)), axis=1)
    pixel_log = ASARRAY([LOG(data / SUM(data)) for data in data_set])
    for index, aV in enumerate(alpha):
        G.append(g_matrix_generator(aV, posterior[:, [index]], pixel_log, dim))
    return ASARRAY(G)


def g_matrix_generator(alpha, posterior, log_pixels, dim):
    return SUM(posterior * (POLYGAMMA(0, SUM(alpha)) -
                            POLYGAMMA(0, alpha).reshape(1, dim + 1) +
                            log_pixels.reshape(len(log_pixels), dim + 1)), axis=0).reshape(dim + 1, 1)


def hessian(dim, posterior, alpha):
    h_diagonal = []
    h_constant = []
    h_a = []

    for index, a_vector in enumerate(alpha):
        p_sum = SUM(posterior[:, index])
        a_tri_gamma = POLYGAMMA(1, a_vector)
        a_tri_gamma_sum = POLYGAMMA(1, SUM(a_vector))
        h_diagonal.append(DIAGONAL(1 / (-1 * p_sum * a_tri_gamma)))
        h_constant.append(((a_tri_gamma_sum * SUM(1 / a_tri_gamma)) - 1) * a_tri_gamma_sum * p_sum)
        h_a.append(((-1 / p_sum) * (1 / a_tri_gamma)).reshape(1, dim + 1))

    return ASARRAY(h_diagonal), h_constant, ASARRAY(h_a)


def hessian_inverse(K, diagonal, constant, a):
    return ASARRAY([diagonal[j] + (constant[j] * MATMUL(a[j].T, a[j])) for j in range(K)])


def alpha_updater(alpha_set, hessian_inverse, G, K, dim):
    return ASARRAY([alpha_set[j].reshape(dim + 1, 1) -
                    0.9 * MATMUL(hessian_inverse[j], G[j]) for j in range(K)]).reshape(K, dim + 1)


def cluster_drop_test(mix, alpha, cluster_drop_val, K, dim):
    mix_arr = []
    alpha_arr = []
    mix = mix[0]
    for j in range(K):
        if mix[j] > cluster_drop_val:
            mix_arr.append(mix[j])
            alpha_arr.append(alpha[j])
        else:
            print("Cluster having  alpha :", alpha[j], " & Mix :", j, " & Value :", mix[j], " is removed!")

    mix_arr = ASARRAY(mix_arr)
    alpha_arr = ASARRAY(alpha_arr)
    return mix_arr.reshape(1, mix_arr.size), alpha_arr.reshape(len(alpha_arr), dim + 1), mix_arr.size


def predict_labels(posterior):
    return posterior.argmax(axis=1)

def convergence_test(alpha, convergence_val):
    alpha_size = len(alpha)
    if alpha_size >= 2:
        if alpha[alpha_size - 1].shape == alpha[alpha_size - 2].shape:
            return ALL(convergence_val >= (alpha[alpha_size - 1] - alpha[alpha_size - 2]))
        else:
            print("Two or more value of Alpha Exist but their shape differs !")
            return False
    else:
        return False
