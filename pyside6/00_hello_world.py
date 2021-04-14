import sys

from PySide6 import QtCore, QtWidgets, QtGui


class GreetingWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.greeting = "Hello"

        self.button = QtWidgets.QPushButton('Click me!')
        self.label = QtWidgets.QLabel('Greeting', alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.greet)

    @QtCore.Slot()
    def greet(self):
        self.label.setText(self.greeting)
        return


if __name__ == "__main__":

    app = QtWidgets.QApplication([])

    widget = GreetingWidget()
    widget.resize(320, 240)
    widget.show()

    sys.exit(app.exec_())
