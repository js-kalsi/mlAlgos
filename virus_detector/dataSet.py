"""
*
*    # Coded by `AAJ2018 Team`.
*    # Implementation of "Framework for malware analysis in Android" research paper by Christian & Andres.
*    # DataSet Extraction from CSV files.
*
"""

import pandas as pd

class dataSet:

    """
         /**
          * Constructor of dataSet Class.
          * @param  {String} fileName.
          * @param  {Boolean} isTest.
         */
    """

    def __init__(self, fileName, isTest):
        self.fileName = fileName
        self.isTest = isTest

    """
        /**
         * `loadCsv` function of dataSet Class.
         * @return  {Integer Vector} vector X & Y.
        */
    """
    def loadCsv(self):
        dataSet = pd.read_csv("./dataset/" + self.fileName)
        X = dataSet.iloc[:, :-1].values  # Permission's Data.
        Y = dataSet.iloc[:, -1].values  # Class-Label.

        X_test_Malware = []  # Array for storing Malware's Test Data.
        Y_test_Malware = []  # Array for storing Malware's Test Class Label.
        X_test_Normal = []  # Array for storing Normal's Test Data.
        Y_test_Normal = []  # Array for storing Normal's Test Class Label.

        if self.isTest:
            labelIndex = len(dataSet.iloc[:].values[0]) - 1

            for data in dataSet.iloc[:].values:

                if data[labelIndex] == 1:
                    X_test_Malware.append(data[:-1])
                    Y_test_Malware.append(data[-1])
                else:
                    X_test_Normal.append(data[:-1])
                    Y_test_Normal.append(data[-1])

            return X, Y, X_test_Malware, Y_test_Malware, X_test_Normal, Y_test_Normal
        else:
            return X, Y


    """
        /**
         * `Bagging` function of dataSet Class.
         * @return  {Integer Array} dataSet.
        */
    """
    def Bagging(self, X, XPerc, featurePerc):
        return X[:int(round((XPerc * len(X))/100)), :int(round((featurePerc * len(X[0]))/100))]


    """
        /**
         * `randomDataSetGenerator` function of dataSet Class.
         * @return  {Integer Vector} dataSet.
        */
    """
    def randomDataSetGenerator(self, dataSet, noOfVector, widthOfVector):
        return self