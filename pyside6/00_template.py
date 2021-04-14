import sys

from PySide6 import QtCore, QtGui, QtWidgets

class Template(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.name = "Template"

    @QtCore.Slot()
    def __name__(self):
        print(self.name)
        return


if __name__ == "__main__":

    app = QtWidgets.QApplication([])

    template = Template()
    template.show()
    
    print(template.__name__())

    sys.exit(app.exec_())
