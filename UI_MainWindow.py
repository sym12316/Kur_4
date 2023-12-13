from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1174, 694)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(2000, 2000))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(170, 10, 822, 671))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayoutAll = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayoutAll.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutAll.setObjectName("gridLayoutAll")
        self.tableWidget = QtWidgets.QTableWidget(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMaximumSize(QtCore.QSize(2000, 2000))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setRowCount(18)
        self.tableWidget.setColumnCount(20)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        self.gridLayoutAll.addWidget(self.tableWidget, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayoutAll.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayoutDateButton = QtWidgets.QGridLayout()
        self.gridLayoutDateButton.setObjectName("gridLayoutDateButton")
        self.label_date = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_date.setObjectName("label_date")
        self.gridLayoutDateButton.addWidget(self.label_date, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayoutDateButton.addItem(spacerItem1, 1, 4, 1, 1)
        self.pushButton_right = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_right.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_right.setMaximumSize(QtCore.QSize(100, 50))
        self.pushButton_right.setObjectName("pushButton_right")
        self.gridLayoutDateButton.addWidget(self.pushButton_right, 1, 3, 1, 1)
        self.pushButton_left = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_left.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_left.setMaximumSize(QtCore.QSize(100, 50))
        self.pushButton_left.setObjectName("pushButton_left")
        self.gridLayoutDateButton.addWidget(self.pushButton_left, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayoutDateButton.addItem(spacerItem2, 1, 0, 1, 1)
        self.gridLayoutAll.addLayout(self.gridLayoutDateButton, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayoutAll.addItem(spacerItem3, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonNewDoc = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButtonNewDoc.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButtonNewDoc.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButtonNewDoc.setObjectName("pushButtonNewDoc")
        self.horizontalLayout.addWidget(self.pushButtonNewDoc)
        self.pushButtonUpdateRes = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButtonUpdateRes.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButtonUpdateRes.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButtonUpdateRes.setObjectName("pushButtonUpdateRes")
        self.horizontalLayout.addWidget(self.pushButtonUpdateRes)
        self.pushButtonNewRes = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButtonNewRes.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButtonNewRes.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButtonNewRes.setObjectName("pushButtonNewRes")
        self.horizontalLayout.addWidget(self.pushButtonNewRes)
        self.pushButtonUpdateTable = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButtonUpdateTable.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButtonUpdateTable.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButtonUpdateTable.setObjectName("pushButtonUpdateTable")
        self.horizontalLayout.addWidget(self.pushButtonUpdateTable)
        self.gridLayoutAll.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.gridLayoutWidget_2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tableWidget.setVerticalHeaderLabels(['','','9:00','9:30','10:00','10:30','11:00','11:30','12:00','12:30','13:00','13:30','14:00','14:30','15:00','15:30','16:00','16:30'])
        self.tableWidget.setHorizontalHeaderLabels(['V1','V2','V3','V4','V5']) 
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # __sortingEnabled = self.tableWidget.isSortingEnabled()
        # self.tableWidget.setSortingEnabled(False)
        # item = self.tableWidget.item(1, 0)
        # item.setText(_translate("MainWindow", "asdasdasd"))
        # self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_date.setText(_translate("MainWindow", "TextLabel"))

        self.pushButtonUpdateTable.setText(_translate("MainWindow", "Обновить таблицу"))
        self.pushButtonNewDoc.setText(_translate("MainWindow", "Добавить врача"))
        self.pushButtonUpdateRes.setText(_translate("MainWindow", "Обновить рассписание врача"))
        self.pushButtonNewRes.setText(_translate("MainWindow", "Добавить запись"))
        
        self.pushButton_right.setText(_translate("MainWindow", "->>"))
        self.pushButton_left.setText(_translate("MainWindow", "<<-"))

        # ///1 - 2 - 3 -0
        #   1 - добавить врача  pushButton_4 ->  pushButtonNewDoc
        #   2 - Обновить рассписание врача  pushButton_3 -> pushButtonUpdateRes
        #   3 - Добавить запись pushButton_2 -> pushButtonNewRes
        #   4 - Обновить таблицу  pushButton -> pushButtonUpdateTable