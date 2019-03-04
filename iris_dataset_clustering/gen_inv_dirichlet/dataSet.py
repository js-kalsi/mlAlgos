"""
/*
*
*
*       Iris Dataset Clustering Generalized Inverted Dirichlet Finite Mixture Model.
*
*       ```python core.py```
*
*/



from sklearn import datasets
from numpy import asarray as ASARRAY


def iris():
    return datasets.load_iris().data, len(datasets.load_iris().data)
