# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_DocFilther.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1024, 600)
        Dialog.setMinimumSize(QtCore.QSize(1024, 600))
        Dialog.setMaximumSize(QtCore.QSize(1024, 600))
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 1001, 591))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        self.verticalLayoutButton = QtWidgets.QVBoxLayout()
        self.verticalLayoutButton.setObjectName("verticalLayoutButton")
        self.pushButtonChangeFilter = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButtonChangeFilter.setMinimumSize(QtCore.QSize(200, 100))
        self.pushButtonChangeFilter.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButtonChangeFilter.setFont(font)
        self.pushButtonChangeFilter.setObjectName("pushButtonChangeFilter")
        self.verticalLayoutButton.addWidget(self.pushButtonChangeFilter)
        self.pushButtonSelect = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButtonSelect.setMinimumSize(QtCore.QSize(200, 100))
        self.pushButtonSelect.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButtonSelect.setFont(font)
        self.pushButtonSelect.setObjectName("pushButtonSelect")
        self.verticalLayoutButton.addWidget(self.pushButtonSelect)
        self.pushButtonDeselect = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButtonDeselect.setMinimumSize(QtCore.QSize(200, 100))
        self.pushButtonDeselect.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButtonDeselect.setFont(font)
        self.pushButtonDeselect.setObjectName("pushButtonDeselect")
        self.verticalLayoutButton.addWidget(self.pushButtonDeselect)
        self.pushButtonApply = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButtonApply.setMinimumSize(QtCore.QSize(200, 100))
        self.pushButtonApply.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButtonApply.setFont(font)
        self.pushButtonApply.setObjectName("pushButtonApply")
        self.verticalLayoutButton.addWidget(self.pushButtonApply)
        self.gridLayout.addLayout(self.verticalLayoutButton, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 3, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        # Dialog.setCentralWidget(self.gridLayoutWidget)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Поиск врачей"))
        self.pushButtonChangeFilter.setText(_translate("Dialog", "Перейти в поиск \n по специальности"))
        self.pushButtonSelect.setText(_translate("Dialog", "Выбрать "))
        self.pushButtonDeselect.setText(_translate("Dialog", "Убрать врача"))
        self.pushButtonApply.setText(_translate("Dialog", "Применить поиск"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
