# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DelDocOrDay.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(240, 360)
        Form.setMinimumSize(QtCore.QSize(240, 360))
        Form.setMaximumSize(QtCore.QSize(240, 360))
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 241, 361))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.label_Down = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Down.setMinimumSize(QtCore.QSize(200, 50))
        self.label_Down.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_Down.setFont(font)
        self.label_Down.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Down.setObjectName("label_Down")
        self.gridLayout.addWidget(self.label_Down, 2, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setMinimumSize(QtCore.QSize(200, 50))
        self.textEdit.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textEdit.setLineWidth(1)
        self.textEdit.setMidLineWidth(0)
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 4, 0, 1, 1)
        self.pushButton_Accept = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_Accept.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_Accept.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_Accept.setFont(font)
        self.pushButton_Accept.setObjectName("pushButton_Accept")
        self.gridLayout.addWidget(self.pushButton_Accept, 6, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setMinimumSize(QtCore.QSize(200, 50))
        self.comboBox.setMaximumSize(QtCore.QSize(200, 50))
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        self.label_Up = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Up.setMinimumSize(QtCore.QSize(200, 50))
        self.label_Up.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_Up.setFont(font)
        self.label_Up.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Up.setObjectName("label_Up")
        self.gridLayout.addWidget(self.label_Up, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Удаление записи"))
        self.label_Down.setText(_translate("Form", "Введите ФИО врача"))
        self.pushButton_Accept.setText(_translate("Form", "Удалить запись"))
        self.label_Up.setText(_translate("Form", "Введите специальность \n"
"врача"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())