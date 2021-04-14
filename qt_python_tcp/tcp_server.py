import os
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import qDebug, QFile, Signal, Slot
from PySide6.QtUiTools import QUiLoader

from PySide6.QtNetwork import QHostAddress, QTcpServer, QTcpSocket

import serial
import serial.tools.list_ports

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = self.load_ui()
        self.ui.show()

        self.ser = serial.Serial()

        self.baudRate = "9600"
        self.dataSize = "8"
        self.parity = "N"
        self.stopBits = "1"
        self.flowControl = "False"
        self.COMPort = "COM3"
        self.timeout = 5.0

        self.server = QTcpServer()
        self.socket = QTcpSocket()

        [self.ui.comboBoxBaudRate.addItem(str(i)) for i in self.ser.BAUDRATES]
        self.ui.comboBoxBaudRate.setCurrentText(self.baudRate)
        [self.ui.comboBoxDataSize.addItem(str(i)) for i in self.ser.BYTESIZES]
        self.ui.comboBoxDataSize.setCurrentText(self.dataSize)
        [self.ui.comboBoxParity.addItem(str(i)) for i in self.ser.PARITIES]
        self.ui.comboBoxParity.setCurrentText(self.parity)
        [self.ui.comboBoxStopBits.addItem(str(i)) for i in self.ser.STOPBITS]
        self.ui.comboBoxStopBits.setCurrentText(self.stopBits)
        [self.ui.comboBoxFlowControl.addItem(str(i)) for i in [True, False]]
        self.ui.comboBoxFlowControl.setCurrentText(self.flowControl)
        [self.ui.comboBoxCOMPorts.addItem(str(i)) for i in serial.tools.list_ports.comports()]
        self.ui.comboBoxCOMPorts.setCurrentIndex(0)

        self.ui.comboBoxBaudRate.currentTextChanged.connect(self.baudRateChanged)
        self.ui.comboBoxDataSize.currentTextChanged.connect(self.dataSizeChanged)
        self.ui.comboBoxStopBits.currentTextChanged.connect(self.stopBitsChanged)
        self.ui.comboBoxParity.currentTextChanged.connect(self.parityChanged)
        self.ui.comboBoxFlowControl.currentTextChanged.connect(self.flowControlChanged)
        self.ui.comboBoxCOMPorts.currentTextChanged.connect(self.comPortsChanged)
        self.ui.pushButtonStart.clicked.connect(self.start)
        
        self.ui.actionQuit.triggered.connect(self.quit)

        self.server.newConnection.connect(self.acceptConnection)

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "server.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        ui = loader.load(ui_file, self)
        ui_file.close()
        return ui

    @Slot()
    def baudRateChanged(self, text):
        self.baudRate = text
        return

    @Slot()
    def dataSizeChanged(self, text):
        self.dataSize = text
        return

    @Slot()
    def stopBitsChanged(self, text):
        self.stopBits = text
        return

    @Slot()
    def parityChanged(self, text):
        self.parity = text
        return

    @Slot()
    def flowControlChanged(self, text):
        self.flowControl = text
        return

    @Slot()
    def comPortsChanged(self, text):
        self.COMPorts = text
        return

    @Slot()
    def start(self):
        if self.ui.pushButtonStart.text() == "Start":
            self.ui.pushButtonStart.setText("Stop")
            address = self.ui.lineEditAddress.text()
            port = self.ui.lineEditPort.text()
            self.server.listen(QHostAddress(address), int(port))
            message = "Server waiting for messages <{}:{}>".format(address, int(port))
            self.ui.textEditDisplay.append(message)

            self.ser.baudrate = int(self.baudRate)
            self.ser.bytesize = int(self.dataSize)
            self.ser.parity = self.parity
            self.ser.stopbits = int(self.stopBits)
            if (self.flowControl == "True"):
                self.ser.set_input_flow_control()
                self.ser.set_output_flow_control()
            self.ser.port = self.COMPort
            self.ser.timeout = self.timeout
            self.ser.open()
        else:
            self.ui.pushButtonStart.setText("Start")
            self.server.close()
            self.socket.close()

            self.ser.close()
        return

    @Slot()
    def acceptConnection(self):
        self.socket = self.server.nextPendingConnection()
        self.socket.readyRead.connect(self.readMessage)
        return

    @Slot()
    def readMessage(self):
        buffer = self.socket.readAll()
        bytesRead = buffer.length()
        message = "Message: {} ({} bytes)".format(buffer, bytesRead)
        self.ui.textEditDisplay.append(message)
        self.ser.write(buffer)
        buffer = self.ser.readline()
        self.ui.textEditDisplay.append(buffer.decode("utf-8"))
        return

    @Slot()
    def quit(self):
        QApplication.quit()
        return


if __name__ == "__main__":

    app = QApplication([])

    window = MainWindow()

    sys.exit(app.exec_())
