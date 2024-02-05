# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewAppoimentDayWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 400)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1001, 401))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 4, 3, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox_Doc_Spec = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.comboBox_Doc_Spec.sizePolicy().hasHeightForWidth())
        self.comboBox_Doc_Spec.setSizePolicy(sizePolicy)
        self.comboBox_Doc_Spec.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_Doc_Spec.setFont(font)
        self.comboBox_Doc_Spec.setObjectName("comboBox_Doc_Spec")
        self.verticalLayout_2.addWidget(self.comboBox_Doc_Spec)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.comboBox_Doc_Fio = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_Doc_Fio.setMinimumSize(QtCore.QSize(200, 50))
        self.comboBox_Doc_Fio.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_Doc_Fio.setFont(font)
        self.comboBox_Doc_Fio.setObjectName("comboBox_Doc_Fio")
        self.verticalLayout_2.addWidget(self.comboBox_Doc_Fio)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_Doc_Data = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_Doc_Data.setMinimumSize(QtCore.QSize(220, 50))
        self.label_Doc_Data.setMaximumSize(QtCore.QSize(220, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_Doc_Data.setFont(font)
        self.label_Doc_Data.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Doc_Data.setObjectName("label_Doc_Data")
        self.gridLayout_3.addWidget(self.label_Doc_Data, 0, 0, 1, 1)
        self.textEdit_Doc_Date = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.textEdit_Doc_Date.setMinimumSize(QtCore.QSize(320, 50))
        self.textEdit_Doc_Date.setMaximumSize(QtCore.QSize(320, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.textEdit_Doc_Date.setFont(font)
        self.textEdit_Doc_Date.setObjectName("textEdit_Doc_Date")
        self.gridLayout_3.addWidget(self.textEdit_Doc_Date, 1, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(270, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem5, 0, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem6, 2, 3, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.spinBox_Time_Num_Step = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox_Time_Num_Step.setMinimumSize(QtCore.QSize(160, 50))
        self.spinBox_Time_Num_Step.setMaximumSize(QtCore.QSize(160, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.spinBox_Time_Num_Step.setFont(font)
        self.spinBox_Time_Num_Step.setObjectName("spinBox_Time_Num_Step")
        self.gridLayout_2.addWidget(self.spinBox_Time_Num_Step, 1, 6, 1, 1)
        self.label_Doc_Num_Step = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_Doc_Num_Step.setMinimumSize(QtCore.QSize(160, 50))
        self.label_Doc_Num_Step.setMaximumSize(QtCore.QSize(160, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_Doc_Num_Step.setFont(font)
        self.label_Doc_Num_Step.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Doc_Num_Step.setObjectName("label_Doc_Num_Step")
        self.gridLayout_2.addWidget(self.label_Doc_Num_Step, 0, 6, 1, 1)
        self.label_Doc_Time = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_Doc_Time.setMinimumSize(QtCore.QSize(160, 50))
        self.label_Doc_Time.setMaximumSize(QtCore.QSize(160, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_Doc_Time.setFont(font)
        self.label_Doc_Time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Doc_Time.setObjectName("label_Doc_Time")
        self.gridLayout_2.addWidget(self.label_Doc_Time, 0, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 1, 3, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 1, 7, 1, 1)
        self.label_Doc_Step = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_Doc_Step.setMinimumSize(QtCore.QSize(160, 50))
        self.label_Doc_Step.setMaximumSize(QtCore.QSize(160, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_Doc_Step.setFont(font)
        self.label_Doc_Step.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Doc_Step.setObjectName("label_Doc_Step")
        self.gridLayout_2.addWidget(self.label_Doc_Step, 0, 4, 1, 1)
        self.pushButton_Accept_New_Day = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Accept_New_Day.setEnabled(True)
        self.pushButton_Accept_New_Day.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_Accept_New_Day.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_Accept_New_Day.setFont(font)
        self.pushButton_Accept_New_Day.setObjectName("pushButton_Accept_New_Day")
        self.gridLayout_2.addWidget(self.pushButton_Accept_New_Day, 1, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 1, 1, 1, 1)
        self.pushButton_Help = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Help.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_Help.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_Help.setFont(font)
        self.pushButton_Help.setObjectName("pushButton_Help")
        self.gridLayout_2.addWidget(self.pushButton_Help, 1, 8, 1, 1)
        self.timeEdit = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.timeEdit.setMinimumSize(QtCore.QSize(160, 50))
        self.timeEdit.setMaximumSize(QtCore.QSize(160, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.timeEdit.setFont(font)
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout_2.addWidget(self.timeEdit, 1, 2, 1, 1)
        self.spinBox_Time_Step = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox_Time_Step.setMinimumSize(QtCore.QSize(160, 50))
        self.spinBox_Time_Step.setMaximumSize(QtCore.QSize(160, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.spinBox_Time_Step.setFont(font)
        self.spinBox_Time_Step.setObjectName("spinBox_Time_Step")
        self.gridLayout_2.addWidget(self.spinBox_Time_Step, 1, 4, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem10, 1, 5, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 3, 3, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_Doc_Data.setText(_translate("Form", "Дни приёма"))
        self.label_Doc_Num_Step.setText(_translate("Form", "Количество шагов"))
        self.label_Doc_Time.setText(_translate("Form", "Время записи"))
        self.label_Doc_Step.setText(_translate("Form", "Шаг записи"))
        self.pushButton_Accept_New_Day.setText(_translate("Form", "Добавить запись"))
        self.pushButton_Help.setText(_translate("Form", "?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())