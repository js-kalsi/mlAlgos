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

from numpy import sum as SUM
from numpy import subtract as SUBS
from numpy import zeros as ZEROS
from scipy.special import gammaln as GAMMALN
from numpy import exp as EXP
from numpy import log as LOG
import warnings
warnings.filterwarnings("error")

"""
/**
 * This function add the array's element and return them in the form of a String.
 * @param  {Integer} a.
 * @return {String} which contains the Sum of Array.
 */
"""


class invertedDirichlet:

    def __init__(self, no_of_clusters, alpha, img_pixels):
        self.no_of_clusters = no_of_clusters
        self.alpha = alpha
        self.img_pixels = img_pixels

    """
    /**
     * This function add the array's element and return them in the form of a String.
     * @param  {Integer} a.
     * @return {String} which contains the Sum of Array.
     */
    """
    def pdf_fetcher(self):
        probability = ZEROS((len(self.img_pixels), self.no_of_clusters))
        for a_index, a_v in enumerate(self.alpha):
            for p_index, pixels in enumerate(self.img_pixels):
                probability[p_index][a_index] = self.pdf(pixels, a_v)
        return probability


    """
    /**
     * This function add the array's element and return them in the form of a String.
     * @param  {Integer} a.
     * @return {String} which contains the Sum of Array.
     */
    """
    @staticmethod
    def pdf(p_v, a_v):
        try:
            return EXP(GAMMALN(SUM(a_v)) - SUM(GAMMALN(a_v)) +
                       SUM(SUBS(a_v[:-1], 1) * LOG(p_v)) -
                       SUM(a_v) * LOG(1 + SUM(p_v)))
        except RuntimeWarning:
            print("pVector :>", p_v)
            print("aVector :>", a_v)
            print("GAMMALN(SUM(a_v)) :>", GAMMALN(SUM(a_v)))
            print("GAMMALN(a_v) :>", GAMMALN(a_v))
            print("LOG(p_v) :>", LOG(p_v))
            print("SUM(a_v) :>", SUM(a_v))
            print("LOG(1 + SUM(p_v) :>", LOG(1 + SUM(p_v)))
            exit(0)
