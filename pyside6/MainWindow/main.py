# This Python file uses the following encoding: utf-8
import sys
import os


from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QObject, QFile, Signal, Slot
from PySide6.QtUiTools import QUiLoader


class MainWindow(QMainWindow, QObject):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = self.load_ui()
        self.ui.show()

        self.ui.pushButtonGreet.clicked.connect(self.greet)
        self.msg.connect(self.message)
              
    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        ui = loader.load(ui_file, self)
        ui_file.close()
        return ui

    msg = Signal()

    @Slot()
    def greet(self):
        print("Hello {}".format(self.ui.lineEditUsername.text()))
        self.msg.emit()
        return
    
    @Slot()
    def message(self):
        print("Message")
        return


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
#    widget.show()
    sys.exit(app.exec_())
