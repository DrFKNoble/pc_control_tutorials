import sys
import os

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = self.load_ui()
        self.ui.show()

        self.ui.pushButtonGreet.clicked.connect(self.greet)

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "mainwindow.ui")
        ui_file = QtCore.QFile(path)
        ui_file.open(QtCore.QFile.ReadOnly)
        ui = loader.load(ui_file, self)
        ui_file.close()
        return ui

    @QtCore.Slot()
    def greet(self):
        print("Hello {}!".format(self.ui.lineEditUsername.text()))
        return


if __name__ == "__main__":

    app = QtWidgets.QApplication([])

    window = MainWindow()

    sys.exit(app.exec_())