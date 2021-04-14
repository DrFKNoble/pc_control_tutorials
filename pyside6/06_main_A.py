import sys

from PySide6 import QtCore, QtGui, QtWidgets

from ui_mainwindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonGreet.clicked.connect(self.greet)

    @QtCore.Slot()
    def greet(self):
        print("Hello {}!".format(self.ui.lineEditUsername.text()))
        return

if __name__ == "__main__":

    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
