import sys

from PySide6 import QtCore, QtGui, QtWidgets


class Form(QtWidgets.QDialog):

    def __init__(self, parent=None):

        super(Form, self).__init__(parent)
        self.setWindowTitle("My Form")

        self.label = QtWidgets.QLabel('Username:')
        self.username = QtWidgets.QLineEdit("")
        self.button = QtWidgets.QPushButton("Click Me!")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.username)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.greet)

    @QtCore.Slot()
    def greet(self):
        print("Hello {}".format(self.username.text()))


if __name__ == "__main__":

    app = QtWidgets.QApplication([])

    form = Form()
    form.show()

    sys.exit(app.exec_())
