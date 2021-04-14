import sys

from PySide6 import QtCore, QtGui, QtWidgets

data = {
    "Project 01": ["01.py", "02.py"],
    "Project 02": ["01.py"],
    "Project 03": []
}


if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    
    tree = QtWidgets.QTreeWidget()
    tree.setColumnCount(2)
    tree.setHeaderLabels(["Name", "Type"])

    items = []
    for key, values in data.items():
        item = QtWidgets.QTreeWidgetItem([key])
        for value in values:
            ext = value.split('.')[-1].upper()
            child = QtWidgets.QTreeWidgetItem([value, ext])
            item.addChild(child)
        items.append(item)

    tree.insertTopLevelItems(0, items)

    tree.show()
    
    sys.exit(app.exec_())