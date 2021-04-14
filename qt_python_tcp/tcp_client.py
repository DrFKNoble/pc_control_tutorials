import os
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import qDebug, QFile, Signal, Slot
from PySide6.QtUiTools import QUiLoader

from PySide6.QtNetwork import QHostAddress, QTcpSocket


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = self.load_ui()
        self.ui.show()
    
        self.socket = QTcpSocket()
    
        self.ui.pushButtonConnect.clicked.connect(self.connect)
        self.ui.pushButtonSend.clicked.connect(self.send)
        self.ui.lineEditSend.returnPressed.connect(self.send)
        
        self.ui.actionQuit.triggered.connect(self.quit)

        self.socket.connected.connect(self.onConnection)

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "client.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        ui = loader.load(ui_file, self)
        ui_file.close()
        return ui

    @Slot()
    def send(self):
        if self.socket.state() == QTcpSocket.ConnectedState:
            message = self.ui.lineEditSend.text()
            self.ui.textEditDisplay.append(message)
            self.socket.write(message.encode("utf-8"))
        return

    @Slot()
    def connect(self):
        if self.ui.pushButtonConnect.text() == "Connect":
            address = self.ui.lineEditAddress.text()
            port = self.ui.lineEditPort.text()
            self.socket.connectToHost(QHostAddress(address), int(port))
        else:
            self.ui.pushButtonConnect.setText("Connect")
            self.socket.close()
        return

    @Slot()
    def onConnection(self):
        self.ui.pushButtonConnect.setText("Disconnect")
        address = self.ui.lineEditAddress.text()
        port = self.ui.lineEditPort.text()
        message = "Connected to host <{}:{}>".format(address, port)
        self.ui.textEditDisplay.append(message)
        return

    @Slot()
    def quit(self):
        QApplication.quit()
        return


if __name__ == "__main__":

    app = QApplication([])

    window = MainWindow()

    sys.exit(app.exec_())
