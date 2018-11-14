"""
*
*    # Coded by `AAJ2018 Team`.
*    # Implementation of "Framework for malware analysis in Android" research paper by Christian & Andres.
*    # Support Vector Machine's Implementation.
*
"""
from sklearn import svm
import numpy as np

class SVM:


    """
        /**
         * Constructor of SVM Class.
         * @param  {Integer Vector} X_train(Training Data).
         * @param  {Integer Vector} Y_train(Training Class Label).
         * @param  {Integer Vector} X_test(Test Data).
         * @param  {Integer Vector} Y_test(Test Class Label).
        */
     """
    def __init__(self, X_train, Y_train, X_test, X_test_Malware, X_test_Normal):
        self.X_train = X_train
        self.Y_train = Y_train
        self.X_test = X_test
        self.X_test_Malware = X_test_Malware
        self.X_test_Normal = X_test_Normal
        self.clf = svm.SVC(kernel='linear', C = 1.0) # Calling SVM Classifier with kernal='linear' & SVM's regularization parameter(C) as 1.0.       self.clf.fit(self.X_train, self.Y_train) # Fitting the Training Data and their respective Class Label.
        self.clf.fit(X_train, Y_train) # Fitting the Training Data and their respective Class Label.


    """
        /**
         * `predict` function of SVM Class.
         * @return  {Integer Vector} Y_Predict(Predicted Class Label for Test Data).
        */
    """
    def predict(self):
        # Predicting the Class Label for both Malware & Normal Data.
        return self.clf.predict(self.X_test), self.clf.predict(self.X_test_Malware), self.clf.predict(self.X_test_Normal)
