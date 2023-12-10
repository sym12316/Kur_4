import sys 
import sqlite3 
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from functools import partial
from PyQt5.QtCore import Qt
import UI_RegWindow as RegWindow
conn = sqlite3.connect(r'DB/SAR.DB')
cur = conn.cursor()

class RegWindow(QtWidgets.QMainWindow, RegWindow.Ui_Form):
    def __init__(self):
        super().__init__()
        # self.registration.RegWindow = RegWindow()
        # self.registration.RegWindow.show()
        self.setupUi(self)
        # self.showFullScreen()
        self.pushButtonStatus.setText('Выбрать врача')
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

        # print ("мы делаем дело")
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
        print (currentDocFIOStr)
        print (currentDateStr)
        

        # self.textEditFIO.setText('asdsad')
        currentTimeStr = str(self.comboBoxTime.currentText()) 
        print (currentTimeStr)
        currentPacFIO = self.textEditFIO.toPlainText() 
        print(self.textEditFIO.toPlainText() )

        # pacientAppointmentinformation = (currentDocFIOStr,currentDateStr,currentTimeStr,currentPacFIO)
        # cur.execute("""INSERT INTO Appointment(Pac_fio, Day_appointment, Time_appointment,) 
        # VALUES(?,?,?);""",pacientAppointmentinformation)
        # conn.commit()