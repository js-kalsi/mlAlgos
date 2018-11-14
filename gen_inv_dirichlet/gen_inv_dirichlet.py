"""
/*
*       Coded by : Jaspreet Singh Kalsi.
*
*       "Thesis  Chapter-2 Part A
*       (Image Fragmentation using Generalized Inverted Dirichlet Distribution using Markov Random Field as a Prior).
*
*       ```python core.py <Image-Name>```
*
*/

"""

import sys
from scipy.special import loggamma as GAMMALN
from numpy import prod as PROD
from numpy import log as LOG
from numpy import exp as EXP
from numpy import asarray as ASARRAY

class GeneralizedInvertedDirichlet:

    def __init__(self, k, alpha, beta, img_pixels):
        self.k = k
        self.alpha = alpha
        self.beta = beta
        self.img_pixels = img_pixels

    def pdf_fetcher(self):
        result = []
        for p_v in self.img_pixels:
            result.append([self.pdf(p_v, a_v, b_v) for a_v, b_v in zip(self.alpha, self.beta)])
        return ASARRAY(result)

    @staticmethod
    def pdf(p_v, a_v, b_v):
        return PROD(EXP(GAMMALN(a_v + b_v) - GAMMALN(a_v) - GAMMALN(b_v) +
                        (a_v - 1) * LOG(p_v) - (a_v + b_v) * LOG(1 + p_v)))
