# This Python file uses the following encoding: utf-8
import sys
import os


from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import qDebug, QFile, Signal, Slot
from PySide6.QtUiTools import QUiLoader


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
        self.timeout = 2.0
        
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
        self.ui.pushButtonOpenPort.clicked.connect(self.open)
        self.ui.pushButtonSend.clicked.connect(self.send)
        self.ui.lineEditSend.returnPressed.connect(self.send)

        self.ui.actionQuit.triggered.connect(self.quit)

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        ui = loader.load(ui_file, self)
        ui_file.close()
        return ui

    @Slot()
    def baudRateChanged(self, text):
        self.baudRate = text
        qDebug(self.baudRate)
        return

    @Slot()
    def dataSizeChanged(self, text):
        self.dataSize = text
        qDebug(self.dataSize)
        return

    @Slot()
    def stopBitsChanged(self, text):
        self.stopBits = text
        qDebug(self.stopBits)
        return

    @Slot()
    def parityChanged(self, text):
        self.parity = text
        qDebug(self.parity)
        return

    @Slot()
    def flowControlChanged(self, text):
        self.flowControl = text
        qDebug(self.flowControl)
        return

    @Slot()
    def comPortsChanged(self, text):
        self.COMPorts = text
        qDebug(self.COMPort)
        return

    @Slot()
    def open(self):
        if not self.ser.is_open:
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
            qDebug("Opened")

            self.ui.pushButtonOpenPort.setText("Close")
        else:
            self.ser.close()
            qDebug("Closed")

            self.ui.pushButtonOpenPort.setText("Open")

        return

    @Slot()
    def send(self):
        if self.ser.is_open:
            data = "{}".format(self.ui.lineEditSend.text())
            bytesWritten = self.ser.write(data.encode("utf-8"))
            qDebug(str(bytesWritten))

            self.ui.textEditDisplay.append(data)

            data = self.ser.readline()
            qDebug(str(len(data)))

            self.ui.textEditDisplay.append(data.decode("utf-8"))

        return

    @Slot()
    def quit(self):
        QApplication.quit()
        return

if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
#    widget.show()
    sys.exit(app.exec_())
