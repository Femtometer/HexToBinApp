# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainGUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(504, 147)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 30, 421, 33))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.hexfilename = QtWidgets.QLineEdit(self.layoutWidget)
        self.hexfilename.setReadOnly(True)
        self.hexfilename.setObjectName("hexfilename")
        self.horizontalLayout.addWidget(self.hexfilename)
        self.selectfile = QtWidgets.QPushButton(self.layoutWidget)
        self.selectfile.setObjectName("selectfile")
        self.horizontalLayout.addWidget(self.selectfile)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 70, 321, 28))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.usedefaultname = QtWidgets.QCheckBox(self.layoutWidget1)
        self.usedefaultname.setChecked(True)
        self.usedefaultname.setObjectName("usedefaultname")
        self.horizontalLayout_2.addWidget(self.usedefaultname)
        self.binfilename = QtWidgets.QLineEdit(self.layoutWidget1)
        self.binfilename.setReadOnly(True)
        self.binfilename.setObjectName("binfilename")
        self.horizontalLayout_2.addWidget(self.binfilename)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 70, 91, 32))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.selectfile.released.connect(MainWindow.selecthexfile)
        self.usedefaultname.stateChanged['int'].connect(MainWindow.enableedit)
        self.pushButton.released.connect(MainWindow.generatebin)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HexToBin工具"))
        self.selectfile.setText(_translate("MainWindow", "选择文件"))
        self.usedefaultname.setText(_translate("MainWindow", "原文件名保存"))
        self.pushButton.setText(_translate("MainWindow", "转换"))
