# Form implementation generated from reading ui file 'password_generate.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_PasswordGenerate(object):
    def setupUi(self, PasswordGenerate):
        PasswordGenerate.setObjectName("PasswordGenerate")
        PasswordGenerate.resize(404, 257)
        self.pushButton = QtWidgets.QPushButton(parent=PasswordGenerate)
        self.pushButton.setGeometry(QtCore.QRect(0, 120, 401, 71))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(28)
        self.pushButton.setFont(font)
        self.pushButton.setText("生成一个新的密码")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_result = QtWidgets.QLineEdit(parent=PasswordGenerate)
        self.lineEdit_result.setGeometry(QtCore.QRect(0, 200, 401, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(28)
        self.lineEdit_result.setFont(font)
        self.lineEdit_result.setObjectName("lineEdit_result")
        self.checkBox_upper = QtWidgets.QCheckBox(parent=PasswordGenerate)
        self.checkBox_upper.setGeometry(QtCore.QRect(30, 80, 79, 20))
        self.checkBox_upper.setObjectName("checkBox_upper")
        self.checkBox_lower = QtWidgets.QCheckBox(parent=PasswordGenerate)
        self.checkBox_lower.setGeometry(QtCore.QRect(120, 80, 79, 20))
        self.checkBox_lower.setObjectName("checkBox_lower")
        self.checkBox_number = QtWidgets.QCheckBox(parent=PasswordGenerate)
        self.checkBox_number.setGeometry(QtCore.QRect(210, 80, 79, 20))
        self.checkBox_number.setObjectName("checkBox_number")
        self.checkBox_puc = QtWidgets.QCheckBox(parent=PasswordGenerate)
        self.checkBox_puc.setGeometry(QtCore.QRect(270, 80, 79, 20))
        font = QtGui.QFont()
        font.setBold(False)
        self.checkBox_puc.setFont(font)
        self.checkBox_puc.setObjectName("checkBox_puc")
        self.label = QtWidgets.QLabel(parent=PasswordGenerate)
        self.label.setGeometry(QtCore.QRect(10, 15, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_site = QtWidgets.QLineEdit(parent=PasswordGenerate)
        self.lineEdit_site.setGeometry(QtCore.QRect(140, 10, 251, 41))
        self.lineEdit_site.setObjectName("lineEdit_site")

        self.retranslateUi(PasswordGenerate)
        QtCore.QMetaObject.connectSlotsByName(PasswordGenerate)

    def retranslateUi(self, PasswordGenerate):
        _translate = QtCore.QCoreApplication.translate
        PasswordGenerate.setWindowTitle(_translate("PasswordGenerate", "密码生成小程序"))
        self.checkBox_upper.setText(_translate("PasswordGenerate", "大写字母"))
        self.checkBox_lower.setText(_translate("PasswordGenerate", "小写字母"))
        self.checkBox_number.setText(_translate("PasswordGenerate", "数字"))
        self.checkBox_puc.setText(_translate("PasswordGenerate", "标点符号"))
        self.label.setText(_translate("PasswordGenerate", "请输入网站"))
