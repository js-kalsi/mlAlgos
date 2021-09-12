from math import pow as POW

import numpy as np
from numpy import all as ALL
from numpy import asarray as ASARRAY
from numpy import log as LOG
from numpy import matmul as MATMUL
from numpy import sum as SUM
from numpy.linalg import inv as INVERSE
from scipy.special import polygamma as POLYGAMMA
from sklearn.preprocessing import normalize

from parameters import CONVERGENCE, DIM, EPSILON, NO_OF_CLUSTERS


def split_data_by_label(dataset, labels):
    clusters = {}
    for index, label in enumerate(labels):
        if label not in clusters:
            clusters[label] = []
        clusters[label].append(dataset[index])
    return clusters


def geo_transformation(data):
    """
    Perform geo-transformation on dataset.
    @param data:
    @return: transformation: Transformed form of dataset.
    """
    data = data[:5]
    print("data :>", data)
    for d in range(DIM):
        print("data[:, d:d + 1] :>", data[:, d:d + 1])
        print("data[:, :d] :>", data[:, :d])

    transformation = np.asarray([data[:, d:d + 1] / (1 + SUM(data[:, :d], axis=1)) for d in range(DIM)])
    print("transformation :>", transformation)
    # return transformation.reshape(len(data), DIM)


def method_of_moment(clusters):
    """
    Using method of moment to get initial value fot alpha.
    @param clusters:
    @return:
    """
    alpha = np.zeros((NO_OF_CLUSTERS, DIM))
    for label in clusters:
        for d in range(DIM):
            mean = np.mean(clusters[label][:, [d]])
            var = np.var(clusters[label][:, [d]]) + EPSILON
            alpha_d_plus_one = ((POW(mean, 2) + mean) / var) + 2
            alpha[label][d] = mean * (alpha_d_plus_one - 1)
    return normalize(alpha)


def g_estimation(data_set, alpha, beta, posterior, dim, K):
    q_alpha = []
    q_beta = []
    q_alpha_square = []
    q_beta_square = []
    q_alpha_beta_square = []

    for index, (a_vector, b_vector) in enumerate(zip(alpha, beta)):
        a_d_gamma = POLYGAMMA(0, a_vector).reshape(1, dim)
        b_d_gamma = POLYGAMMA(0, b_vector).reshape(1, dim)
        ab_d_gamma = POLYGAMMA(0, a_vector + b_vector).reshape(1, dim)
        a_t_gamma = POLYGAMMA(1, a_vector).reshape(1, dim)
        b_t_gamma = POLYGAMMA(1, b_vector).reshape(1, dim)
        ab_t_gamma = POLYGAMMA(1, a_vector + b_vector).reshape(1, dim)
        a_data = ASARRAY([LOG(data / (1 + data)) for data in data_set]).reshape(len(data_set), dim)
        b_data = ASARRAY([LOG(1 / (1 + data)) for data in data_set]).reshape(len(data_set), dim)
        q_alpha.append(SUM(posterior[:, [index]] * (ab_d_gamma - a_d_gamma + a_data), axis=0).reshape(1, dim))
        q_beta.append(SUM(posterior[:, [index]] * (ab_d_gamma - b_d_gamma + b_data), axis=0).reshape(1, dim))
        q_alpha_square.append(SUM(posterior[:, [index]] * (ab_t_gamma - a_t_gamma), axis=0).reshape(1, dim))
        q_beta_square.append(SUM(posterior[:, [index]] * (ab_t_gamma - b_t_gamma), axis=0).reshape(1, dim))
        q_alpha_beta_square.append(SUM(posterior[:, [index]] * ab_t_gamma, axis=0).reshape(1, dim))

    return ASARRAY(q_alpha).reshape(K, dim), ASARRAY(q_beta).reshape(K, dim), ASARRAY(q_alpha_square).reshape(K,
                                                                                                              dim), ASARRAY(
        q_beta_square).reshape(K, dim), ASARRAY(q_alpha_beta_square).reshape(K, dim)


def fisher_info_inv(alpha, beta, q_alpha, q_beta, q_a_sqr, q_b_sqr, q_a_b_sqr, k, dim):
    updated_alpha = []
    updated_beta = []

    for aV, bV, qAV, qBV, qASqrV, qBSqrV, qABSqrV in zip(alpha, beta, q_alpha, q_beta, q_a_sqr, q_b_sqr, q_a_b_sqr):
        for aVal, bVal, qAVal, qBVal, qASqVal, qBSqVal, qABSqVal in zip(aV, bV, qAV, qBV, qASqrV, qBSqrV, qABSqrV):
            h_inverse = INVERSE(ASARRAY([qASqVal, qABSqVal, qABSqVal, qBSqVal]).reshape(2, 2))
            theta = ASARRAY([aVal, bVal]).reshape(2, 1) - 0.5 * MATMUL(h_inverse, ASARRAY([qAVal, qBVal]).reshape(2, 1))
            updated_alpha.append(theta[0])
            updated_beta.append(theta[1])
    return ASARRAY(updated_alpha).reshape(k, dim), ASARRAY(updated_beta).reshape(k, dim)


def clusterDropTest(mix, alpha, dropingCriteria, K, DIM, pixelSize):
    mixInfo = []
    alphaInfo = []

    for j in range(K):
        if SUM(mix[:, j: j + 1]) > dropingCriteria:
            mixInfo.append(mix[:, j: j + 1])
            alphaInfo.append(alpha[j])
        else:
            print("Cluster having  alpha :", alpha[j], " & Mix :", j, " is removed!")
    return (ASARRAY(mixInfo).T).reshape(pixelSize, len(alphaInfo)), ASARRAY(alphaInfo).reshape(len(alphaInfo),
                                                                                               DIM), len(mixInfo)


def convergence_test(alpha):
    alpha_size = len(alpha)
    if alpha_size >= 2:
        if alpha[alpha_size - 1].shape == alpha[alpha_size - 2].shape:
            return ALL(CONVERGENCE >= (alpha[alpha_size - 1] - alpha[alpha_size - 2]))
        else:
            print("Two or more value of Alpha Exist but their shape differs !")
            return False
    else:
        return False
