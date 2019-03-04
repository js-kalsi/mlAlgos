"""
/*
*
*
*       Iris Dataset Clustering Generalized Inverted Dirichlet Finite Mixture Model.
*
*       ```python core.py```
*
*/


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
from numpy.linalg import inv as INVERSE
from numpy import matmul as MATMUL
from numpy import all as ALL
from numpy import real as REAL

class Helper:

    @staticmethod
    def geo_transformation(pixels, DIM, pixelSize):
        return ASARRAY(
            [pixels[:, d:d + 1] / (1 + SUM(pixels[:, 0:d], axis=1).reshape(pixelSize, 1)) for d in
             range(DIM)]).T.reshape(
            pixelSize, DIM)

    @staticmethod
    def mixer_estimator(clusterSet, pixelSize):
        return [len(clusterSet[cluster]) / pixelSize for cluster in clusterSet]

    @staticmethod
    def split_Pixels_Based_On_Label(labels, imgPixels):
        unique_Clusters = np.unique(labels)
        clustersObj = {}
        for index, label in enumerate(labels):
            if not (label in clustersObj):
                clustersObj[label] = []
            clustersObj[label].append(imgPixels[index])
        return clustersObj, unique_Clusters, len(clustersObj[0][0])

    @staticmethod
    def method_of_moment(K, clusterSet, DIM):
        alpha = ZEROS((K, DIM))
        for label in clusterSet:
            sum = 0
            for d in range(DIM):
                clusterSet[label] = ASARRAY(clusterSet[label])
                mean = MEAN(clusterSet[label][:, [d]])
                den = VAR(clusterSet[label][:, [d]]) + sys.float_info.epsilon
                alpha_D_pls_One = ((POW(mean, 2) + mean) / den) + 2
                sum += alpha_D_pls_One
                alpha[label][d] = mean * (alpha_D_pls_One - 1)
        return NORMALIZE(alpha)

    @staticmethod
    def posterior_estimator(pdf, mix):
        return ASARRAY([(mix * pV) / SUM(mix * pV) for pV in pdf]).reshape(len(pdf), mix.size)

    @staticmethod
    def mix_updater(posterior, size, cluster):
        return (SUM(posterior, axis=0) / size).reshape(1, cluster)

    def g_estimation(self, data_set, alpha, beta, posterior, dim, K):
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

        return ASARRAY(q_alpha).reshape(K, dim), ASARRAY(q_beta).reshape(K, dim), ASARRAY(q_alpha_square).reshape(K, dim), ASARRAY(
            q_beta_square).reshape(K, dim), ASARRAY(q_alpha_beta_square).reshape(K, dim)

    @staticmethod
    def fisher_info_inv(alpha, beta, q_alpha, q_beta, q_a_sqr, q_b_sqr, q_a_b_sqr, k, dim):
        updated_alpha = []
        updated_beta = []

        for aV, bV, qAV, qBV, qASqrV, qBSqrV, qABSqrV in zip(alpha, beta, q_alpha, q_beta, q_a_sqr, q_b_sqr, q_a_b_sqr):
            for aVal, bVal, qAVal, qBVal, qASqVal, qBSqVal, qABSqVal in zip(aV, bV, qAV, qBV, qASqrV, qBSqrV, qABSqrV):
                h_inverse = INVERSE(ASARRAY([qASqVal, qABSqVal, qABSqVal, qBSqVal]).reshape(2, 2))
                theta = ASARRAY([aVal, bVal]).reshape(2, 1) - 0.5* MATMUL(h_inverse, ASARRAY([qAVal, qBVal]).reshape(2, 1))
                updated_alpha.append(theta[0])
                updated_beta.append(theta[1])
        return ASARRAY(updated_alpha).reshape(k, dim), ASARRAY(updated_beta).reshape(k, dim)

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def predict_labels(posterior):
        return posterior.argmax(axis=1)
