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
    # foo = ASARRAY([[10, 20, 30], [40, 50, 60]])
    # return foo, len(foo)
    return datasets.load_iris().data, len(datasets.load_iris().data)





