import sys 
import sqlite3 
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import MainWindow_2 as MainWindow
from functools import partial
from PyQt5.QtCore import Qt
import datetime
import RegWindow as RegWindow
from datetime import date
conn = sqlite3.connect(r'DB/SAR.DB')
cur = conn.cursor()
# data = ['table']

class RegWindow(QtWidgets.QMainWindow, RegWindow.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.showFullScreen()
        self.pushButtonStatus2.hide()
        self.pushButtonStatus3.hide()
        while True:
            self.BoxDoc()
            return
        

    def BoxDoc(self):
        cur.execute("""SELECT Doc_FIO FROM Doc""",())
        docFIO = cur.fetchall()
        # ↓ переформотируем tuple в int/str
        for i in range(len(docFIO)):
            docFIOStr = ''.join(docFIO[i])
            comboBoxDoc = self.comboBoxDoc
            comboBoxDoc.addItem(docFIOStr)

        self.pushButtonStatus2.setText('Выбрать дату')
        self.pushButtonStatus.clicked.connect(self.BoxDate)

    def BoxDate(self):

        self.pushButtonStatus2.show()
        self.pushButtonStatus.hide()

        print ("мы делаем дело")
        global currentDocFIOStr
        currentDocFIOStr = str(self.comboBoxDoc.currentText()) 
        
        cur.execute("""SELECT Day_appointment FROM Appointment 
                        WHERE ID_Doc = (SELECT ID_Doc FROM Doc 
                            WHERE Doc_FIO = (?)) 
                        GROUP BY Day_appointment""",(currentDocFIOStr,))
        DayAppointment = cur.fetchall()

        for i in range(len(DayAppointment)):
            DayAppointmentStr = ''.join(DayAppointment[i])
            comboBoxDate = self.comboBoxDate
            comboBoxDate.addItem(DayAppointmentStr)
        
        
        self.pushButtonStatus2.clicked.connect(self.BoxTime)
        return 0 

    def BoxTime(self):
        self.pushButtonStatus2.hide()
        self.pushButtonStatus3.show()
        global currentDateStr
        currentDateStr = str(self.comboBoxDate.currentText()) 
        self.pushButtonStatus.setText('Выбрать время')
        cur.execute("""SELECT Time_appointment FROM Appointment 
                        WHERE ID_Doc = (SELECT ID_Doc FROM Doc 
                            WHERE Doc_FIO = (?)) 
                        AND Day_appointment = (?)""",(currentDocFIOStr,currentDateStr,))
        TimeAppointment = cur.fetchall()
        
        for i in range(len(TimeAppointment)):
            TimeAppointmentStr = ''.join(TimeAppointment[i])
            comboBoxTime = self.comboBoxTime
            comboBoxTime.addItem(TimeAppointmentStr)
            
        self.pushButtonStatus3.setText('Подтвердить запись')
        self.pushButtonStatus3.clicked.connect(self.PacFIO)

    def PacFIO(self):
        # print (currentDocFIOStr)
        # print (currentDateStr)
        self.textEditFIO.setText('asdsad')
        currentPacFIO = self.textEditFIO.toPlainText() 
        print(self.textEditFIO.toPlainText() )


class MainWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        # self.showFullScreen()


        self.label_date.setText(datetime.datetime.today().strftime('%d.%m.%Y')) 
        # self.label_date.setText('17.11.2023')

        self.tableFil()
    
        self.pushButton_left.clicked.connect(self.onLeftBut_NewRes)
        self.pushButton_right.clicked.connect(self.onRightBut)

    def onLeftBut(self):
        ourDate = self.label_date.text()
        Date2 = datetime.datetime.strptime(ourDate, '%d.%m.%Y') + datetime.timedelta(days=-1)
        ourDate = Date2.strftime('%d.%m.%Y') 
        self.label_date.setText(ourDate)
        self.tableClean()
        self.tableFil()

    def onLeftBut_NewRes(self):
        self.RegWindow= RegWindow()
        self.RegWindow.show()
        # self.hide()




    def onRightBut(self):
        ourDate = self.label_date.text()
        Date2 = datetime.datetime.strptime(ourDate, '%d.%m.%Y') + datetime.timedelta(days=1)
        ourDate = Date2.strftime('%d.%m.%Y') 
        self.label_date.setText(ourDate)
        self.tableClean()
        self.tableFil()
        


    def tableClean(self):
        self.tableWidget.clear()
        # rowNum=0
        # colNum=0
        # while rowNum<5:
        #     while colNum <16:
        #         item = QTableWidgetItem() 
        #         item.setBackground(QtGui.QColor(255, 10, 10)) 
        #         sus = '-'
        #         item.setData(Qt.EditRole, sus) 
        #         self.tableWidget.setItem(colNum+2, rowNum, item)
        #         colNum+1
        #     rowNum+1




    def tableFil(self):
        print("АХАХАХАХАХХ РОМ")
        ourDate = self.label_date.text()
        # tableWidget.clear()
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
                if len(currentAppointmentId) > 0:
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

                    # ↓ проверка состояния записи, окрашивание ячейки
                    if appointmentStatusStr == 0:
                        item.setBackground(QtGui.QColor(255, 128, 128))
                    elif  appointmentStatusStr == 1:
                        item.setBackground(QtGui.QColor(200, 200, 200))
                    elif  appointmentStatusStr == 2:
                        item.setBackground(QtGui.QColor(98, 111, 222))
                    
                    # ↓ Вставляем данные в таблицу
                    self.tableWidget.setItem(j+2, i, item)
            # self.tableWidget.itemClicked.connect(lambda: print('Button clicked'))
    #     self.pushButton_right.clicked.connect(self.def1)
    
    # def def1(self):
    #     self.label_date.setText('a')
    # def def1(self):
    #     self.appointmentDoctorWindow= appointmentDoctorWindow()
    #     self.appointmentDoctorWindow.show()
    #     self.hide()
        # self.def2







def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
    



if __name__ == '__main__':  
    main()