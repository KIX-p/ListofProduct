import sys

from PyQt6.QtWidgets import QDialog, QApplication, QTableWidgetItem, QMessageBox

from layout import Ui_Dialog


class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.add.clicked.connect(self.add)
        self.ui.delete_2.clicked.connect(self.delete)
        self.ui.save.clicked.connect(self.zapisz)
        self.show()

    def add(self):
        name = self.ui.nameofproduct.text()
        count = self.ui.countofproduct
        listofproducts = self.ui.listofproducts

        if name == "" or count == 0:
            QMessageBox.warning(self, "brak", "Uzupełnij pola")
        elif len(name) > 50:
            QMessageBox.warning(self, "dlugosc", "Tekst jest za długi")
        else:
            listofproducts.addItem(self.ui.nameofproduct.text())



    def delete(self):
        name = self.ui.nameofproduct.text()
        count = self.ui.countofproduct
        listofproducts = self.ui.listofproducts



    def zapisz(self):
        with open("lista.txt", "w") as i:
            for i in range(self.ui.listofproducts.count()):
                i.write(str(self.ui.listofproducts()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    window.setWindowTitle('Lista Zakupów')
    window.show()
    sys.exit(app.exec())
