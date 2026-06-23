import sys
from datetime import datetime
from PyQt5 import QtWidgets
from notped1 import Ui_NotepadWindow


class Notepad(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_NotepadWindow()
        self.ui.setupUi(self)

        self.dataCatatan = {}
        self.currentItem = None

        self.btnSave = QtWidgets.QPushButton("Simpan")
        self.btnDelete = QtWidgets.QPushButton("Hapus")
        self.ui.buttonLayout.addWidget(self.btnSave)
        self.ui.buttonLayout.addWidget(self.btnDelete)

        self.btnSave.clicked.connect(self.simpanCatatan)
        self.btnDelete.clicked.connect(self.hapusCatatan)

        self.ui.listWidget.itemClicked.connect(self.tampilCatatan)

        self.ui.actionBaru.triggered.connect(self.baru)
        self.ui.actionBukaFile.triggered.connect(self.bukaCatatan)
        self.ui.actionSimpanFile.triggered.connect(self.simpanKeFile)
        self.ui.actionKeluar.triggered.connect(self.konfirmasiKeluar)
        self.ui.actionUndo.triggered.connect(self.ui.textEditor.undo)
        self.ui.actionRedo.triggered.connect(self.ui.textEditor.redo)

    def simpanCatatan(self):
        teks = self.ui.textEditor.toPlainText()
        if teks.strip() == "":
            return

        judul = teks.split("\n")[0][:15]
        hari_indonesia = {
            "Monday": "Senin", "Tuesday": "Selasa", "Wednesday": "Rabu",
            "Thursday": "Kamis", "Friday": "Jumat", "Saturday": "Sabtu", "Sunday": "Minggu"
        }
        sekarang = datetime.now()
        hari = hari_indonesia[sekarang.strftime("%A")]
        tanggal = sekarang.strftime("%d-%m-%Y %H:%M")
        nama = f"{judul} | {hari}, {tanggal}"

        if self.currentItem:
            nama_lama = self.currentItem.text()
            if nama_lama in self.dataCatatan:
                del self.dataCatatan[nama_lama]
            self.currentItem.setText(nama)
        else:
            self.ui.listWidget.addItem(nama)

        self.dataCatatan[nama] = teks
        self.currentItem = None
        self.ui.textEditor.clear()

    def tampilCatatan(self, item):
        self.currentItem = item
        judul = item.text()
        if judul in self.dataCatatan:
            self.ui.textEditor.setPlainText(self.dataCatatan[judul])

    def hapusCatatan(self):
        item = self.ui.listWidget.currentItem()
        if item:
            reply = QtWidgets.QMessageBox.question(
                self, "Konfirmasi Hapus", "Yakin mau menghapus catatan ini?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No
            )
            if reply == QtWidgets.QMessageBox.Yes:
                nama = item.text()
                row = self.ui.listWidget.row(item)
                self.ui.listWidget.takeItem(row)
                if nama in self.dataCatatan:
                    del self.dataCatatan[nama]
                self.ui.textEditor.clear()
                self.currentItem = None
                self.ui.listWidget.clearSelection()
                self.ui.listWidget.setCurrentItem(None)
        else:
            QtWidgets.QMessageBox.warning(
                self, "Hapus Catatan", "Pilih catatan dari daftar untuk dihapus."
            )

    def bukaCatatan(self):
        faisal, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Buka Catatan", "", "Text Files (*.txt);;All Files (*)"
        )
        if faisal:
            with open(faisal, "r", encoding="utf-8") as f:
                self.ui.textEditor.setPlainText(f.read())

    def simpanKeFile(self):
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Simpan Catatan", "", "Text Files (*.txt);;All Files (*)"
        )
        if fileName:
            teks = self.ui.textEditor.toPlainText()
            with open(fileName, "w", encoding="utf-8") as f:
                f.write(teks)

    def baru(self):
        self.ui.textEditor.clear()
        self.ui.listWidget.clearSelection()
        self.currentItem = None

    def konfirmasiKeluar(self):
        reply = QtWidgets.QMessageBox.question(
            self, "Konfirmasi Keluar", "Anda ingin keluar?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No
        )
        if reply == QtWidgets.QMessageBox.Yes:
            self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Notepad()
    window.show()
    sys.exit(app.exec_())
