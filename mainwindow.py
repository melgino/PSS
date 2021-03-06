# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(627, 311)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.yehaibopush = QtWidgets.QPushButton(self.centralWidget)
        self.yehaibopush.setGeometry(QtCore.QRect(480, 200, 85, 29))
        self.yehaibopush.setObjectName("yehaibopush")
        self.labelYehaibo = QtWidgets.QLabel(self.centralWidget)
        self.labelYehaibo.setGeometry(QtCore.QRect(40, 10, 81, 21))
        self.labelYehaibo.setObjectName("labelYehaibo")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 120, 85, 29))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 627, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuGet_Character = QtWidgets.QMenu(self.menuBar)
        self.menuGet_Character.setObjectName("menuGet_Character")
        self.menuProcess_Character = QtWidgets.QMenu(self.menuBar)
        self.menuProcess_Character.setObjectName("menuProcess_Character")
        self.menuClean = QtWidgets.QMenu(self.menuProcess_Character)
        self.menuClean.setObjectName("menuClean")
        self.menuPre_Process = QtWidgets.QMenu(self.menuProcess_Character)
        self.menuPre_Process.setObjectName("menuPre_Process")
        self.menucharacter = QtWidgets.QMenu(self.menuBar)
        self.menucharacter.setObjectName("menucharacter")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionFrom_redis = QtWidgets.QAction(MainWindow)
        self.actionFrom_redis.setObjectName("actionFrom_redis")
        self.actionFrom_Kafka = QtWidgets.QAction(MainWindow)
        self.actionFrom_Kafka.setObjectName("actionFrom_Kafka")
        self.actionFrom_Elasticsearch = QtWidgets.QAction(MainWindow)
        self.actionFrom_Elasticsearch.setObjectName("actionFrom_Elasticsearch")
        self.actionFrom_Mysql = QtWidgets.QAction(MainWindow)
        self.actionFrom_Mysql.setObjectName("actionFrom_Mysql")
        self.actionFrom_Mongodb = QtWidgets.QAction(MainWindow)
        self.actionFrom_Mongodb.setObjectName("actionFrom_Mongodb")
        self.actionFrom_Oracle = QtWidgets.QAction(MainWindow)
        self.actionFrom_Oracle.setObjectName("actionFrom_Oracle")
        self.actionOutlier = QtWidgets.QAction(MainWindow)
        self.actionOutlier.setObjectName("actionOutlier")
        self.actionanti_spam = QtWidgets.QAction(MainWindow)
        self.actionanti_spam.setObjectName("actionanti_spam")
        self.actionData = QtWidgets.QAction(MainWindow)
        self.actionData.setObjectName("actionData")
        self.actionChooose = QtWidgets.QAction(MainWindow)
        self.actionChooose.setObjectName("actionChooose")
        self.actionCombination = QtWidgets.QAction(MainWindow)
        self.actionCombination.setObjectName("actionCombination")
        self.actionDecrease = QtWidgets.QAction(MainWindow)
        self.actionDecrease.setObjectName("actionDecrease")
        self.menuGet_Character.addAction(self.actionFrom_redis)
        self.menuGet_Character.addAction(self.actionFrom_Kafka)
        self.menuGet_Character.addAction(self.actionFrom_Elasticsearch)
        self.menuGet_Character.addAction(self.actionFrom_Mysql)
        self.menuGet_Character.addAction(self.actionFrom_Mongodb)
        self.menuGet_Character.addAction(self.actionFrom_Oracle)
        self.menuClean.addAction(self.actionOutlier)
        self.menuClean.addAction(self.actionanti_spam)
        self.menuPre_Process.addAction(self.actionData)
        self.menuPre_Process.addAction(self.actionChooose)
        self.menuPre_Process.addAction(self.actionCombination)
        self.menuPre_Process.addAction(self.actionDecrease)
        self.menuProcess_Character.addAction(self.menuClean.menuAction())
        self.menuProcess_Character.addAction(self.menuPre_Process.menuAction())
        self.menuBar.addAction(self.menuGet_Character.menuAction())
        self.menuBar.addAction(self.menuProcess_Character.menuAction())
        self.menuBar.addAction(self.menucharacter.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.yehaibopush.setText(_translate("MainWindow", "yehaibo"))
        self.labelYehaibo.setText(_translate("MainWindow", "FirstYehaibo"))
        self.pushButton.setText(_translate("MainWindow", "Test2"))
        self.menuGet_Character.setTitle(_translate("MainWindow", "Get Character"))
        self.menuProcess_Character.setTitle(_translate("MainWindow", "Process Character"))
        self.menuClean.setTitle(_translate("MainWindow", "Clean"))
        self.menuPre_Process.setTitle(_translate("MainWindow", "Pre-Process"))
        self.menucharacter.setTitle(_translate("MainWindow", "Monitor Character"))
        self.actionFrom_redis.setText(_translate("MainWindow", "From Redis"))
        self.actionFrom_Kafka.setText(_translate("MainWindow", "From Kafka"))
        self.actionFrom_Elasticsearch.setText(_translate("MainWindow", "From Elasticsearch"))
        self.actionFrom_Mysql.setText(_translate("MainWindow", "From Mysql"))
        self.actionFrom_Mongodb.setText(_translate("MainWindow", "From Mongodb"))
        self.actionFrom_Oracle.setText(_translate("MainWindow", "From Oracle"))
        self.actionOutlier.setText(_translate("MainWindow", "Outlier"))
        self.actionanti_spam.setText(_translate("MainWindow", "Anti-Spam"))
        self.actionData.setText(_translate("MainWindow", "Data"))
        self.actionChooose.setText(_translate("MainWindow", "Chooose"))
        self.actionCombination.setText(_translate("MainWindow", "Combination"))
        self.actionDecrease.setText(_translate("MainWindow", "Decrease Dimension"))


