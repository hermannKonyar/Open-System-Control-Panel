

from asyncio import subprocess
from typing import Text
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import subprocess as sb
import sqlite3 as sq
import os


class Ui_MainWindow(object):

    def __init__(self):
        self.prcs = Process()
        self.sql_name = 'data.sql'
        self.check_sql = os.path.exists(self.sql_name)

        self.sql = sq.connect(self.sql_name)
        self.im = self.sql.cursor()
        self.query = """CREATE TABLE IF NOT EXISTS data
(Name, Mail, Ip, Status)"""
        self.im.execute(self.query)
        self.sql.commit()

        if self.check_sql:
            self.UpdateList()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1270, 836)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1270, 800))
        self.centralwidget.setMaximumSize(QtCore.QSize(1270, 800))
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 781, 561))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(895, 70, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(800, 70, 61, 21))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(895, 120, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(895, 160, 113, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(800, 120, 51, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(800, 160, 51, 21))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(895, 200, 61, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.AddToList)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(255, 600, 71, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(965, 200, 61, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(800, 240, 391, 351))
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(800, 210, 51, 31))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(1075, 70, 151, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(1075, 120, 113, 21))
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1075, 30, 111, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1075, 90, 81, 31))
        self.label_6.setObjectName("label_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1040, 610, 71, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(950, 610, 71, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(170, 600, 71, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.SaveData)
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(1080, 150, 51, 21))
        self.statusLabel.setText("")
        self.statusLabel.setObjectName("statusLabel")
        self.statusLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel2.setGeometry(QtCore.QRect(1124, 610, 61, 31))
        self.statusLabel2.setText("")
        self.statusLabel2.setObjectName("statusLabel2")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(340, 600, 71, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.check)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1270, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "User Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Mail Adress"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ip"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_2.setText(_translate("MainWindow", "Mail"))
        self.label_3.setText(_translate("MainWindow", "Ip"))
        self.pushButton.setText(_translate("MainWindow", "Add"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear"))
        self.label_4.setText(_translate("MainWindow", "Text"))
        self.label_5.setText(_translate("MainWindow", "Mail "))
        self.label_6.setText(_translate("MainWindow", "Password"))
        self.pushButton_4.setText(_translate("MainWindow", "Send"))
        self.pushButton_5.setText(_translate("MainWindow", "Clear"))
        self.pushButton_6.setText(_translate("MainWindow", "Save"))
        self.pushButton_7.setText(_translate("MainWindow", "Check"))

    def UpdateList(self):
            self.im.execute("SELECT * FROM data")
            self.datas = self.im.fetchall()
            for j in self.datas:
                self.prcs.AddToList(j[0],j[0],j[0],j[0])

    def AddToList(self, Mainwindow):
        self.prcs.AddToList(self.lineEdit.text(
        ), self.lineEdit_2.text(), self.lineEdit_3.text(), 'Offline')

    def check(self, Mainwindow):
        self.prcs.IpCheck()

    def SaveData(self, Mainwindow):
        self.prcs.SaveList()

    


class Process():
    def __init__(self):
        self.row_count = 0
        self.ip_list = []
        self.status_list = []

    def AddToList(self, name, mail, ip, status):
        ui.tableWidget.setRowCount(self.row_count+1)
        liste = [name, mail, ip, status]
        for i in range(4):
            ui.tableWidget.setItem(
                self.row_count, i, QtWidgets.QTableWidgetItem(liste[i]))
        self.row_count += 1
        self.ListInit()

    def ListInit(self):
        for i in range(ui.tableWidget.rowCount()):
            if ui.tableWidget.item(i, 3).text() == 'Offline':
                ui.tableWidget.item(i, 3).setBackground(
                    QtGui.QColor(255, 0, 0))
            else:
                ui.tableWidget.item(i, 3).setBackground(
                    QtGui.QColor(0, 255, 0))

    def IpCheck(self):
        for i in range(ui.tableWidget.rowCount()):
            self.ip_list.append(ui.tableWidget.item(i, 2).text())
        for i in self.ip_list:
            ping_send = sb.call(f'ping {i} -n 4')
            if ping_send == 0:
                self.status_list.append('Online')
            else:
                self.status_list.append('Offline')
        for i, j in enumerate(self.status_list):
            ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(j))
            if ui.tableWidget.item(i, 3).text() == 'Online':
                ui.tableWidget.item(i, 3).setBackground(
                    QtGui.QColor(0, 255, 0))
        self.ListInit()

    def SaveList(self):
        outPut = []
        for i in range(ui.tableWidget.rowCount()):
            row_data = []
            for j in range(ui.tableWidget.columnCount()):
                row_data.append(ui.tableWidget.item(i, j).text())
            outPut.append(row_data)

        for i in outPut:
            text = f"INSERT INTO data  VALUES ('{i[0]}','{i[1]}','{i[2]}','{i[3]}')"
            ui.im.execute(text)
            ui.sql.commit()


app = QtWidgets.QApplication(sys.argv)
pencere = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(pencere)
pencere.show()
sys.exit(app.exec_())
