"""
*
*    # Coded by `AAJ2018 Team`.
*    # Implementation of "Framework for malware analysis in Android" research paper by Christian & Andres.
*    # K-Nearest Neighbor Implementation.
*
"""
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

class KNN:


    """
        /**
         * @param  {Integer Vector} X_train(Training Data).
         * @param  {Integer Vector} Y_train(Training Class Label).
         * @param  {Integer Vector} X_test(Test Data).
         * @param  {Integer Vector} X_test_Malware (Malware Test Data).
         * @param  {Integer Vector} X_test_Normal (Normal Test Data).
        */
    """

    def __init__(self, X_train, Y_train, X_test, X_test_Malware, X_test_Normal):
        self.X_train = X_train
        self.Y_train = Y_train
        self.X_test = X_test
        self.X_test_Malware = X_test_Malware
        self.X_test_Normal = X_test_Normal
        self.KNN = KNeighborsClassifier(n_neighbors=4) # Calling K-Neighbor Classifier & giving neighbor parameter as 4.
        self.KNN.fit(self.X_train, self.Y_train) # Fitting the Training Data and their respective Class Label.


    """
        /**
         * `predict` function of KNN Class.
         * @return  {Integer Vector} Y_Predict(Predicted Class Label for Test Data).
        */
     """
    def predict(self):
        # Predicting the Class Label for both Malware & Normal Data.
        return self.KNN.predict(self.X_test), self.KNN.predict(self.X_test_Malware), self.KNN.predict(self.X_test_Normal)