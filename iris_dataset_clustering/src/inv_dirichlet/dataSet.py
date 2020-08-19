"""
/*
*
*
*       Iris Dataset Clustering Inverted Dirichlet Finite Mixture Model.
*
*       ```python core.py```
*
*/
"""


from sklearn import datasets
from numpy import asarray as ASARRAY


def iris():
    # foo = ASARRAY([[10, 20, 30], [40, 50, 60]])
    # return foo, len(foo)
    return datasets.load_iris().data, len(datasets.load_iris().data)





