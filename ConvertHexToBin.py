from intelhex import IntelHex
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QFileInfo
from HexToBinApp.MainGUI import *


class MyWindow(QMainWindow, Ui_MainWindow):
    lastfiledir = ""

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

    def selecthexfile(self) -> None:
        file = QFileDialog.getOpenFileName(self, '选择Hex文件', '', 'Intel Hex files(*.hex , *.mcs)')
        qfileinfo : QFileInfo = QFileInfo(file[0])
        filename = qfileinfo.fileName()
        if filename[-3:].lower() == "hex":
            self.lastfiledir = qfileinfo.path()
            self.hexfilename.setText(filename)
            self.enableedit()
            self.statusbar.showMessage("打开文件成功", msecs=2000)

    def enableedit(self):
        if self.usedefaultname.isChecked():
            self.binfilename.setText(self.hexfilename.text()[0:-4] + ".bin")
        else:
            self.binfilename.setReadOnly(False)

    def generatebin(self):
        if self.hexfilename.text() != "" and self.binfilename.text() != "":
            hex = IntelHex(self.lastfiledir + "/" + self.hexfilename.text())
            hex.tobinfile(self.lastfiledir + "/" + self.binfilename.text())
            self.statusbar.showMessage("格式转换完毕", msecs=2000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
    pass
