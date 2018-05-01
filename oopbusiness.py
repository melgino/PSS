# -*- coding: utf-8 -*-
import sys
import mainwindow
import oopui
from PyQt5.QtWidgets import QApplication, QMainWindow

class Business():

    # 构造函数
    def __init__(self):
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        # you need to invoke your code yourself
        ui = oopui.Ui_OOPWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
        return

