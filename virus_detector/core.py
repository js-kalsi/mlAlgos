"""
*
*    # Coded by Jaspreet Singh Kalsi.
*    # Implementation of "Framework for malware analysis in Android" research paper by Christian & Andres.
*    # Feature Extracted : From Android_Manifest.xml.
*    # Algorithm used for Classification : K-Nearest-Neighbor, Decision Tree & SVM.
*    # Assessment Measurements: Accuracy, Precision & Recall.
*
"""
import sys  # Provides access to some variables used or maintained by the interpreter.
from dataSet import dataSet  # Importing DataSet
from KNN import KNN  # contains KNN related functionality.
from DTree import DecisionTree  # contains DecisionTree related functionality.
from SVM import SVM  # contains SVM related functionality.
from lib.helpers import helpers as HELPER  # class contains the logic like performanceMeasure, Precision etc.
from lib.constants import CONST  # contains the constant values.
from PyQt5.QtWidgets import QApplication  # provides classes that provide a set of UI elements to create desktop GUI.
from table import tableGenerator  # contains the table creation Logic.


# Fetching the training data and Labels from the `dataSet` class.
X_train, Y_train = dataSet(CONST['TRAINING_FILE'], False).loadCsv()

# Fetching the test data and Class Labels of both Malware & Normal Applications from the `dataSet` class.
X_test, Y_test, X_test_Malware, Y_test_Malware, X_test_Normal, Y_test_Normal = dataSet(CONST['TEST_FILE'], True).loadCsv()


"""
*
*  K-Nearest Neighbor Classifier Begins
*
"""

# KNN classifier: predicting both Malware & Normal Application's Test Class Label.
Y_predict_KNN, Y_predict_KNN_Malware, Y_predict_KNN_Normal = KNN(X_train, Y_train, X_test, X_test_Malware, X_test_Normal).predict()


# `performanceMeasure()` of HELPER class return the values of True Positive, False Positive,
#  False Negative & True Negative for Malware Oriented Data.
TN_KNN_Malware, FP_KNN_Malware, FN_KNN_Malware, TP_KNN_Malware  = HELPER().performanceMeasure(Y_test_Malware, Y_predict_KNN_Malware)

# `performanceMeasure()` of HELPER class return the values of True Positive, False Positive,
#  False Negative & True Negative for Normal Data.
TN_KNN_Normal, FP_KNN_Normal, FN_KNN_Normal, TP_KNN_Normal = HELPER().performanceMeasure(Y_test_Normal, Y_predict_KNN_Normal)

# `Precision()` of HELPER class return the values of Precision for KNN Classifier.
precision_KNN_Malware, precision_KNN_Normal = HELPER().Precision(Y_test_Malware, Y_predict_KNN_Malware, Y_test_Normal, Y_predict_KNN_Normal)

# `Recall()` of HELPER class return  the values of Recall for KNN Classifier.
recall_KNN_Malware, recall_KNN_Normal = HELPER().Recall(Y_test_Malware, Y_predict_KNN_Malware, Y_test_Normal, Y_predict_KNN_Normal)

# `accuracyScore()` of HELPER class return the values of Accuracy for KNN Classifier.
accuracy_KNN, accuracy_KNN_Malware, accuracy_KNN_Normal = HELPER().accuarycyScore(Y_test, Y_predict_KNN, Y_test_Malware, Y_predict_KNN_Malware, Y_test_Normal, Y_predict_KNN_Normal)

# `f1_Score()` of HELPER class return the values of f1_score for KNN Classifier.
f1_Score_KNN_Malware, f1_Score_KNN_Normal = HELPER().f1_Score(Y_test_Malware, Y_predict_KNN_Malware, Y_test_Normal, Y_predict_KNN_Normal)


HELPER().displayString("*****************************************************")
HELPER().display("KNN", "Malware Precision", precision_KNN_Malware)
HELPER().display("KNN", "Malware Recall", recall_KNN_Malware)
HELPER().display("KNN", "Malware Accuracy", accuracy_KNN_Malware)
HELPER().display("KNN", "Malware f1_Score", f1_Score_KNN_Malware)
print("")
HELPER().display("KNN", "Normal Precision", precision_KNN_Normal)
HELPER().display("KNN", "Normal Recall", recall_KNN_Normal)
HELPER().display("KNN", "Normal Accuracy", accuracy_KNN_Normal)
HELPER().display("KNN", "Normal f1_Score", f1_Score_KNN_Normal)
print("")
HELPER().display("KNN", "Accuracy", accuracy_KNN)
print("\n\n")

""" K-Nearest Neighbor Classifier ends here. """




"""
*
*  Decision-Tree Classifier Begins.
*
"""

# Decision-Tree classifier: predicting both Malware & Normal Application's Test Class Label.
Y_predict_DT, Y_predict_DT_Malware, Y_predict_DT_Normal = DecisionTree(X_train, Y_train, X_test, X_test_Malware, X_test_Normal).predict()

# `performanceMeasure()` of HELPER class return the values of True Positive, False Positive,
#  False Negative & True Negative for Normal Data.
TN_DT_Malware, FP_DT_Malware, FN_DT_Malware, TP_DT_Malware = HELPER().performanceMeasure(Y_test_Malware, Y_predict_DT_Malware)

# `performanceMeasure()` of HELPER class return the values of True Positive, False Positive,
#  False Negative & True Negative for Normal Data.
TN_DT_Normal, FP_DT_Normal, FN_DT_Normal, TP_DT_Normal = HELPER().performanceMeasure(Y_test_Normal, Y_predict_DT_Normal)

# `Precision()` of HELPER class return the values of Precision for Decision-Tree Classifier.
precision_DT_Malware, precision_DT_Normal  = HELPER().Precision(Y_test_Malware, Y_predict_DT_Malware, Y_test_Normal, Y_predict_DT_Normal)

# `Recall()` of HELPER class return the values of recall for Decision-Tree Classifier.
recall_DT_Malware, recall_DT_Normal  = HELPER().Recall(Y_test_Malware, Y_predict_DT_Malware, Y_test_Normal, Y_predict_DT_Normal)

# `accuarycyScore()` of HELPER class return the values of Accuracy for Decision-Tree Classifier.
accuracy_DT, accuracy_DT_Malware, accuracy_DT_Normal = HELPER().accuarycyScore(Y_test, Y_predict_DT, Y_test_Malware, Y_predict_DT_Malware, Y_test_Normal, Y_predict_DT_Normal)

# `f1_Score()` of HELPER class return the values of f1_score for Decision-Tree Classifier.
f1_Score_DT_Malware, f1_Score_DT_Normal = HELPER().f1_Score(Y_test_Malware, Y_predict_DT_Malware, Y_test_Normal, Y_predict_DT_Normal)

# Displaying the Content to the Screen.
HELPER().displayString("*****************************************************")
HELPER().display("Decision-Tree", "Malware Precision", precision_DT_Malware)
HELPER().display("Decision-Tree", "Malware Recall", recall_DT_Malware)
HELPER().display("Decision-Tree", "Malware Accuracy", accuracy_DT_Malware)
HELPER().display("Decision-Tree", "Malware f1_Score", f1_Score_DT_Malware)
print("")
HELPER().display("Decision-Tree", "Normal Precision", precision_DT_Normal)
HELPER().display("Decision-Tree", "Normal Recall", recall_DT_Normal)
HELPER().display("Decision-Tree", "Normal Accuracy", accuracy_DT_Normal)
HELPER().display("Decision-Tree", "Normal f1_Score", f1_Score_DT_Normal)
print("")
HELPER().display("Decision-Tree", "Accuracy", accuracy_DT)
print("\n \n")
""" Decision-Tree Classifier ends here. """





"""
*
*  Support Vector Machine Classifier Begins.
*
"""

# SVM classifier: predicting both Malware & Normal Application's Test Class Label.
Y_predict_SVM, Y_predict_SVM_Malware, Y_predict_SVM_Normal = SVM(X_train, Y_train, X_test, X_test_Malware, X_test_Normal).predict()

# `performanceMeasure()` of HELPER class return the values of True Positive, False Positive,
#  False Negative & True Negative for Normal Data.
TN_SVM_Malware, FP_SVM_Malware, FN_SVM_Malware, TP_SVM_Malware = HELPER().performanceMeasure(Y_test_Malware, Y_predict_SVM_Malware)

# `performanceMeasure()` of HELPER class return the values of True Positive, False Positive,
#  False Negative & True Negative for Normal Data.
TN_SVM_Normal, FP_SVM_Normal, FN_SVM_Normal, TP_SVM_Normal = HELPER().performanceMeasure(Y_test_Normal, Y_predict_SVM_Normal)

# `Precision()` of HELPER class return the values of `Precision` for SVM.
precision_SVM_Malware, precision_SVM_Normal = HELPER().Precision(Y_test_Malware, Y_predict_SVM_Malware, Y_test_Normal, Y_predict_SVM_Normal)

# `Recall()` of HELPER class return the values of `Recall` for SVM.
recall_SVM_Malware, recall_SVM_Normal = HELPER().Recall(Y_test_Malware, Y_predict_SVM_Malware, Y_test_Normal, Y_predict_SVM_Normal)

# `accuarycyScore()` of HELPER class return the values of Accuracy for SVM Classifier.
accuracy_SVM, accuracy_SVM_Malware, accuracy_SVM_Normal = HELPER().accuarycyScore(Y_test, Y_predict_SVM, Y_test_Malware, Y_predict_SVM_Malware, Y_test_Normal, Y_predict_SVM_Normal)

# `f1_Score()` of HELPER class return the values of f1_score for SVM Classifier.
f1_Score_SVM_Malware, f1_Score_SVM_Normal = HELPER().f1_Score(Y_test_Malware, Y_predict_SVM_Malware, Y_test_Normal, Y_predict_SVM_Normal)


# Displaying the Content to the Screen.
HELPER().displayString("*****************************************************")
HELPER().display("SVM", "Malware Precision", precision_SVM_Malware)
HELPER().display("SVM", "Malware Recall", recall_SVM_Malware)
HELPER().display("SVM", "Malware Accuracy", accuracy_SVM_Malware)
HELPER().display("SVM", "Malware f1_Score", f1_Score_SVM_Malware)
print("")
HELPER().display("SVM", "Normal Precision", precision_SVM_Normal)
HELPER().display("SVM", "Normal Recall", recall_SVM_Normal)
HELPER().display("SVM", "Normal Accuracy", accuracy_SVM_Normal)
HELPER().display("SVM", "Normal f1_Score", f1_Score_SVM_Normal)
print("")
HELPER().display("SVM", "Accuracy", accuracy_SVM)

""" Support Vector Machine Classifier ends here. """


"""
*
*  Logic for putting all the Machine Learning Classifiers(KNN, DT, SVM) result in the Tabular form.
*
"""

tableView = QApplication(sys.argv)
tableObj = tableGenerator()
params = {}
params['HEADERS'] = CONST['HEADERS']
params['KNN_Malware'] = [precision_KNN_Malware, recall_KNN_Malware, accuracy_KNN_Malware, f1_Score_KNN_Malware]
params['KNN_Normal'] = [precision_KNN_Normal, recall_KNN_Normal, accuracy_KNN_Normal, f1_Score_KNN_Normal]
params['KNN_accuracy'] = accuracy_KNN
params['DT_Malware'] = [precision_DT_Malware, recall_DT_Malware, accuracy_DT_Malware, f1_Score_DT_Malware]
params['DT_Normal'] = [precision_DT_Normal, recall_DT_Normal, accuracy_DT_Normal, f1_Score_DT_Normal]
params['DT_accuracy'] = accuracy_DT
params['SVM_Malware'] = [precision_SVM_Malware, recall_SVM_Malware, accuracy_SVM_Malware, f1_Score_SVM_Malware]
params['SVM_Normal'] = [precision_SVM_Normal, recall_SVM_Normal, accuracy_SVM_Normal, f1_Score_SVM_Normal]
params['SVM_accuracy'] = accuracy_SVM

tableObj.initUI(params)
sys.exit(tableView.exec_())