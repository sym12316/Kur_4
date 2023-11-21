import sys 
import sqlite3 
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import MainWindow_2 as MainWindow
from functools import partial
from PyQt5.QtCore import Qt
import datetime
from datetime import date
conn = sqlite3.connect(r'DB/SAR.DB')
cur = conn.cursor()
# data = ['table']



class MainWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        # self.showFullScreen()
        self.label_date.setText(datetime.datetime.today().strftime('%d.%m.%Y')) 
        print(self.label_date.text())
        # ↓ выбираем тип врача и ФИО
        cur.execute("SELECT Spec FROM 'Doc' ORDER BY ID_Doc ASC;")
        medSpec = cur.fetchall()
        cur.execute("SELECT Doc_FIO FROM 'Doc' ORDER BY ID_Doc ASC;")
        docFIO = cur.fetchall()
        # ↑ выбираем тип врача и ФИО

        # ↓ 
        # ↑ 

        # ↓ забиваем ячейки
        for i in range(len(docFIO)):
        
            # ↓ 
            medSpecStr = ''.join(medSpec[i])
            self.tableWidget.setItem(0, i, QtWidgets.QTableWidgetItem(medSpecStr))
            # ↑ 
            # ↓ 
            docFIOStr = ''.join(docFIO[i])
            self.tableWidget.setItem(1, i, QtWidgets.QTableWidgetItem(docFIOStr))
            # ↑ 

            
            
            # ↓ берём нашу дату
            ourDate = self.label_date.text()
            ourDate = '15.11.2023'
            # ↓ забиваем время
            time = ['9:00','9:30','10:00','10:30','11:00','11:30','12:00','12:30','13:00','13:30','14:00','14:30','15:00','15:30','16:00','16:30']
            
            # ↓ забиваем ячейки в столбце
            for j in range(len(time)):

                item = QTableWidgetItem()

                 # ↓ запрос на выдачу ID приёмов
                cur.execute("""SELECT ID_appointment FROM Appointment 
                WHERE Time_appointment = (?) 
                AND (ID_Doc = (SELECT ID_Doc FROM Doc WHERE Doc_FIO = (?))
                AND Day_appointment = (?));""",(time[j],docFIOStr,ourDate,))
                 # ↓ переформотируем tuple в int/str
                currentAppointmentId = cur.fetchall()
                currentAppointmentIdStr= int(''.join(map(str,currentAppointmentId[0])))
                
                 # ↓ запрос на выдачу ФИО по ID приёмов
                cur.execute("""SELECT Pat_FIO FROM Patient_card
                WHERE (ID_Pat = (SELECT ID_Pat FROM Appointment
                WHERE ID_appointment = (?)))""",(currentAppointmentIdStr,))
                patFio = cur.fetchall()
                # ↓ переформотируем tuple в int/str
                patFioStr = ''.join(patFio[0])
                
                 # ↓ Вставляем ФИО пациента в item
                item.setData(Qt.EditRole, patFioStr)

                 # ↓ запрос на выдачу статуса записи по ID приёмов
                cur.execute("""SELECT appointment_status FROM Appointment                      
                WHERE ID_appointment = (?)""",(currentAppointmentIdStr,))
                appointmentStatus = cur.fetchall()
                # ↓ переформотируем tuple в int/str
                appointmentStatusStr = int(''.join(map(str,appointmentStatus[0])))
                print (appointmentStatusStr)

                if appointmentStatusStr == 0:
                    item.setBackground(QtGui.QColor(255, 128, 128))
                elif  appointmentStatusStr == 1:
                    item.setBackground(QtGui.QColor(200, 200, 200))
                elif  appointmentStatusStr == 2:
                    item.setBackground(QtGui.QColor(98, 111, 222))
                print (j )
                self.tableWidget.setItem(j+2, i, item)

                # item.setBackground(QtGui.QColor(255, 128, 128))
                # item.setBackground(QtGui.QColor(200, 200, 200))









def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
    



if __name__ == '__main__':  
    main()