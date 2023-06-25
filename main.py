import vobject
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtWidgets import  QFileDialog
import sys
from pyqt5_plugins.examplebuttonplugin import QtGui


class Form1(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form1, self).__init__()
        uic.loadUi('UI/firstactivity.ui', self)
        self.Next.clicked.connect(self.next)
        self.setWindowTitle('VCF парсинг')
        self.setWindowIcon(QtGui.QIcon('icon.png'))

    def next(self):
        self.switch_window.emit('1>2')






class Form2(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form2, self).__init__()
        uic.loadUi('UI/secondactivity.ui', self)
        self.setWindowTitle('VCF парсинг')
        self.Back.clicked.connect(self.back)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.Open.clicked.connect(self.parseVCF)

    def back(self):
        self.switch_window.emit('1<2')

    def parseVCF(self):

            vcf_file = QFileDialog.getOpenFileName(self, "Выберите файл VCF")[0]
            if vcf_file:
                try:
                    with open(vcf_file, 'r') as file:
                        vcard = vobject.readOne(file)
                        self.nameLabel.setText(vcard.fn.value)
                        self.emailLabel.setText(vcard.email.value)
                        self.phoneLabel.setText(vcard.tel.value)
                except FileNotFoundError:
                    self.nameLabel.setText("Файл не найден")
                    self.emailLabel.setText("")
                    self.phoneLabel.setText("")





def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Form1()
    window.show()
    sys.exit(app.exec_())


class Controller:
    def __init__(self):
        pass

    def select_forms(self, text):
        if text == '1':
            self.form1 = Form1()
            self.form1.switch_window.connect(self.select_forms)
            self.form1.show()
        if text == '1>2':
            self.form2 = Form2()
            self.form2.switch_window.connect(self.select_forms)
            self.form2.show()
            self.form1.close()
        if text == '1<2':
            self.form1 = Form1()
            self.form1.switch_window.connect(self.select_forms)
            self.form1.show()
            self.form2.close()




def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.select_forms("1")
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()