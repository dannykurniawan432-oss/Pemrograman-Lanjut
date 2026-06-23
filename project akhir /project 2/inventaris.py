import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QInputDialog
from ui_inventaris import Ui_MainWindow


class InventarisWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
       
        self.ui.btnSimpan.clicked.connect(self.simpan_barang)
        self.ui.btnReset.clicked.connect(self.reset_form)
        self.ui.btnHapus.clicked.connect(self.hapus_barang)
        self.ui.btnStokMasuk.clicked.connect(self.stok_masuk)
        self.ui.btnStokKeluar.clicked.connect(self.stok_keluar)
        
        self.ui.inputCari.textChanged.connect(self.search_data)
        self.ui.comboFilter.currentIndexChanged.connect(self.search_data)

        self.load_table()

    
    def simpan_barang(self):
        nama = self.ui.inputNama.text().strip()
        kategori = self.ui.comboKategori.currentText()
        stok = self.ui.spinStok.value()
        satuan = self.ui.comboSatuan.currentText()
        harga_text = self.ui.inputHarga.text().strip()

        if not nama or not harga_text:
            QMessageBox.warning(self, "Error", "Nama dan harga wajib diisi")
            return

        try:
            harga = int(harga_text)
        except ValueError:
            QMessageBox.warning(self, "Error", "Harga harus angka")
            return

        barang = {
            "kode": f"BRG{self.kode_counter:04d}",
            "nama": nama,
            "kategori": kategori,
            "stok": stok,
            "satuan": satuan,
            "harga": harga
        }

        self.data.append(barang)
        self.kode_counter += 1

        self.reset_form()
        self.load_table()

   
    def reset_form(self):
        self.ui.inputNama.clear()
        self.ui.spinStok.setValue(0)
        self.ui.inputHarga.clear()
        self.ui.comboKategori.setCurrentIndex(0)
        self.ui.comboSatuan.setCurrentIndex(0)

   
    def load_table(self, filtered=None):
        data = filtered if filtered is not None else self.data

        self.ui.tableInventaris.setRowCount(len(data))

        total_nilai = 0
        stok_menipis = 0

        for row, item in enumerate(data):
            self.ui.tableInventaris.setItem(row, 0, QTableWidgetItem(item["kode"]))
            self.ui.tableInventaris.setItem(row, 1, QTableWidgetItem(item["nama"]))
            self.ui.tableInventaris.setItem(row, 2, QTableWidgetItem(item["kategori"]))
            self.ui.tableInventaris.setItem(row, 3, QTableWidgetItem(str(item["stok"])))
            self.ui.tableInventaris.setItem(row, 4, QTableWidgetItem(item["satuan"]))
            self.ui.tableInventaris.setItem(row, 5, QTableWidgetItem(str(item["harga"])))

            total_nilai += item["stok"] * item["harga"]

            if item["stok"] <= 2:
                stok_menipis += 1

        
        self.ui.lblStatTotalValue.setText(str(len(self.data)))
        self.ui.lblStatHabisValue.setText(str(stok_menipis))
        self.ui.lblStatusInfo.setText(f"Menampilkan {len(data)} barang")
        self.ui.lblTotalNilai.setText(f"Total nilai stok: Rp {total_nilai:,}")

    def hapus_barang(self):
        selected = self.ui.tableInventaris.currentRow()
        if selected < 0:
            return

        kode = self.ui.tableInventaris.item(selected, 0).text()

        self.data = [d for d in self.data if d["kode"] != kode]
        self.load_table()

    
    def search_data(self):
        keyword = self.ui.inputCari.text().lower()
        filter_kat = self.ui.comboFilter.currentText()

        def match(item):
            if filter_kat != "Semua" and item["kategori"] != filter_kat:
                return False
            if keyword and keyword not in item["nama"].lower():
                return False
            return True

        filtered = list(filter(match, self.data))
        self.load_table(filtered)

    
    def stok_masuk(self):
        self.update_stok(0)

    
    def stok_keluar(self):
        self.update_stok(-1)

    def update_stok(self, mode):
        selected = self.ui.tableInventaris.currentRow()
        if selected < 0:
            return

        kode = self.ui.tableInventaris.item(selected, 0).text()
        item = next((d for d in self.data if d["kode"] == kode), None)

        if not item:
            return

        value, ok = QInputDialog.getInt(self, "Update Stok", "Jumlah:")
        if not ok:
            return

        if mode == 0:
            item["stok"] += value
        else:
            item["stok"] = max(0, item["stok"] - value)

        self.load_table()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = InventarisWindow()
    window.show()
    sys.exit(app.exec_())
