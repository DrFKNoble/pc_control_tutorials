import sys

from PySide6 import QtCore, QtGui, QtWidgets


if __name__ == "__main__":

    app = QtWidgets.QApplication([])

    label = QtWidgets.QLabel('Hello World!')
    label.show()

    sys.exit(app.exec_())
