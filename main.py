import sys 
import sqlite3 
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import MainWindow_2 as MainWindow
from functools import partial
from PyQt5.QtCore import Qt

conn = sqlite3.connect(r'DB/SAR.DB')
cur = conn.cursor()
# data = ['table']



class MainWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        self.showFullScreen()

        cur.execute("SELECT Spec FROM 'Doc' ORDER BY ID_Doc ASC;")
        medSpec = cur.fetchall()
        cur.execute("SELECT Doc_FIO FROM 'Doc' ORDER BY ID_Doc ASC;")
        docFIO = cur.fetchall()
        for i in range(len(medSpec)):
            
            medSpecStr = ''.join(medSpec[i])
            self.tableWidget.setItem(0, i, QtWidgets.QTableWidgetItem(medSpecStr))
            docFIOStr = ''.join(docFIO[i])
            self.tableWidget.setItem(1, i, QtWidgets.QTableWidgetItem(docFIOStr)) # rowPosition


            cur.execute("SELECT ID_appointment FROM Appointment WHERE ID_Doc = (SELECT ID_Doc FROM Doc WHERE Doc_FIO = (?));",(docFIOStr,))
            appointmentStatus = cur.fetchall()
            for j in range(len(appointmentStatus)):

                appointmentStatusInt = int(''.join(map(str,appointmentStatus[j])))
                

                cur.execute("SELECT Time_appointment FROM Appointment WHERE ID_appointment = (?);",(appointmentStatusInt,))
                appointmentTime = cur.fetchall()
                appointmentTimeStr = ''.join(appointmentTime[0])

                cur.execute("SELECT Pat_FIO FROM Patient_card WHERE ID_Pat = (SELECT ID_Pat FROM Appointment WHERE ID_appointment = (?));",(appointmentStatusInt,))
                appointmentPac = cur.fetchall()

                print(appointmentPac)
                print(type(appointmentPac))

                appointmentPacStr = ''.join(appointmentPac[0])

                item = QTableWidgetItem()
                item.setData(Qt.EditRole, appointmentPacStr)

                if appointmentTimeStr == '9:00':  
                    self.tableWidget.setItem(2, i, item)
                elif appointmentTimeStr == '9:30':  

                    self.tableWidget.setItem(3, i, item)
                elif appointmentTimeStr == '10:00':  
                    self.tableWidget.setItem(4, i, item)
                elif appointmentTimeStr == '10:30': 

                    self.tableWidget.setItem(5, i, item)
                elif appointmentTimeStr == '11:00':  
                    self.tableWidget.setItem(6, i, item)
                elif appointmentTimeStr == '11:30': 

                    self.tableWidget.setItem(7, i, item)
                elif appointmentTimeStr == '12:00':  
                    self.tableWidget.setItem(8, i, item)
                elif appointmentTimeStr == '12:30': 

                    self.tableWidget.setItem(9, i, item)
                elif appointmentTimeStr == '13:00':  
                    self.tableWidget.setItem(10, i, item)
                elif appointmentTimeStr == '13:30':  
                    
                    self.tableWidget.setItem(11, i, item)
                elif appointmentTimeStr == '14:00':  
                    self.tableWidget.setItem(12, i, item)
                elif appointmentTimeStr == '14:30':  

                    self.tableWidget.setItem(13, i, item)
                elif appointmentTimeStr == '15:00':  
                    self.tableWidget.setItem(14, i, item)
                elif appointmentTimeStr == '15:30':  
                    self.tableWidget.setItem(15, i, item)

                elif appointmentTimeStr == '16:00':  
                    self.tableWidget.setItem(16, i, item)
                elif appointmentTimeStr == '16:30':  
                    self.tableWidget.setItem(17, i, item)
 

                # appointmentStatusStr = ''.join(appointmentStatus[i])

                # self.tableWidget.setItem(j+2, i , QtWidgets.QTableWidgetItem('1' + appointmentStatusInt))
                
                # if appointmentStatusStr == '0':
                #     self.tableWidget.setItem(j+2, i , QtWidgets.QTableWidgetItem('0 Запись свободная'))


                # if appointmentStatusStr == '1':
                #     self.tableWidget.setItem(j+2, i , QtWidgets.QTableWidgetItem('1 Запись занята'))

                # if appointmentStatusStr == '2':
                #     self.tableWidget.setItem(j+2, i , QtWidgets.QTableWidgetItem('2 Запись подтверждена'))
                    




def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
    



if __name__ == '__main__':  
    main()