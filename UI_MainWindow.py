# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestWindow_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1064, 674)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(2000, 2000))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(58, 0, 991, 661))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayoutAll = QtWidgets.QGridLayout()
        self.gridLayoutAll.setObjectName("gridLayoutAll")
        spacerItem1 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayoutAll.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayoutAll.addItem(spacerItem2, 4, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.tableWidget.setMaximumSize(QtCore.QSize(2000, 2000))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(20)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        self.gridLayoutAll.addWidget(self.tableWidget, 3, 0, 1, 1)
        self.gridLayoutDateButton = QtWidgets.QGridLayout()
        self.gridLayoutDateButton.setObjectName("gridLayoutDateButton")
        self.pushButton_left_week = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_left_week.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_left_week.setMaximumSize(QtCore.QSize(100, 50))
        self.pushButton_left_week.setObjectName("pushButton_left_week")
        self.gridLayoutDateButton.addWidget(self.pushButton_left_week, 1, 1, 1, 1)
        self.pushButton_left_day = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_left_day.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_left_day.setMaximumSize(QtCore.QSize(100, 50))
        self.pushButton_left_day.setObjectName("pushButton_left_day")
        self.gridLayoutDateButton.addWidget(self.pushButton_left_day, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayoutDateButton.addItem(spacerItem3, 1, 0, 1, 1)
        self.pushButton_right_week = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_right_week.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_right_week.setMaximumSize(QtCore.QSize(100, 50))
        self.pushButton_right_week.setObjectName("pushButton_right_week")
        self.gridLayoutDateButton.addWidget(self.pushButton_right_week, 1, 6, 1, 1)
        self.pushButton_right_day = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_right_day.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_right_day.setMaximumSize(QtCore.QSize(100, 50))
        self.pushButton_right_day.setObjectName("pushButton_right_day")
        self.gridLayoutDateButton.addWidget(self.pushButton_right_day, 1, 5, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayoutDateButton.addItem(spacerItem4, 1, 7, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_date = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_date.setMinimumSize(QtCore.QSize(180, 50))
        self.label_date.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        self.label_date.setFont(font)
        self.label_date.setAlignment(QtCore.Qt.AlignCenter)
        self.label_date.setObjectName("label_date")
        self.verticalLayout.addWidget(self.label_date)
        self.label_weekday = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_weekday.setFont(font)
        self.label_weekday.setAlignment(QtCore.Qt.AlignCenter)
        self.label_weekday.setObjectName("label_weekday")
        self.verticalLayout.addWidget(self.label_weekday)
        self.gridLayoutDateButton.addLayout(self.verticalLayout, 1, 4, 1, 1)
        self.gridLayoutAll.addLayout(self.gridLayoutDateButton, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayoutAll.addItem(spacerItem5, 2, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButtonUpdateTable = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonUpdateTable.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButtonUpdateTable.setMaximumSize(QtCore.QSize(250, 50))
        self.pushButtonUpdateTable.setObjectName("pushButtonUpdateTable")
        self.verticalLayout_5.addWidget(self.pushButtonUpdateTable)
        self.pushButtonNewRes = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonNewRes.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButtonNewRes.setMaximumSize(QtCore.QSize(250, 50))
        self.pushButtonNewRes.setObjectName("pushButtonNewRes")
        self.verticalLayout_5.addWidget(self.pushButtonNewRes)
        self.pushButtonUpdateRes = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonUpdateRes.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButtonUpdateRes.setMaximumSize(QtCore.QSize(250, 50))
        self.pushButtonUpdateRes.setObjectName("pushButtonUpdateRes")
        self.verticalLayout_5.addWidget(self.pushButtonUpdateRes)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_change_appointment_green = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_change_appointment_green.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_change_appointment_green.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_change_appointment_green.setObjectName("pushButton_change_appointment_green")
        self.horizontalLayout.addWidget(self.pushButton_change_appointment_green)
        self.pushButton_change_appointment_blue = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_change_appointment_blue.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_change_appointment_blue.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_change_appointment_blue.setObjectName("pushButton_change_appointment_blue")
        self.horizontalLayout.addWidget(self.pushButton_change_appointment_blue)
        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.pushButton_Edit_Appointment = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Edit_Appointment.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButton_Edit_Appointment.setMaximumSize(QtCore.QSize(250, 50))
        self.pushButton_Edit_Appointment.setObjectName("pushButton_Edit_Appointment")
        self.verticalLayout_5.addWidget(self.pushButton_Edit_Appointment)

        self.pushButton_Search = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Search.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButton_Search.setMaximumSize(QtCore.QSize(250, 50))
        self.pushButton_Search.setObjectName("pushButton_Search")
        self.verticalLayout_5.addWidget(self.pushButton_Search)

        self.pushButtonNewDoc = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonNewDoc.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButtonNewDoc.setMaximumSize(QtCore.QSize(250, 50))
        self.pushButtonNewDoc.setObjectName("pushButtonNewDoc")
        self.verticalLayout_5.addWidget(self.pushButtonNewDoc)
        self.gridLayoutAll.addLayout(self.verticalLayout_5, 3, 1, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayoutAll)
        spacerItem6 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setCentralWidget(self.horizontalLayoutWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow_1"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_left_week.setText(_translate("MainWindow", "Неделя назад"))
        self.pushButton_left_day.setText(_translate("MainWindow", "День назад"))
        self.pushButton_right_week.setText(_translate("MainWindow", "Неделя вперёд"))
        self.pushButton_right_day.setText(_translate("MainWindow", "День вперёд"))
        self.label_date.setText(_translate("MainWindow", "12.10.2023"))
        self.label_weekday.setText(_translate("MainWindow", "Воскресенье"))
        self.pushButtonUpdateTable.setText(_translate("MainWindow", "Обновить таблицу"))
        self.pushButtonNewRes.setText(_translate("MainWindow", "Поиск свободной записи"))
        self.pushButtonUpdateRes.setText(_translate("MainWindow", "Записать пациента в пустую ячейку"))
        self.pushButton_change_appointment_green.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_change_appointment_blue.setText(_translate("MainWindow", "PushButton"))

        self.pushButton_Search.setText(_translate("MainWindow", "pushButton_Search"))

        self.pushButton_Edit_Appointment.setText(_translate("MainWindow", "Редактирование/удаление записи"))
        self.pushButtonNewDoc.setText(_translate("MainWindow", "Изменение расписания"))


        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
