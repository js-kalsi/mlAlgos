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


from sklearn import datasets
from numpy import asarray as ASARRAY


def iris():
    return datasets.load_iris().data, len(datasets.load_iris().data)
