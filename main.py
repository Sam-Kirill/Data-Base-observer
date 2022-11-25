import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication
import sqlite3

class dbWindow(QDialog):
    def __init__(self, parent=None):
        super(). __init__(parent)
        loadUi('dbwindow.ui', self)
        self.loaddata()
        self.btn.clicked.connect(self.close)

    def loaddata(self):
        connection = sqlite3.connect('housestaff.db')
        c = connection.cursor()
        sqlquery = "SELECT * FROM housestaff"
        self.tableWidget.setRowCount(50)
        tablerow = 0

        for row in c.execute(sqlquery):
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))

            tablerow+=1

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self). __init__()
        loadUi('MainWindow.ui', self)
        self.btn.clicked.connect(self.create_window)
        self.btn1.clicked.connect(QCoreApplication.instance().quit)

    def create_window(self):
        self.MainWindokw = dbWindow(self)
        self.MainWindokw.show()

def application():
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(600)
    widget.setFixedHeight(485)
    widget.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    application()
