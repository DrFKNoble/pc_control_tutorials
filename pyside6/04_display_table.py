import sys

from PySide6 import QtCore, QtGui, QtWidgets

colors = [
    ("Red", "#FF0000"),
    ("Green", "#00FF00"),
    ("Blue", "#0000FF"),
]

def cvtColor(code):

    code = code.replace('#', '')
    
    rgb = tuple(int(code[i:i+2], 16) for i in (0, 2, 4))

    return QtGui.QColor.fromRgb(rgb[0], rgb[1], rgb[2])



if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    
    table = QtWidgets.QTableWidget()
    table.setRowCount(len(colors))
    table.setColumnCount(len(colors[0]) + 1)
    table.setHorizontalHeaderLabels(["Name", "Hex Code", "Color"])
    
    for i, (name, code) in enumerate(colors):
        item_name = QtWidgets.QTableWidgetItem(name)
        item_code = QtWidgets.QTableWidgetItem(code)
        item_color = QtWidgets.QTableWidgetItem()
        item_color.setBackground(cvtColor(code))
        table.setItem(i, 0, item_name)
        table.setItem(i, 1, item_code)
        table.setItem(i, 2, item_color)

    table.show()
    
    sys.exit(app.exec_())