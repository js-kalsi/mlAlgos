"""
*
*    # Coded by `AAJ2018 Team`.
*    # Implementation of "Framework for Malware analysis in Android" research paper by Christian & Andres".
*    # PyQt5 Library is  used for creating the Table in order to observe the different Machine Learning classifiers.
*
"""

from PyQt5.QtWidgets import QMainWindow, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
from lib.constants import CONST


class tableGenerator(QWidget):

    def __init__(self):
        super().__init__()
        self.title = CONST['TITLE'] # Setting Title for the Table.
        # Setting Table's position.
        self.left = 0
        self.top = 0
        self.width = 543
        self.height = 154


    """
        /**
         * This function initializes the UI parameter for the table.
         * @param  {Key-value pair Array Vector} params.
        */
    """
    def initUI(self, params):
        self.setWindowTitle(self.title) # Setting Window's Title Name.
        self.setGeometry(self.left, self.top, self.width, self.height) # Setting the Orientation of the Table w.r.t the Screen.
        self.createTable(params) # Populating the data inside Table.

        # Add box layout, add table to box layout and add box layout to widget.
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        # Show widget
        self.show()


    """
        /**
         * This function populates the data inside the Table.
         * @param  {Key-value pair Array Vector} params.
        */
    """
    def createTable(self, params):
        # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(params['HEADERS'])

        self.tableWidget.setItem(0, 0, QTableWidgetItem("K-Neighbor"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem(str(params["KNN_Normal"][0]) + ',  ' + str(params["KNN_Malware"][0])) )
        self.tableWidget.setItem(0, 2, QTableWidgetItem(str(params["KNN_Normal"][1]) + ',  ' + str(params["KNN_Malware"][1])) )
        self.tableWidget.setItem(0, 3, QTableWidgetItem(str(params["KNN_Normal"][2]) + ',  ' + str(params["KNN_Malware"][2])) )
        self.tableWidget.setItem(0, 4, QTableWidgetItem(str(params["KNN_Normal"][3]) + ',  ' + str(params["KNN_Malware"][3])) )

        self.tableWidget.setItem(1, 0, QTableWidgetItem("Decision-Tree") )
        self.tableWidget.setItem(1, 1, QTableWidgetItem(str(params["DT_Normal"][0]) + ',  ' + str(params["DT_Malware"][0])) )
        self.tableWidget.setItem(1, 2, QTableWidgetItem(str(params["DT_Normal"][1]) + ',  ' + str(params["DT_Malware"][1])) )
        self.tableWidget.setItem(1, 3, QTableWidgetItem(str(params["DT_Normal"][2]) + ',  ' + str(params["DT_Malware"][2])) )
        self.tableWidget.setItem(1, 4, QTableWidgetItem(str(params["DT_Normal"][3]) + ',  ' + str(params["DT_Malware"][3])) )

        self.tableWidget.setItem(2, 0, QTableWidgetItem("SVM"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem(str(params["DT_Normal"][0]) + ',  ' + str(params["SVM_Malware"][0])))
        self.tableWidget.setItem(2, 2, QTableWidgetItem(str(params["DT_Normal"][1]) + ',  ' + str(params["SVM_Malware"][1])))
        self.tableWidget.setItem(2, 3, QTableWidgetItem(str(params["DT_Normal"][2]) + ',  ' + str(params["SVM_Malware"][2])))
        self.tableWidget.setItem(2, 4, QTableWidgetItem(str(params["DT_Normal"][3]) + ',  ' + str(params["SVM_Malware"][3])))
        self.tableWidget.move(0, 0)



