"""
*
*    # Implementation of "Framework for malware analysis in Android" research paper by Christian & Andres.
*    # Helper Class: Contains the Tools.
*
"""

from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from math import ceil as CEIL

class helpers:

    """
        /**
         * Computes the True-Positive, False-Positive, True-Negative & False-Negative.
         * @param  {Integer Vector} Y_test(Training Data).
         * @param  {Integer Vector} Y_pred(Training Class Label).
         * @returns {Float} True-Positive, False-Positive, True-Negative & False-Negative.
        */
    """
    def performanceMeasure(self, Y_test, Y_pred):
        return confusion_matrix(Y_test, Y_pred).ravel()



    """
        /**
         * Computes the Precision.
         * @param  {Integer Vector} truePositive.
         * @param  {Integer Vector} falsePositive.
         * @returns {Integer Vector} Precision.
        */
    """
    def Precision(self, Y_test_Malware, Y_predict_Malware, Y_test_Normal, Y_predict_Normal):
        return self.roundOff(precision_score(Y_test_Malware, Y_predict_Malware, average='micro')), self.roundOff(precision_score(Y_test_Normal, Y_predict_Normal, average='micro'))



    """
        /**
         * Computes the Recall.
         * @param  {Integer Vector} Y_test(Training Data).
         * @param  {Integer Vector} Y_pred(Training Class Label).
         * @returns  {Float} Recall.
        */
    """
    def Recall(self, Y_test_Malware, Y_predict_Malware, Y_test_Normal, Y_predict_Normal):
        return self.roundOff(recall_score(Y_test_Malware, Y_predict_Malware, average='micro')), self.roundOff(recall_score(Y_test_Normal, Y_predict_Normal, average='micro'))

    """
        /**
         * Computes the Accuracy.
         * @param  {Integer Vector} Y_test(Training Data).
         * @param  {Integer Vector} Y_pred(Training Class Label).
         * @returns  {Float} Accuracy.
        */
    """
    def accuarycyScore(self, Y_test, Y_test_predict, Y_test_Malware, Y_predict_KNN_Malware, Y_test_Normal, Y_predict_KNN_Normal):
        return self.roundOff(accuracy_score(Y_test, Y_test_predict)), self.roundOff(accuracy_score(Y_test_Malware, Y_predict_KNN_Malware)), self.roundOff(accuracy_score(Y_test_Normal, Y_predict_KNN_Normal))

    """
        /**
         * Computes the f1_score.
         * @param  {Integer Vector} Y_true(Training Data).
         * @param  {Integer Vector} Y_pred(Training Class Label).
         * @returns  {Float} f1_score.
        */
    """
    def f1_Score(self, Y_test_Malware, Y_predict_KNN_Malware, Y_test_Normal, Y_predict_KNN_Normal):
        return self.roundOff(f1_score(Y_test_Malware, Y_predict_KNN_Malware, average='micro')), self.roundOff(f1_score(Y_test_Normal, Y_predict_KNN_Normal, average='micro'))


    """
        /**
         * Round-off value upto 2 decimal places.
         * @param  {float} data.
         * @returns  {Float} Round-Off data.
        */
    """
    def roundOff(self, data):
        return CEIL(data* 100)/100

    """
        /**
         * Display the Contents over the Screen in a Specific Manner.
         * @param  {String} paramOne.
         * @param  {String} paramTwo.
         * @param  {String} paramThree.
        */
    """
    def display(self, paramOne, paramTwo, paramThree):
        print(('{0}\'s {1} : {2}').format(paramOne, paramTwo, paramThree))


    """
        /**
         * Display the String over the Screen.
         * @param  {String} paramOne.
         * @param  {String} paramTwo.
         * @param  {String} paramThree.
        */
    """

    def displayString(self, paramOne):
        print(('{0}').format(paramOne))


    """
        /**
         * Move the Cursor according to the (X,Y) Coordinates.
         * @param  {String} X: x point.
         * @param  {String} Y: y point.
        */
    """
    def gotoxy(x, y):
        print ("%c[%d;%df" % (0x1B, y, x))

