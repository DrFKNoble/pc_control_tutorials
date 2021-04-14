import sys

from PySide6 import QtCore, QtGui, QtWidgets


@QtCore.Slot()
def greet():
    print("Hello World!")


if __name__ == "__main__":

    app = QtWidgets.QApplication([])

    button = QtWidgets.QPushButton("Click Me!")
    button.clicked.connect(greet)

    button.show()

    sys.exit(app.exec_())
