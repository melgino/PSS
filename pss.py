import sys
import mainwindow
import oopui
from PyQt5.QtWidgets import QApplication, QMainWindow

####################################
# test github
# test github2
# test github3
# test github push code in pycharm
#
#
#
####################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    # you need to invoke your code yourself
    ui = oopui.Ui_OOPWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())