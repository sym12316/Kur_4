
import sys 
import sqlite3 
import datetime
import configparser
import hashlib
from datetime import date
import mysql.connector

from getpass import getpass
from mysql.connector import connect, Error

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt

from UI import UI_LogWindow as LogWindow
from UI import UI_MainWindow as MainWindow

class MainWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        # self.showFullScreen()

        self.label_date.setText(datetime.datetime.today().strftime('%d.%m.%Y'))
        
        self.firstFilling()
        self.pushButtonUpdateTable.clicked.connect(self.whoseScheduleIsThis)

    def firstFilling(self):
            
        cursor.execute("SELECT Spec FROM Doc GROUP BY Spec;")

        self.doc_spec = cursor.fetchall()
        self.whatYouNeed = [0] + self.doc_spec
        self.whoseScheduleIsThis()

    def whoseScheduleIsThis(self):
        # cursor = connection.cursor()
        if self.whatYouNeed[0] == 0:

            self.docFIO = []
            for i in range(len(self.whatYouNeed)-1):

                request = """ SELECT Doc_FIO , Spec FROM Doc
                                WHERE Spec = %s
                                ORDER BY ID_Doc ASC"""

                into = self.whatYouNeed[i+1]
                
                global connection
                connection = connect(
                    host="localhost",
                    user="admin",
                    password="klinika",
                    database="asormo",
                )
                
                cursor = connection.cursor()
                print("!!!!!!!!!!")
                cursor.execute(request, into)
                docFioTmp = cursor.fetchall()
                print("SSSSSSSSSSSSSSSSs")
                # with connection.cursor() as cursor:
                #     cursor.execute(request, into)
                #     connection.commit()
                #     docFioTmp = cursor.fetchall()


                self.docFIO = self.docFIO + docFioTmp
                
            self.tableFillSpec()
            
        elif self.whatYouNeed[0] == 1:
            
            self.docFIO = self.whatYouNeed
            self.docFIO.pop(0)
            
            self.tableFillSpec()
            self.whatYouNeed = [1] + self.whatYouNeed
        else:
            self.firstFilling()

    def tableFillSpec(self):
        # self.enableWidget()
        self.tableWidget.clear()
        ourDate = self.label_date.text()
        cursor = connection.cursor()
        
        docFIO = self.docFIO
        self.tableWidget.setRowHeight(0, 30)
        self.tableWidget.setRowHeight(1, 30)

        for i in range(len(docFIO)):
            
            self.tableWidget.setColumnWidth(i, 200)

            self.tableWidget.setItem(0, i, QtWidgets.QTableWidgetItem(str(docFIO[i][1])))
            self.tableWidget.setItem(1, i, QtWidgets.QTableWidgetItem(str(docFIO[i][0])))
           
            # ↓ забиваем ячейки в столбце
            # ↓ запрос на выдачу ID приёмов
            request = """SELECT ID_appointment,Time_appointment,appointment_status,ID_Pat FROM Appointment
                            WHERE ID_Doc = (SELECT ID_Doc FROM Doc WHERE Doc_FIO = %s)
                            AND Day_appointment = %s
                            ORDER BY Time_appointment;"""
            into = (docFIO[i][0],"15.02.2024")
            cursor.execute(request, into)

            # ID_appointment,Time_appointment,appointment_status,ID_Pat # 
            #       0               1               2               3   # 
            CurrentData = cursor.fetchall()
            for j in range(len(CurrentData)):
                self.tableWidget.setRowHeight(j+2, 75)
                item = QTableWidgetItem()
                self.tableWidget.setRowHeight(j+2, 85)
 
 
                item.setStatusTip(str (CurrentData[j][0]))
                
                if len(CurrentData)+2 > self.tableWidget.rowCount():
                    self.tableWidget.setRowCount(len(CurrentData)+2)
                    
                Pat_ID = CurrentData[j][3]
                
                requets = """SELECT Pat_FIO, Phone_num, Pat_Card FROM Patient_card
                                WHERE ID_Pat = %s"""
                into = [Pat_ID]
                cursor.execute(requets, into)
                PatData = cursor.fetchall()



                if PatData[0][2] == 1:
                    item.setText('{0}\n+ {1}\n{2}'.format(CurrentData[j][1], PatData[0][0], PatData[0][1]))
                elif PatData[0][2] == 0:
                    item.setText('{0}\n- {1}\n{2}'.format(CurrentData[j][1], PatData[0][0], PatData[0][1]))
                
                
                appointmentStatusStr = CurrentData[j][2]
                # ↓ проверка состояния записи, окрашивание ячейки
                if appointmentStatusStr == 0:
                    item.setBackground(QtGui.QColor(255, 126, 147)) #красный    ЗАПИСИ НЕТ 0
                elif  appointmentStatusStr == 1:
                    item.setBackground(QtGui.QColor(163, 198, 192)) # Очень светлый зеленовато-синий запись не подтверждена
                elif  appointmentStatusStr == 2:
                    item.setBackground(QtGui.QColor(98, 111, 222))  # синий ПРИЁМ ЕСТЬ И ЭТО ТОЧНО запись подтверждена
                
                # ↓ Вставляем данные в таблицу
                self.tableWidget.setItem(j+2, i, item)


class LogWindow(QtWidgets.QMainWindow, LogWindow.Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self) 
        self.pushButton.clicked.connect(self.authorization)
    def authorization(self):


        try:
            with connect(
                host="localhost",


                user="admin",
                password="klinika",

                # user=self.lineEdit_username.text(),
                # password=self.lineEdit_password.text(),
                
                database="asormo",
            ) as connection:
                global cursor 
                cursor = connection.cursor()
                self.close()
                self.MainWindow = MainWindow()
                self.MainWindow.show()

        except Error as e:
            self.pushButton.setText('Неправильный логин или пароль')
            self.lineEdit_username.clear()
            self.lineEdit_password.clear()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = LogWindow()
    window.show()
    app.exec_()
   
if __name__ == '__main__':  
    main()