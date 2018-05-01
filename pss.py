import sys
import mainwindow
from PyQt5.QtWidgets import QApplication, QMainWindow

####################################
# test github
#
#
#
####################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    # you need to invoke your code yourself
    ui = mainwindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())