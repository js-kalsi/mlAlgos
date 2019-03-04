"""
/*
*
*
*       Iris Dataset Clustering Generalized Inverted Dirichlet Finite Mixture Model.
*
*       ```python core.py```
*
*/


from sklearn.cluster import KMeans as KM
import numpy as np

class KMeans:

    """
        /**
         * Constructor of KNN Class.
         * @param  {Integer Vector} X_train(Training Data).
         * @param  {Integer Vector} Y_train(Training Class Label).
         * @param  {Integer Vector} X_test(Test Data).
         * @param  {Integer Vector} Y_test(Test Class Label).
        */
     """

    def __init__(self, imgPixels, K):
        self.imgPixels = imgPixels
        self.KM = KM(n_clusters= K, random_state= 0).fit(self.imgPixels)

    """
        /**
         * `predict` function of KNN Class.
         * @return  {Integer Vector} Y_Predict(Predicted Class Label for Test Data).
        */
     """
    def predict(self):
        return self.KM.predict(self.imgPixels)
