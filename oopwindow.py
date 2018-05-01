# -*- coding: utf-8 -*-
import mainwindow

class Ui_OOPWindow(mainwindow.Ui_MainWindow):
    def readFromCSV(self):
        return ''

    def setupUi(self, MainWindow):
        # 调用父类的方法
        mainwindow.Ui_MainWindow.setupUi(self, MainWindow)
        # 之后可以增加自己的方法
        # self.labelYehaibo.setText("kkkkk")
        return

    def __init__(self):
        # 这一行解决问题
        super(mainwindow.Ui_MainWindow, self).__init__()