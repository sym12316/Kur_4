import sys 
import sqlite3 
import datetime
from datetime import date

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt

import UI_DocFilther as DocFilther
import UI_MainWindow as MainWindow
import UI_AppoimentWindowInTable as Appointment_Window
import UI_NotificationDialog as NotificationDialog
import UI_RegWindow as RegWindow
from functools import partial

# from registration import RegWindow as registration #попытка переноса в другой файл
conn = sqlite3.connect(r'DB/SAR.DB')
cur = conn.cursor()
                                        # , MainWindow.Ui_MainWindow
class NotificationDialog(QtWidgets.QDialog, NotificationDialog.Ui_Dialog):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        
        self.setupUi(self)
        self.main = root

        self.label_Notification.setText(self.label_Notification.text() + self.main.AppointmentCollor)

        self.label_Data.setText(self.label_Data.text() + self.main.tableWidget.item(self.main.sel_row, self.main.sel_col ).text())
      
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(lambda:self.close())

    def accept(self):
        
        if self.main.AppointmentCollor == 'запись подтверждена':
            appointment_Status = 2
        elif self.main.AppointmentCollor == 'запись не подтверждена':
            appointment_Status = 1
        else: 
            self.label_Data.setText("Возникла ошибка.\nexiption 101")

        appointment_Id = self.main.tableWidget.item(self.main.sel_row, self.main.sel_col).statusTip()

        cur.execute(""" UPDATE Appointment set appointment_status = (?)
                        WHERE ID_appointment = (?)""",(appointment_Status, appointment_Id,))
        conn.commit()
        self.main.tableFillSpec()

        self.close()

class Appointment_Window(QtWidgets.QMainWindow, Appointment_Window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.showFullScreen()
        self.labelStatus.setText('')
        # Sell_Data,Doc_Fio,Doc_Spec
        self.Num_Fio_Pac = Sell_Data.split("\n")

        self.label_Date_Day.setText(ourDate)
        self.label_Date_Time.setText(self.Num_Fio_Pac[0])
        self.label_doc_fio.setText(Doc_Fio)
        self.label_spec.setText(Doc_Spec)

        self.pushButton_Appointment.clicked.connect(self.PacFIO)


    def PacFIO(self):
        currentPacFIO = self.textEdit_Pac_Fio.toPlainText() 

        if currentPacFIO == "":
            self.labelStatus.setText("Введите ФИО пациента!")
            self.PacFIO
        else:

            currentPacFIO = self.textEdit_Pac_Fio.toPlainText()
            cur.execute(""" SELECT Pat_FIO,ID_Pat FROM Patient_card
                            WHERE Pat_FIO = (?)""",(currentPacFIO,))
            Pac_Data_From_SQL = cur.fetchall()
            
            if Pac_Data_From_SQL != []:
                if self.checkBox_Appointment.isChecked() == 1:
                    self.PacID = Pac_Data_From_SQL[0][1]
                    
                    self.PacRegistration()

                else: 
                    self.labelStatus.setText("""Пациент уже присутствует в базе данных.
                                                \nНе установлен флаг 'Карта существует', продолжить?""")
                    self.PacID = Pac_Data_From_SQL[0][1]
                    self.pushButton_Appointment.clicked.connect(self.PacRegistration)

            else:
                if self.checkBox_Appointment.isChecked() == 1:
                    
                    cur.execute(""" INSERT INTO Patient_card(Pat_FIO,Pat_Card) VALUES(?,1);""",(currentPacFIO,))
                    self.labelStatus.setText('Добавлен существующий(????) Пациент.')
                else: 
                    cur.execute(""" INSERT INTO Patient_card(Pat_FIO) VALUES(?);""",(currentPacFIO,))
                    self.labelStatus.setText('Добавлен новый Пациент.')
                conn.commit()

                cur.execute(""" SELECT ID_Pat FROM Patient_card 
                                WHERE Pat_FIO = (?) """,(currentPacFIO,))
                ID_Pat = cur.fetchall()
                self.PacID = int(''.join(map(str,ID_Pat[0])))

                self.PacRegistration()


    def PacRegistration(self):
        # вставляем : PacID 
        
        cur.execute("""SELECT ID_appointment FROM Appointment 
                        WHERE ID_Doc = (SELECT ID_Doc FROM Doc 
                            WHERE Doc_FIO = (?)) 
                        AND Day_appointment = (?)
                        AND Time_appointment =(?)
                        AND appointment_status = 0""",(Doc_Fio, ourDate, self.Num_Fio_Pac[0],))
        IDAppointment = cur.fetchall()
        currentIDAppointment = int(''.join(map(str,IDAppointment[0])))
        
        cur.execute("""Update Appointment set ID_Pat = (?) ,appointment_status = 1 where ID_appointment = (?)""",(self.PacID, currentIDAppointment,))
        conn.commit()
        self.labelStatus.setText(self.labelStatus.text()+'\nЗапись успешно добалена!')

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
        # print (TimeAppointment)
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
            # print (self.textEditFIO.toPlainText())
            
            cur.execute(""" SELECT Pat_FIO,ID_Pat FROM Patient_card """)
            AllPac = cur.fetchall()
            # print(AllPac)
            for i in range(len(AllPac)):
                if self.textEditFIO.toPlainText() == AllPac[i][0]:
                    cur.execute(""" SELECT ID_Pat FROM Patient_card 
                                        WHERE Pat_FIO = (?) """,(self.textEditFIO.toPlainText(),))
                    PacID = cur.fetchall()
                    self.currentPacID = int(''.join(map(str,PacID[0])))
                    
                    self.PacRegistration()
            asd = self.textEditFIO.toPlainText()
            cur.execute(""" INSERT INTO Patient_card(Pat_FIO) VALUES(?);""",(asd,))
            conn.commit()
            
            cur.execute(""" SELECT ID_Pat FROM Patient_card 
                                        WHERE Pat_FIO = (?) """,(self.textEditFIO.toPlainText(),))
            PacID = cur.fetchall()
            self.currentPacID = int(''.join(map(str,PacID[0])))
            self.PacRegistration()

    def PacRegistration(self):
        # вставляем : PacID 
        currentTimeStr = self.comboBoxTime.currentText()
        cur.execute("""SELECT ID_appointment FROM Appointment 
                        WHERE ID_Doc = (SELECT ID_Doc FROM Doc 
                            WHERE Doc_FIO = (?)) 
                        AND Day_appointment = (?)
                        AND Time_appointment =(?)
                        AND appointment_status = 0""",(currentDocFIOStr,currentDateStr,currentTimeStr,))
        IDAppointment = cur.fetchall()
        currentIDAppointment = int(''.join(map(str,IDAppointment[0])))

        cur.execute("""Update Appointment set ID_Pat = (?) ,appointment_status = 1 where ID_appointment = (?)""",(self.currentPacID,currentIDAppointment,))
        conn.commit()
        
class DocFilther(QtWidgets.QDialog, DocFilther.Ui_Dialog):
    def __init__(self, root):
        super().__init__(root)
        self.setupUi(self)
        self.filtherDoc()
        self.main = root
        self.pushButtonSelect.clicked.connect(self.onButtonSelect)
        self.pushButtonDeselect.clicked.connect(self.onButtonDeselect)
        self.tableWidget.selectionModel().selectionChanged.connect(self.on_selectionChanged)
        self.pushButtonApply.clicked.connect(self.onButtonApply)
                
    def onButtonApply(self):
        
        self.main.whatYouNeed = [self.whatAreYouLookingFor]

        for j in range(self.tableWidget.columnCount()):
            
            for i in range(self.tableWidget.rowCount()):
                list_1 = []
                if self.tableWidget.item(i,j) != None: 
                    if self.tableWidget.item(i,j).statusTip() == '1':
                        list_1.append(self.tableWidget.item(i,j).text())
                if list_1 != []:
                    
                    if self.whatAreYouLookingFor == 1:
                        list_1.append(self.tableWidget.item(0,j).text())
                    self.main.whatYouNeed.append(tuple(list_1))

        # print(self.main.whatYouNeed)
        self.main.whoseScheduleIsThis()
        self.close()
     
    def on_selectionChanged(self, selected, deselected):	
        for ix in selected.indexes():
            self.sel_row=ix.row()
            self.sel_col=ix.column()

    def onButtonSelect(self):
        self.pushButtonSelect.setStyleSheet('QPushButton {background-color: #a3c6c0;}')
        item = QTableWidgetItem()
        item = self.tableWidget.item(self.sel_row, self.sel_col)
        item.setStatusTip('1')
        item.setBackground(QtGui.QColor(100,255,100))
        self.tableWidget.takeItem(self.sel_row, self.sel_col)
        self.tableWidget.setItem(self.sel_row, self.sel_col, item)

    def onButtonDeselect(self):
        self.pushButtonSelect.setStyleSheet('QPushButton {background-color: #a3c6c0;}')
        item = QTableWidgetItem()
        item = self.tableWidget.item(self.sel_row, self.sel_col)
        item.setStatusTip('0')
        item.setBackground(QtGui.QColor(255,255,255))
        self.tableWidget.takeItem(self.sel_row, self.sel_col)
        self.tableWidget.setItem(self.sel_row, self.sel_col, item)

    def filtherDoc(self):
        self.whatAreYouLookingFor = 1
        self.tableWidget.clear()
        self.pushButtonChangeFilter.setText("Перейти в поиск\nпо специальности")
        cur.execute("SELECT Spec FROM 'Doc' GROUP BY Spec ORDER BY ID_Doc ASC;")
        docSpec = cur.fetchall()
        
        self.tableWidget.setColumnCount(len(docSpec))
        
        cur.execute("""SELECT count(Doc_FIO) FROM Doc
                    GROUP BY Spec""")
        numberRow = str(max(cur.fetchall()))
        self.tableWidget.setRowCount(int(numberRow.replace(',','').replace('(','').replace(')',''))+1)
        for i in range(len(docSpec)):
            item = QTableWidgetItem()
            item.setBackground(QtGui.QColor(240, 240, 240))
            item.setText(str(docSpec[i][0]))
            
            cur.execute(""" SELECT Doc_FIO FROM 'Doc'
                            WHERE Spec = (?)
                            ORDER BY ID_Doc ASC;""", (str(docSpec[i][0]),))
            docFIO = cur.fetchall()
            # self.tableWidget.setColumnCount(len(docSpec)+1)
            self.tableWidget.setItem(0,i, item)

            for j in range(len(docFIO)):
                item = QTableWidgetItem()
                item.setText(str(docFIO[j][0]))
                item.setStatusTip('0')
                self.tableWidget.setItem(j+1,i, item)
        self.pushButtonChangeFilter.clicked.connect(self.filtherSpec)

    def filtherSpec(self):
        self.whatAreYouLookingFor = 0
        self.tableWidget.clear()
        self.pushButtonChangeFilter.setText("Перейти в поиск \nпо врачам")
        cur.execute("SELECT Spec FROM 'Doc' GROUP BY Spec ORDER BY ID_Doc ASC;")
        docSpec = cur.fetchall()
        
        self.tableWidget.setRowCount(len(docSpec))
        self.tableWidget.setColumnCount(1)
        for i in range(len(docSpec)):
            item = QTableWidgetItem()
            item.setBackground(QtGui.QColor(240, 240, 240))
            item.setText(str(docSpec[i][0]))
            item.setStatusTip('0')
            self.tableWidget.setItem(i,0, item)

        self.pushButtonChangeFilter.clicked.connect(self.filtherDoc)

class MainWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, **kwargs):
        super().__init__( **kwargs)
        self.setupUi(self)  
        # self.showFullScreen()

        
        self.pushButton_change_appointment_green.setStyleSheet('QPushButton {background-color: #a3c6c0;}')
        self.pushButton_change_appointment_blue.setStyleSheet('QPushButton {background-color: #626fde;}')

        # self.label_date.setText(datetime.datetime.today().strftime('%d.%m.%Y')) 
        self.label_date.setText('29.11.2023')

        self.weekdayDefining()
        
        # # # # # # # # # # # # # # # # # # # # # # # # # # # 
        # self.whatYouNeed = [-1]
        self.firstFilling()
        # # # # # # # # # # # # # # # # # # # # # # # # # # # 


        self.pushButton_left_day.clicked.connect(self.onLeftDayButton)
        self.pushButton_right_day.clicked.connect(self.onRightDayButton)
        self.pushButton_left_week.clicked.connect(self.onLeftWeekButton)
        self.pushButton_right_week.clicked.connect(self.onRightWeekButton)

        self.pushButtonNewRes.clicked.connect(self.onBut_NewRes)
        self.pushButtonUpdateTable.clicked.connect(self.tableFillSpec)
        
        self.pushButtonUpdateRes.clicked.connect(self.onBut_UpdateRes)
        self.tableWidget.selectionModel().selectionChanged.connect(self.on_selectionChanged)

        self.pushButton_change_appointment_green.clicked.connect(self.onChangeAppointmentGreenButton)
        self.pushButton_change_appointment_blue.clicked.connect(self.onChangeAppointmentBlueButton)

        self.pushButton_Search.clicked.connect(self.DocFilther)

    def DocFilther(self):
        self.DocFilther = DocFilther(self)  
        self.DocFilther.show()
        
    def on_selectionChanged(self, selected, deselected):	
        for ix in selected.indexes():
            # print('Selected Cell Location Row: {0}, Column: {1}'.format(ix.row(), ix.column()))
            self.pushButtonUpdateRes.setText("Записать пациента в пустую ячейку")
            self.pushButton_change_appointment_green.setText('Изменить \nстатус \nприёма')
            self.pushButton_change_appointment_blue.setText('Изменить \nстатус \nприёма')
            self.sel_row=ix.row()
            self.sel_col=ix.column()
        # for ix in deselected.indexes():
        #     print('Deselected Cell Location Row: {0}, Column: {1}'.format(ix.row(), ix.column()))

    def onBut_UpdateRes(self, selected):
        
        global Sell_Data,Doc_Fio,Doc_Spec,ourDate
        
        if self.tableWidget.currentItem() == None:
            self.pushButtonUpdateRes.setText('Ячейка пуста')
        else:

            Sell_Data_Str = self.tableWidget.item(self.sel_row, self.sel_col ).text()
            Sell_Data_Split_Str = Sell_Data_Str.split("\n")  

            if Sell_Data_Split_Str[1] != 'Свободно':
                self.pushButtonUpdateRes.setText('Записать пациента в ПУСТУЮ ячейку')
            else:
                ourDate=self.label_date.text()
                Doc_Spec = self.tableWidget.item(0, self.sel_col ).text()
                Doc_Fio = self.tableWidget.item(1, self.sel_col ).text()
                Sell_Data = self.tableWidget.item(self.sel_row, self.sel_col ).text()
                self.Appointment_Window = Appointment_Window()
                self.Appointment_Window.show()

    def onChangeAppointmentGreenButton(self):
        if self.tableWidget.currentItem() == None:
            self.pushButton_change_appointment_green.setText('Ячейка пуста')
        else:

            Sell_Data_Str = self.tableWidget.item(self.sel_row, self.sel_col ).text()
            Sell_Data_Split_Str = Sell_Data_Str.split("\n")  

            if Sell_Data_Split_Str[1] == 'Свободно':
                self.pushButton_change_appointment_green.setText('Ячейка свободна')
            elif self.tableWidget.item(self.sel_row, self.sel_col).background().color().getRgb() == (163, 198, 192, 255):
                self.pushButton_change_appointment_green.setText('Уже установленно\n состояние запись\nне подтверждена')
            else:
                
                self.AppointmentCollor = 'запись не подтверждена'
                self.dialog = NotificationDialog(self)
                self.dialog.show()

    def onChangeAppointmentBlueButton(self):
        if self.tableWidget.currentItem() == None:
            self.pushButton_change_appointment_green.setText('Ячейка пуста')
        else:

            Sell_Data_Str = self.tableWidget.item(self.sel_row, self.sel_col ).text()
            Sell_Data_Split_Str = Sell_Data_Str.split("\n")  

            if Sell_Data_Split_Str[1] == 'Свободно':
                self.pushButton_change_appointment_green.setText('Ячейка свободна')
            elif self.tableWidget.item(self.sel_row, self.sel_col).background().color().getRgb() == (98, 111, 222):
                self.pushButton_change_appointment_green.setText('Уже установленно \nсостояние \nзапись подтверждена')
            else:
                self.AppointmentCollor = 'запись подтверждена'
                self.dialog = NotificationDialog(self)
                self.dialog.show()

    def onBut_NewRes(self):
        self.RegWindow = RegWindow()
        self.RegWindow.show()
        # self.hide()

    def onLeftDayButton(self):
        ourDate = self.label_date.text()
        Date2 = datetime.datetime.strptime(ourDate, '%d.%m.%Y') + datetime.timedelta(days=-1)
        ourDate = Date2.strftime('%d.%m.%Y') 
        self.label_date.setText(ourDate)
        self.weekdayDefining()
        self.tableFillSpec()   

    def onRightDayButton (self):
        ourDate = self.label_date.text()
        Date2 = datetime.datetime.strptime(ourDate, '%d.%m.%Y') + datetime.timedelta(days=1)
        ourDate = Date2.strftime('%d.%m.%Y') 
        self.label_date.setText(ourDate)
        self.weekdayDefining()
        self.tableFillSpec()

    def onLeftWeekButton(self):

        ourDate = self.label_date.text()
        Date2 = datetime.datetime.strptime(ourDate, '%d.%m.%Y') + datetime.timedelta(days=-7)
        ourDate = Date2.strftime('%d.%m.%Y') 
        self.label_date.setText(ourDate)
        self.weekdayDefining()
        self.tableFillSpec()

    def onRightWeekButton(self):

        ourDate = self.label_date.text()
        Date2 = datetime.datetime.strptime(ourDate, '%d.%m.%Y') + datetime.timedelta(days=7)
        ourDate = Date2.strftime('%d.%m.%Y')
        self.label_date.setText(ourDate)
        self.weekdayDefining()
        self.tableFillSpec()

    def weekdayDefining(self):
        day = datetime.datetime.strptime(self.label_date.text(), '%d.%m.%Y').weekday()
        if day == 0:
            Weekday_Now = 'Понедельник'
        elif day == 1:
            Weekday_Now = 'Вторник'
        elif day == 2:
            Weekday_Now = 'Среда'
        elif day == 3:
            Weekday_Now = 'Четверг'
        elif day == 4:
            Weekday_Now = 'Пятница'
        elif day == 5:
            Weekday_Now = 'Суббота'
        elif day == 6:
            Weekday_Now = 'Воскресенье'
        
        self.label_weekday.setText(Weekday_Now)

    def firstFilling(self):
        cur.execute("SELECT Spec FROM 'Doc' GROUP BY Spec;")
        self.dsa = cur.fetchall()
        
        self.whatYouNeed = [0] + self.dsa
        print(self.whatYouNeed)
        self.whoseScheduleIsThis()

    def whoseScheduleIsThis(self):
        
        if self.whatYouNeed[0] == 0:
            
            self.whatYouNeed.pop(0)

            self.asd = []
            for i in range(len(self.whatYouNeed)):
                cur.execute(""" SELECT Doc_FIO,Spec FROM 'Doc' 
                                WHERE Spec = (?)
                                ORDER BY ID_Doc ASC;""",(str(self.whatYouNeed[i][0]),))
                docFioTmp = cur.fetchall()
                self.asd = self.asd + docFioTmp
                # print(self.whatYouNeed[2][0])
            self.tableFillSpec()
            
        elif self.whatYouNeed[0] == 1:
            
            self.whatYouNeed.pop(0)
            self.asd = self.whatYouNeed
            self.tableFillSpec()

    def tableFillSpec(self):
        # print(self.asd)
        

        self.tableWidget.clear()
        ourDate = self.label_date.text()
        

        docFIO = self.asd

        for i in range(len(docFIO)):
            self.tableWidget.setColumnWidth(i, 140)

            self.tableWidget.setItem(0, i, QtWidgets.QTableWidgetItem(str(docFIO[i][1])))
            self.tableWidget.setItem(1, i, QtWidgets.QTableWidgetItem(str(docFIO[i][0])))
            # ↑ 
            
            # ↓ забиваем ячейки в столбце
            # ↓ запрос на выдачу ID приёмов
            cur.execute("""SELECT ID_appointment,Time_appointment,appointment_status,ID_Pat FROM Appointment
            WHERE ID_Doc = (SELECT ID_Doc FROM Doc WHERE Doc_FIO = (?))
            AND Day_appointment = (?)
            ORDER BY Time_appointment;""",(str(docFIO[i][0]),ourDate,))
            # ↓ переформотируем tuple в int/str

            # ID_appointment,Time_appointment,appointment_status,ID_Pat # 
            #       0               1               2               3   # 
            CurrentData = cur.fetchall()
            
            for j in range(len(CurrentData)):
                self.tableWidget.setRowHeight(j+2, 75)
                item = QTableWidgetItem()
 
 
                item.setStatusTip(str (CurrentData[j][0]))
                
                if len(CurrentData)+2 > self.tableWidget.rowCount():
                    self.tableWidget.setRowCount(len(CurrentData)+2)
                # print(self.tableWidget.rowCount())
                Pat_ID = CurrentData[j][3]
                cur.execute("""SELECT Pat_FIO, Phone_num, Pat_Card FROM Patient_card
                WHERE ID_Pat = (?)""",(Pat_ID,))
                
                PatData = cur.fetchall()
                
                if PatData[0][2] == 1:
                    item.setText('{0}\n{1} - {2}\n{3}'.format(CurrentData[j][1], PatData[0][0], PatData[0][2], PatData[0][1]))
                elif PatData[0][2] == 0:
                    item.setText('{0}\n{1}\n{2}'.format(CurrentData[j][1], PatData[0][0], PatData[0][1]))
                else:
                    print('Ошибка')

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



    def tableCleanAndFil(self):
        
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
            self.tableWidget.setColumnWidth(i, 140)

            # ↓ 
            medSpecStr = ''.join(medSpec[i])
            self.tableWidget.setItem(0, i, QtWidgets.QTableWidgetItem(medSpecStr))
            # ↑ 
            # ↓ 
            docFIOStr = ''.join(docFIO[i])
            self.tableWidget.setItem(1, i, QtWidgets.QTableWidgetItem(docFIOStr))
            # ↑ 
            
            # ↓ забиваем ячейки в столбце
            # ↓ запрос на выдачу ID приёмов
            cur.execute("""SELECT ID_appointment,Time_appointment,appointment_status,ID_Pat FROM Appointment
            WHERE ID_Doc = (SELECT ID_Doc FROM Doc WHERE Doc_FIO = (?))
            AND Day_appointment = (?)
            ORDER BY Time_appointment;""",(docFIOStr,ourDate,))
            # ↓ переформотируем tuple в int/str

            # ID_appointment,Time_appointment,appointment_status,ID_Pat # 
            #       0               1               2               3   # 
            CurrentData = cur.fetchall()
            
            for j in range(len(CurrentData)):
                self.tableWidget.setRowHeight(j+2, 75)
                item = QTableWidgetItem()
 
 
                item.setStatusTip(str (CurrentData[j][0]))
                

                Pat_ID = CurrentData[j][3]
                cur.execute("""SELECT Pat_FIO, Phone_num, Pat_Card FROM Patient_card
                WHERE ID_Pat = (?)""",(Pat_ID,))
                
                PatData = cur.fetchall()
                
                if PatData[0][2] == 1:
                    item.setText('{0}\n{1} - {2}\n{3}'.format(CurrentData[j][1], PatData[0][0], PatData[0][2], PatData[0][1]))
                elif PatData[0][2] == 0:
                    item.setText('{0}\n{1}\n{2}'.format(CurrentData[j][1], PatData[0][0], PatData[0][1]))
                else:
                    print('Ошибка')

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
                


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
   
if __name__ == '__main__':  
    main()