import sys

from PySide6 import QtCore, QtGui, QtWidgets


if __name__ == "__main__":

    app = QtWidgets.QApplication([])

    label = QtWidgets.QLabel("Username")
    # label.setAlignment(QtCore.Qt.AlignCenter)
    # label.setStyleSheet("""
    #     background-color: #262626;
    #     color: #FFFFFF;
    #     font-family: Arial;
    #     font-size: 16px;    
    # """)

    label.show()

    with open("style.qss", 'r') as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec_())
