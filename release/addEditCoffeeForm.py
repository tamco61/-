# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.save_btn = QtWidgets.QPushButton(Form)
        self.save_btn.setGeometry(QtCore.QRect(5, 6, 101, 31))
        self.save_btn.setObjectName("save_btn")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 351, 231))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.add_btn = QtWidgets.QPushButton(Form)
        self.add_btn.setGeometry(QtCore.QRect(110, 6, 101, 31))
        self.add_btn.setObjectName("add_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.save_btn.setText(_translate("Form", "сохранить"))
        self.add_btn.setText(_translate("Form", "добавить"))
