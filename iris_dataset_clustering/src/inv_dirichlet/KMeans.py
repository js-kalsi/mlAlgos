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

from sklearn.cluster import KMeans as KM
import numpy as np

class KMeans:

    def __init__(self, imgPixels, K):
        self.imgPixels = imgPixels
        self.KM = KM(n_clusters=K, random_state=0).fit(self.imgPixels)

    """
        /**
         * `predict` function of KNN Class.
         * @return  {Integer Vector} Y_Predict(Predicted Class Label for Test Data).
        */
     """
    def predict(self):
        return self.KM.predict(self.imgPixels)
