import sys
from PyQt5 import QtWidgets
from inventaris import InventarisWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = InventarisWindow()
    window.show()
    sys.exit(app.exec_())