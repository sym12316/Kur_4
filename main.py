import sys 
import sqlite3 
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import UI_MainWindow as MainWindow
from functools import partial
from PyQt5.QtCore import Qt
import datetime
import UI_RegWindow as RegWindow
from datetime import date
# from registration import RegWindow as registration #попытка переноса в другой файл
conn = sqlite3.connect(r'DB/SAR.DB')
cur = conn.cursor()

class RegWindow(QtWidgets.QMainWindow, RegWindow.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.showFullScreen()
        self.pushButtonStatus.setText('Выбрать врача')
        self.pushButtonStatus2.hide()
        self.pushButtonStatus3.hide()
        self.labelStatus.hide()
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

        # print ("мы делаем дело")
        global currentDocFIOStr
        currentDocFIOStr = str(self.comboBoxDoc.currentText()) 
        
        cur.execute("""SELECT Day_appointment FROM Appointment 
                        WHERE ID_Doc = (SELECT ID_Doc FROM Doc 
                            WHERE Doc_FIO = (?))
                        AND appointment_status = 0 
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
                        AND Day_appointment = (?)
                        AND appointment_status = 0""",(currentDocFIOStr,currentDateStr,))
        TimeAppointment = cur.fetchall()
        print (TimeAppointment)
        for i in range(len(TimeAppointment)):
            TimeAppointmentStr = ''.join(TimeAppointment[i])
            comboBoxTime = self.comboBoxTime
            comboBoxTime.addItem(TimeAppointmentStr)
            
        self.pushButtonStatus3.setText('Подтвердить запись')
        self.pushButtonStatus3.clicked.connect(self.PacFIO)

    def PacFIO(self):
        currentPacFIO = self.textEditFIO.toPlainText() 
        if currentPacFIO == "":
            self.labelStatus.show()
            self.labelStatus.setText("Введите ФИО пациента!")
            self.PacFIO
        else:
            print (currentDocFIOStr)
            print (currentDateStr)
            print (self.comboBoxTime.currentText())
            print (self.textEditFIO.toPlainText())
            # pacientAppointmentinformation = (currentDocFIOStr,currentDateStr,currentTimeStr,currentPacFIO)
            # cur.execute("""INSERT INTO Appointment(Pac_fio, Day_appointment, Time_appointment) 
            # VALUES(?,?,?);""",pacientAppointmentinformation)
            # conn.commit()
            cur.execute(""" SELECT Pat_FIO,ID_Pat FROM Patient_card """)
            AllPac = cur.fetchall()
            print(AllPac)
            for i in range(len(AllPac)):
                if self.textEditFIO.toPlainText() == AllPac[i][0]:
                    cur.execute(""" SELECT ID_Pat FROM Patient_card 
                                        WHERE Pat_FIO = (?) """,(self.textEditFIO.toPlainText(),))
                    PacID = cur.fetchall()
                    currentPacID = int(''.join(map(str,PacID[0])))
                    print (currentPacID)
                    # ФУНКЦИЯ ЗАПИСИ КЛИЕНТА
                    return 0 
            asd = self.textEditFIO.toPlainText()
            print(type(asd))
            cur.execute(""" INSERT INTO Patient_card(Pat_FIO) VALUES(?);""",(asd,))
            conn.commit()
            print("Новый клиент добавлен!")
                    
                    # ФУНКЦИЯ ЗАПИСИ КЛИЕНТА


class MainWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        # self.showFullScreen()


        self.label_date.setText(datetime.datetime.today().strftime('%d.%m.%Y')) 
        # self.label_date.setText('17.11.2023')

        self.tableCleanAndFil()
    
        self.pushButton_left.clicked.connect(self.onLeftBut)
        self.pushButton_right.clicked.connect(self.onRightBut)
        self.pushButtonNewRes.clicked.connect(self.onBut_NewRes)
        self.pushButtonUpdateTable.clicked.connect(self.tableCleanAndFil)

    # def onBut_NewRes(self): #попытка переноса в другой файл
    #     self.registration.RegWindow = RegWindow()
    #     self.registration.RegWindow.show()
    #     registration()
    #     # self.hide()

    def onBut_NewRes(self):
        self.RegWindow = RegWindow()
        self.RegWindow.show()
        # self.hide()

    def onLeftBut(self):
        ourDate = self.label_date.text()
        Date2 = datetime.datetime.strptime(ourDate, '%d.%m.%Y') + datetime.timedelta(days=-1)
        ourDate = Date2.strftime('%d.%m.%Y') 
        self.label_date.setText(ourDate)
        
        self.tableCleanAndFil()

    def onRightBut(self):
        ourDate = self.label_date.text()
        Date2 = datetime.datetime.strptime(ourDate, '%d.%m.%Y') + datetime.timedelta(days=1)
        ourDate = Date2.strftime('%d.%m.%Y') 
        self.label_date.setText(ourDate)
        
        self.tableCleanAndFil()

    def tableCleanAndFil(self):
        # print("АХАХАХАХАХ РОООООМ")
        self.tableWidget.clear()
        ourDate = self.label_date.text()
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