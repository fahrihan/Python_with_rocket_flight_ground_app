# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acilis_ekran.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(612, 231)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 661, 61))
        self.label.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 20pt \"SWRomnt\";\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.yukleme_bar = QtWidgets.QProgressBar(Dialog)
        self.yukleme_bar.setGeometry(QtCore.QRect(100, 140, 421, 31))
        self.yukleme_bar.setStyleSheet("QProgressBar{\n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"    border-radius:10px;\n"
"    background-color: rgb(65, 65, 65);\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius:10px;\n"
"    \n"
"    background-color: rgb(40, 50, 55);\n"
"}")
        self.yukleme_bar.setProperty("value", 24)
        self.yukleme_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.yukleme_bar.setTextVisible(True)
        self.yukleme_bar.setOrientation(QtCore.Qt.Horizontal)
        self.yukleme_bar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.yukleme_bar.setObjectName("yukleme_bar")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(-10, -10, 711, 321))
        self.label_2.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 20, 91, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("border-image: url(:/lgo_png/magnetar-logo_png.png);")
        self.label_3.setText("")
        self.label_3.setScaledContents(False)
        self.label_3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(-20, 160, 661, 61))
        self.label_4.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 12pt \"SWRomnt\";\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_2.raise_()
        self.label.raise_()
        self.yukleme_bar.raise_()
        self.label_3.raise_()
        self.label_4.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Magnetar Roket Takımı"))
        self.label_4.setText(_translate("Dialog", "Yükleniyor"))
import logo_magnetar_rc
import logo_png_rc
