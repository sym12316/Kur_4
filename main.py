import sys 
import datetime
import configparser
from datetime import date
from mysql.connector import connect, Error
import mysql.connector

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt

from UI import UI_MainWindow as MainWindow
from UI import UI_DocFilther as DocFilther
from UI import UI_NewAppointmentCellWindow as newAppointmentCellWindow
from UI import UI_EditDelitingWindow as EditDelitingWindow
from UI import UI_QuestionDialog as QuestionDialog
from UI import UI_SearchFreeAppointment as SearchFreeAppointment 
from UI import UI_NewDocAndSpecWindow as NewDocAndSpecWindow
from UI import UI_NewAppoimentDayWindow as NewAppoimentDayWindow
from UI import UI_ChooseWhatEdit as ChooseWhatEdit
from UI import UI_NoticeDialog as NoticeDialog
from UI import UI_PatientSearch as PatientSearch
from UI import UI_DateChoose as DateChoose
from UI import UI_DelDocOrDay as DelDocOrDay
from UI import UI_LogWindow as LogWindow

from functools import partial

class DateChoose(QtWidgets.QDialog, DateChoose.Ui_Form):
    def __init__(self, root):
        super().__init__(root)
        
        self.setupUi(self)

        self.MainWindow = root

        self.calendarWidget.activated.connect(self.activatedDate)
        self.pushButton.clicked.connect(self.sendDateToMainWindow)
        
    def activatedDate(self):
        self.dateEdit.setDate(datetime.datetime.strptime(self.calendarWidget.selectedDate().toString('dd.MM.yyyy'), '%d.%m.%Y'))



    def sendDateToMainWindow(self):
        ourDate = self.dateEdit.text()
        self.MainWindow.setDate(ourDate)

class PatientSearch(QtWidgets.QDialog, PatientSearch.Ui_Form):
    def __init__(self, root):
        super().__init__(root)
        
        self.setupUi(self)

class QuestionDialog(QtWidgets.QDialog, QuestionDialog.Ui_Dialog):
    def __init__(self, root):
        super().__init__(root)
        
        self.setupUi(self)
        self.main = root
        # self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(lambda:self.close())

class newAppointmentCellWindow(QtWidgets.QMainWindow, newAppointmentCellWindow.Ui_MainWindow):
    def __init__(self,root):
        super().__init__(root)
        self.setupUi(self)

        self.MainWindow = root

        self.labelStatus.setText('')
        self.Num_Fio_Pac = self.MainWindow.Sell_Data.split("\n")

        self.label_Date_Day.setText(self.MainWindow.ourDate)
        self.label_Date_Time.setText(self.Num_Fio_Pac[0])
        self.label_doc_fio.setText(self.MainWindow.Doc_Fio)
        self.label_spec.setText(self.MainWindow.Doc_Spec)

        self.pushButton_Appointment.clicked.connect(self.PacFIO)

    def PacFIO(self):
        currentPacFIO = self.textEdit_Pac_Fio.toPlainText() 
        cursor = connection.cursor()
        if currentPacFIO == "":
            self.labelStatus.setText("Введите ФИО пациента!")
            self.PacFIO
        else:

            self.NoticeDialog = NoticeDialog(self)
            self.NoticeDialog.label.setText('')

            currentPacFIO = self.textEdit_Pac_Fio.toPlainText()

            requets = """SELECT Pat_FIO,ID_Pat FROM Patient_card
                            WHERE Pat_FIO = %s"""
            into = [currentPacFIO]
            cursor.execute(requets, into)
            Pac_Data_From_SQL = cursor.fetchall()

            if Pac_Data_From_SQL != []:
                # if self.checkBox_Appointment.isChecked() == 1:
                self.PacID = Pac_Data_From_SQL[0][1]

                requets = """UPDATE Patient_card set Pat_Card = 1 
                                WHERE ID_Pat = %s"""
                into = [self.PacID]
                cursor.execute(requets, into)
                connection.commit()

                self.PacRegistration()

            else:
                if self.checkBox_Appointment.isChecked() == 1:

                    requets = """INSERT INTO Patient_card(Pat_FIO, Phone_num, Pat_Card) VALUES(%s,%s,1)"""
                    into = [currentPacFIO, self.textEditl_Pac_Num.toPlainText()]
                    cursor.execute(requets, into)
                    self.NoticeDialog.label.setText('Добавленна запись для\nсуществующего пациента.')
                else: 
                    
                    requets = """INSERT INTO Patient_card(Pat_FIO, Phone_num) VALUES(%s,%s)"""
                    into = [currentPacFIO, self.textEditl_Pac_Num.toPlainText()]
                    cursor.execute(requets, into)
                    
                    self.NoticeDialog.label.setText('Добавлен новый пациент.')

                connection.commit()

                requets = """SELECT ID_Pat FROM Patient_card 
                                WHERE Pat_FIO = %s
                                AND Phone_num = %s"""
                into = [currentPacFIO, self.textEditl_Pac_Num.toPlainText()]
                cursor.execute(requets, into)
                ID_Pat = cursor.fetchall()

                self.PacID = int(''.join(map(str,ID_Pat[0])))

                self.PacRegistration()


    def PacRegistration(self):
        # вставляем : PacID 
        cursor = connection.cursor()
        self.labelStatus.setText('')

        requets = """SELECT ID_appointment FROM Appointment 
                        WHERE ID_Doc = (SELECT ID_Doc FROM Doc 
                            WHERE Doc_FIO = %s) 
                        AND Day_appointment = %s
                        AND Time_appointment =%s
                        AND appointment_status = 0"""
                        
        into = [self.MainWindow.Doc_Fio, self.MainWindow.ourDate, self.Num_Fio_Pac[0]]
        cursor.execute(requets, into)
        IDAppointment = cursor.fetchall()

        currentIDAppointment = int(''.join(map(str,IDAppointment[0])))
        
        
        requets = """UPDATE Appointment set ID_Pat = %s ,appointment_status = 1 WHERE ID_appointment = %s"""
        into = [self.PacID, currentIDAppointment]
        cursor.execute(requets, into)

        connection.commit()
        print(self.PacID, currentIDAppointment)
        self.NoticeDialog.label.setText(self.NoticeDialog.label.text()+'\nЗапись успешно добавлена!')

        self.NoticeDialog.show()
        self.NoticeDialog.pushButton.clicked.connect(self.NoticeDialog.closeParent)

        self.MainWindow.whoseScheduleIsThis()

class SearchFreeAppointment(QtWidgets.QMainWindow, SearchFreeAppointment.Ui_Form):
    def __init__(self,root):
        super().__init__(root)
        self.setupUi(self)
        self.MainWindow = root
        self.ButtonsHide()

        cursor = connection.cursor()

        requets = """SELECT Doc_FIO FROM Doc ORDER BY Doc_FIO ASC"""
        cursor.execute(requets)
        docFIO = cursor.fetchall()
        # ↓ переформотируем tuple в int/str
        for i in range(len(docFIO)):
            self.comboBoxDoc.addItem(str(docFIO[i][0]))
        
        self.comboBoxDoc.activated.connect(self.comboBox_Day_Filling)
        self.pushButtonStatus.clicked.connect(self.PacFIO)

    def comboBox_Day_Filling(self):
        self.ButtonsHide()
        self.comboBoxDate.clear()
        
        cursor = connection.cursor()

        requets = """SELECT Day_appointment FROM Appointment 
                        WHERE ID_Doc = (SELECT ID_Doc FROM Doc 
                            WHERE Doc_FIO = %s)
                        AND appointment_status = 0 
                        GROUP BY Day_appointment
                        ORDER BY Day_appointment ASC"""
        into = [self.comboBoxDoc.currentText()]
        cursor.execute(requets, into)
        DayAppointment = cursor.fetchall()

        if len(DayAppointment) == 0:
            self.labelStatus.setText('Свободных дней нет')
        else:
            for i in range(len(DayAppointment)):
                self.comboBoxDate.addItem(self.weekdayDefining(datetime.datetime.strptime(str(DayAppointment[i][0]), '%d.%m.%Y')))

        self.comboBoxDate.activated.connect(self.comboBox_Time_Filling)

    def weekdayDefining(self,day):
        day_num = day.weekday()

        if day_num == 0:
            Weekday_Now = (day.strftime('%d.%m.%Y') + ' - Понедельник')
        elif day_num == 1:
            Weekday_Now = (day.strftime('%d.%m.%Y') + ' - Понедельник')
        elif day_num == 2:
            Weekday_Now = (day.strftime('%d.%m.%Y') + ' - Среда')
        elif day_num == 3:
            Weekday_Now = (day.strftime('%d.%m.%Y') + ' - Четверг')
        elif day_num == 4:
            Weekday_Now = (day.strftime('%d.%m.%Y') + ' - Пятница')
        elif day_num == 5:
            Weekday_Now = (day.strftime('%d.%m.%Y') + ' - Суббота')
        elif day_num == 6:
            Weekday_Now = (day.strftime('%d.%m.%Y') + ' - Воскресенье')
        
        return(Weekday_Now)

    def comboBox_Time_Filling(self):
        self.ButtonsHide()

        self.labelStatus.setText('Будут показаны только \nдни с свободными приёмами.')

        self.currentDateStr = self.comboBoxDate.currentText().split(' ')
        self.currentDateStr = self.currentDateStr[0]
        
        cursor = connection.cursor()

        requets = """SELECT Time_appointment FROM Appointment 
                        WHERE ID_Doc = (SELECT ID_Doc FROM Doc 
                            WHERE Doc_FIO = %s) 
                        AND Day_appointment = %s
                        AND appointment_status = 0
                        ORDER BY Time_appointment ASC"""
        into = [self.comboBoxDoc.currentText(),self.currentDateStr]
        cursor.execute(requets, into)
        TimeAppointment = cursor.fetchall()
        
        if len(TimeAppointment) == 0:
            self.labelStatus.setText('Свободных часов нет')

        for i in range(len(TimeAppointment)):
            self.comboBoxTime.addItem(TimeAppointment[i][0])
        self.comboBoxTime.activated.connect(self.ButtonsActivated)
            
    def ButtonsHide(self):
        self.comboBoxTime.clear()
        self.labelStatus.setText('Будут показаны только \nдни с свободными приёмами.')
        self.textEditFIO.setEnabled(False)
        self.textEditFIO_2.setEnabled(False)   
        self.labelFIO.setEnabled(False)   
        self.labelPhone.setEnabled(False)   

    def ButtonsActivated(self):
        self.textEditFIO.setEnabled(1)
        self.textEditFIO_2.setEnabled(1)   
        self.labelFIO.setEnabled(1)   
        self.labelPhone.setEnabled(1)  

    def PacFIO(self):
        self.labelStatus.setText("")

        cursor = connection.cursor()

        if self.textEditFIO.toPlainText()  == "":
            self.labelStatus.setText("Введите ФИО пациента!")
        elif self.textEditFIO_2.toPlainText() == "":
            self.labelStatus.setText("Введите номер пациента!")
        else:
            # Проверка существования пациента
            self.PacID()
            if len(self.PacId) == 0:
                requets = """INSERT INTO Patient_card(Pat_FIO, Phone_num) 
                                VALUES(%s,%s)"""
                into = [self.textEditFIO.toPlainText(), self.textEditFIO_2.toPlainText()]
                cursor.execute(requets, into)
                connection.commit()
                self.PacID()
                
            self.PacRegistration()

    def PacID(self):
        cursor = connection.cursor()

        requets = """SELECT ID_Pat FROM Patient_card 
                                        WHERE Pat_FIO = %s 
                                        AND Phone_num = %s"""
        into = [self.textEditFIO.toPlainText(), self.textEditFIO_2.toPlainText()]
        cursor.execute(requets, into)
        self.PacId = cursor.fetchall()
        
    def PacRegistration(self):
        # вставляем : PacID в AppoinmentTable

        self.comboBoxTime.currentText()

        cursor = connection.cursor()

        requets = """SELECT ID_appointment FROM Appointment 
                            WHERE ID_Doc = (SELECT ID_Doc FROM Doc 
                                            WHERE Doc_FIO = %s) 
                            AND Day_appointment = %s
                            AND Time_appointment = %s
                            AND appointment_status = 0"""
        into = [self.comboBoxDoc.currentText(), self.currentDateStr, self.comboBoxTime.currentText()]
        cursor.execute(requets, into)
        IDAppointment = cursor.fetchall()
        
        requets = """UPDATE Appointment 
                            set ID_Pat = %s,
                            appointment_status = 1 
                            WHERE ID_appointment = %s"""
        into = [self.PacId[0][0], IDAppointment[0][0]]
        cursor.execute(requets, into)
        connection.commit()
        self.Notice = NoticeDialog(self)
        self.Notice.show()
        self.Notice.label.setText("Новый пациент успешно добавлен!")
        self.Notice.pushButton.clicked.connect(self.Notice.closeParent)
        self.MainWindow.whoseScheduleIsThis()

class DocFilther(QtWidgets.QDialog, DocFilther.Ui_Dialog):
    def __init__(self, root):
        super().__init__(root)
        self.setupUi(self)
        self.filtherDoc()
        self.main = root
        self.pushButtonSelect.clicked.connect(self.onButtonSelect)
        self.pushButtonDeselect.clicked.connect(self.onButtonDeselect)
        self.tableWidget.selectionModel().selectionChanged.connect(self.onSelectionChanged)
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


        self.main.whoseScheduleIsThis()
        self.close()
     
    def onSelectionChanged(self, selected, deselected):	
        for ix in selected.indexes():
            self.sel_row=ix.row()
            self.sel_col=ix.column()

    def onButtonSelect(self):
        self.pushButtonSelect.setStyleSheet('QPushButton {background-color: #a3c6c0;}')
        item = QTableWidgetItem()
        item = self.tableWidget.item(self.tableWidget.currentRow(), self.tableWidget.currentColumn())
        item.setStatusTip('1')
        item.setBackground(QtGui.QColor(100,255,100))
        self.tableWidget.takeItem(self.tableWidget.currentRow(), self.tableWidget.currentColumn())
        self.tableWidget.setItem(self.tableWidget.currentRow(), self.tableWidget.currentColumn(), item)

    def onButtonDeselect(self):
        self.pushButtonSelect.setStyleSheet('QPushButton {background-color: #a3c6c0;}')
        item = QTableWidgetItem()
        item = self.tableWidget.item(self.tableWidget.currentRow(), self.tableWidget.currentColumn())
        item.setStatusTip('0')
        item.setBackground(QtGui.QColor(255,255,255))
        self.tableWidget.takeItem(self.tableWidget.currentRow(), self.tableWidget.currentColumn())
        self.tableWidget.setItem(self.tableWidget.currentRow(), self.tableWidget.currentColumn(), item)

    def filtherDoc(self):
        self.whatAreYouLookingFor = 1
        self.tableWidget.clear()
        self.pushButtonChangeFilter.setText("Перейти в поиск\nпо специальности")
        self.pushButtonSelect.setText("Выбрать врача")
        self.pushButtonDeselect.setText("Убрать врача")
        
        cursor = connection.cursor()

        requets = """SELECT Spec FROM Doc GROUP BY Spec"""
        cursor.execute(requets)
        docSpec = cursor.fetchall()

        self.tableWidget.setColumnCount(len(docSpec))
        
        requets = """SELECT count(Doc_FIO) FROM Doc
                    GROUP BY Spec"""
        cursor.execute(requets)
        numberRow = str(max(cursor.fetchall()))
        self.tableWidget.setRowCount(int(numberRow.replace(',','').replace('(','').replace(')',''))+1)
        for i in range(len(docSpec)):
            item = QTableWidgetItem()
            item.setBackground(QtGui.QColor(240, 240, 240))
            item.setText(str(docSpec[i][0]))
            
            requets = """SELECT Doc_FIO FROM Doc
                            WHERE Spec = %s
                            ORDER BY ID_Doc ASC"""
            into = [str(docSpec[i][0])]
            cursor.execute(requets, into)
            docFIO = cursor.fetchall()

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
        self.pushButtonSelect.setText("Выбрать специальность")
        self.pushButtonDeselect.setText("Убрать специальность")

        cursor = connection.cursor()

        requets = """SELECT Spec FROM Doc GROUP BY Spec"""
        cursor.execute(requets)
        docSpec = cursor.fetchall()
        
        self.tableWidget.setRowCount(len(docSpec))
        self.tableWidget.setColumnCount(1)
        for i in range(len(docSpec)):
            item = QTableWidgetItem()
            item.setBackground(QtGui.QColor(240, 240, 240))
            item.setText(str(docSpec[i][0]))
            item.setStatusTip('0')
            self.tableWidget.setItem(i,0, item)

        self.pushButtonChangeFilter.clicked.connect(self.filtherDoc)

class NewAppoimentDayWindow(QtWidgets.QMainWindow, NewAppoimentDayWindow.Ui_Form):
    def __init__(self, root):
        super().__init__(root)
        self.setupUi(self)

        self.MainWindow = root
        
        cursor = connection.cursor()

        requets ="""SELECT Spec FROM Doc GROUP BY Spec"""
        cursor.execute(requets)
        docSpec = cursor.fetchall()

        # ↓ переформотируем tuple в int/str
        for i in range(len(docSpec)):
            docSpecStr = ''.join(docSpec[i])
            # self.comboBox = self.comboBoxDoc
            self.comboBox_Doc_Spec.addItem(docSpecStr)
        self.comboBox_Doc_Fio_Filling()
        

        self.pushButton_Accept_New_Day.clicked.connect(self.onButton_Accept_New_Day)
        self.comboBox_Doc_Spec.activated.connect(self.comboBox_Doc_Fio_Filling)

            

    def comboBox_Doc_Fio_Filling(self):
        self.comboBox_Doc_Fio.clear()

        cursor = connection.cursor()

        requets = """SELECT Doc_FIO FROM Doc
                        WHERE Spec = %s"""
        into = [self.comboBox_Doc_Spec.currentText()]
        cursor.execute(requets, into)

        docFIO = cursor.fetchall()

        for i in range(len(docFIO)):
            docFIOStr = ''.join(docFIO[i])
            # self.comboBox = self.comboBoxDoc
            self.comboBox_Doc_Fio.addItem(docFIOStr)

    def onButton_Accept_New_Day(self):

        cursor = connection.cursor()

        requets = """SELECT ID_Doc FROM Doc
                        WHERE   Spec = %s 
                        AND     Doc_FIO = %s"""
        into = [self.comboBox_Doc_Spec.currentText(), self.comboBox_Doc_Fio.currentText()]
        cursor.execute(requets, into)
        docId = cursor.fetchall()

        if self.textEdit_Doc_Date.toPlainText() =='':
            self.label_Doc_Data.setText("Укажите дни приёма!")
            
        else:
            days = self.textEdit_Doc_Date.toPlainText().replace(' ','').replace('\n','').split(',')
            time =  self.timeEdit.time().toString('HH:mm')
            for d in range(len(days)):
                if self.spinBox_Time_Num_Step.value() == 0:
                    self.spinBox_Time_Num_Step.setValue(1)
                for i in range(self.spinBox_Time_Num_Step.value()):
                    time2 = datetime.datetime.strptime(time, '%H:%M') + datetime.timedelta(minutes = self.spinBox_Time_Step.value()*i)
                    
                    
                    requets = """INSERT INTO Appointment(Day_appointment, Time_appointment, ID_Pat, ID_Doc, appointment_status) 
                                VALUES(%s, %s, 1, %s, 0)"""
                    into = [days[d],time2.strftime('%H:%M'),docId[0][0]]
                    cursor.execute(requets, into)
                    connection.commit()
            self.Notice = NoticeDialog(self)
            self.Notice.show()
            self.Notice.label.setText('Новые записи успешно добавленны!')
            # self.Notice.pushButton.clicked.connect()
            self.MainWindow.whoseScheduleIsThis()
                    
class ChooseWhatEdit(QtWidgets.QMainWindow, ChooseWhatEdit.Ui_Form):
    def __init__(self,):
        super().__init__()
        self.setupUi(self)

class NewDocAndSpecWindow(QtWidgets.QMainWindow, NewDocAndSpecWindow.Ui_Form):
    def __init__(self, root):
        super().__init__(root)
        self.setupUi(self)
        
        cursor = connection.cursor()

        self.MainWindow = root
        
        self.pushButton_Accept_New_Doc.clicked.connect(self.onButton_Accept_New_Doc_Check)
        self.pushButton_Accept_New_Spec.clicked.connect(self.onButton_Accept_New_Spec_Check)
        
        requets = """SELECT Spec FROM Doc GROUP BY Spec"""
        cursor.execute(requets)
        docSpec = cursor.fetchall()
        for i in range(len(docSpec)):
            docSpecStr = ''.join(docSpec[i])
            self.comboBox_Doc_Spec.addItem(docSpecStr)

    def onButton_Accept_New_Doc_Check(self):

        cursor = connection.cursor()
        
        if self.textEdit_Doc_Fio.toPlainText() != '':
            
            requets = """INSERT INTO Doc(Doc_FIO,Spec) 
                            VALUES(%s,%s)"""
            into = [self.textEdit_Doc_Fio.toPlainText(), self.comboBox_Doc_Spec.currentText()]
            cursor.execute(requets, into)
            connection.commit()

            requets = """SELECT  Doc_FIO,Spec FROM Doc 
                            WHERE   Doc_FIO = %s
                            AND     Spec = %s"""
            into = [self.textEdit_Doc_Fio.toPlainText(), self.comboBox_Doc_Spec.currentText()]
            cursor.execute(requets, into)
            fillingCheck = cursor.fetchall()

            if len(fillingCheck) != 0:
                self.NoticeDialog = NoticeDialog(self)  
                self.NoticeDialog.show()
                self.Notice = NoticeDialog(self)
                
                self.MainWindow.whoseScheduleIsThis()
            else:
                self.NoticeDialog = NoticeDialog(self)  
                self.NoticeDialog.show()
                self.NoticeDialog.label.setText('Произошла ошибка\nврач не добавлен.')
        else:
            self.pushButton_Accept_New_Doc.setText('Добавить Врача\nВведите ФИО')

    def onButton_Accept_New_Spec_Check(self):
        
        cursor = connection.cursor()
        
        if self.textEdit_New_Spec.toPlainText() != '':
            
            requets = """INSERT INTO Doc(Doc_FIO,Spec) 
                            VALUES(%s,%s)"""
            into = [self.textEdit_Doc_Fio.toPlainText(), self.textEdit_New_Spec.toPlainText()]
            cursor.execute(requets, into)
            connection.commit()

            requets = """SELECT  Doc_FIO,Spec FROM Doc 
                            WHERE   Doc_FIO = %s
                            AND     Spec = %s"""
            into = [self.textEdit_Doc_Fio.toPlainText(), self.textEdit_New_Spec.toPlainText()]
            cursor.execute(requets, into)
            fillingCheck = cursor.fetchall()
            if len(fillingCheck) != 0:
                self.NoticeDialog = NoticeDialog(self)  
                self.NoticeDialog.show()
                self.NoticeDialog.label.setText('Новая специальность и врач \nуспешно добавлен!')
                
                self.MainWindow.whoseScheduleIsThis()

            else:
                self.NoticeDialog = NoticeDialog(self)  
                self.NoticeDialog.show()
                self.NoticeDialog.label.setText('Произошла ошибка\nврач не добавлен.')

        else:
            self.label_Doc_New_Spec.setText('ВВЕДИТЕ новую \nспециальность')

class EditDelitingWindow(QtWidgets.QMainWindow, EditDelitingWindow.Ui_MainWindow):
    def __init__(self,root):
        super().__init__(root)
        self.setupUi(self)
        self.main = root
        
        self.fillingData()
        
        self.pushButton_Del.clicked.connect(self.onButtonDel)
        self.pushButton_Change.clicked.connect(self.onButtonChange)
        self.pushButton_Appoiment.clicked.connect(self.onButtonAppoiment)
        
    def onButtonAppoiment(self):
        self.dialog = QuestionDialog(self)
        self.dialog.show()

        self.dialog.label_Notification.setText('Вы уверены что хотите \nдобавить нового пациента?')
        self.dialog.label_Data.hide()

        self.dialog.buttonBox.accepted.connect(self.newPatient)

    def newPatient(self):
        self.dialog.close()

        cursor = connection.cursor()

        requets = """INSERT INTO Patient_card(Pat_FIO, Phone_num, Pat_Card) 
                                VALUES(%s,%s,%s)"""
        into = [self.textEdit_Pac_Fio.toPlainText(), self.textEditl_Pac_Num.toPlainText(), int(self.checkBox_Appointment.isChecked())]
        cursor.execute(requets, into)

        connection.commit()


        requets = """ SELECT ID_Pat FROM Patient_card
                        WHERE Pat_FIO = %s
                        AND Phone_num = %s
                        AND Pat_Card = %s"""
        into = [self.textEdit_Pac_Fio.toPlainText(), self.textEditl_Pac_Num.toPlainText(), int(self.checkBox_Appointment.isChecked())]
        cursor.execute(requets, into)
        patId = cursor.fetchall()

        requets = """Update Appointment set ID_Pat = %s
                        WHERE ID_appointment = %s"""
        into = [patId[0][0], self.main.dataEditDeliting[4]]
        cursor.execute(requets, into)
        connection.commit()


        requets = """ SELECT ID_Pat FROM Appointment
                        WHERE ID_Pat = %s"""
        into = [patId[0][0]]
        cursor.execute(requets, into)
        patId = cursor.fetchall()

        self.NoticeDialog = NoticeDialog(self)
        self.NoticeDialog.show()
        self.NoticeDialog.label.setText('Данные пациента успешно изменены!')
        self.NoticeDialog.pushButton.clicked.connect(self.NoticeDialog.closeParent)
        self.main.whoseScheduleIsThis()

    def onButtonChange(self):
        self.dialog = QuestionDialog(self)
        self.dialog.show()

        self.dialog.label_Notification.setText('Вы уверены что хотите применить изменения?')
        self.dialog.label_Data.hide()

        self.dialog.buttonBox.accepted.connect(self.changePatient)

    def changePatient(self):

        cursor = connection.cursor()

        self.dialog.close()

        requets = """ Update Patient_card set Pat_FIO  = %s, Phone_num = %s, Pat_Card = %s 
                        WHERE ID_Pat = (SELECT ID_Pat FROM Appointment
                                        WHERE ID_appointment = %s)"""
        into = [self.textEdit_Pac_Fio.toPlainText(), self.textEditl_Pac_Num.toPlainText(), int(self.checkBox_Appointment.isChecked()), self.main.dataEditDeliting[4]]
        cursor.execute(requets, into)
        connection.commit()

        self.NoticeDialog = NoticeDialog(self)
        self.NoticeDialog.show()
        self.NoticeDialog.label.setText('Данные пациента успешно изменены!')
        self.NoticeDialog.pushButton.clicked.connect(self.NoticeDialog.closeParent)
        self.main.whoseScheduleIsThis()

    def onButtonDel(self):
        self.dialog = QuestionDialog(self)
        self.dialog.show()
        self.dialog.label_Notification.setText("Вы уверены что хотите удалить запись?")
        self.dialog.label_Data.hide()
        self.dialog.buttonBox.accepted.connect(self.deletingAppoinment)
        
    def deletingAppoinment(self):

        cursor = connection.cursor()

        self.dialog.close()

        requets = """ Update Appointment set ID_Pat = 1 ,appointment_status = 0 
                        WHERE ID_appointment = %s"""
        into = [self.main.dataEditDeliting[4]]
        cursor.execute(requets, into)
        connection.commit()

        requets = """ SELECT appointment_status FROM Appointment
                        WHERE ID_appointment = %s"""
        into = [self.main.dataEditDeliting[4]]
        cursor.execute(requets, into)
        check = cursor.fetchall()

        self.NoticeDialog = NoticeDialog(self)
        self.NoticeDialog.show()

        if check[0][0] == 0:
            
            self.NoticeDialog.label.setText('Запись удалена!')
            self.NoticeDialog.pushButton.clicked.connect(self.NoticeDialog.closeParent)
            self.main.whoseScheduleIsThis()
        else:
            self.NoticeDialog.label.setText('Произошла ошибка')
            self.NoticeDialog.pushButton.clicked.connect(self.NoticeDialog.closeParent)

    def fillingData(self):

        self.labelStatus.setText('')

        self.Num_Fio_Pac = self.main.dataEditDeliting[3].split("\n")
        self.Num_Fio_Pac[1] = self.Num_Fio_Pac[1].replace('+ ','').replace('- ','')
        self.label_Date_Day.setText(self.main.dataEditDeliting[0])
        self.label_Date_Time.setText(self.Num_Fio_Pac[0])
        self.label_doc_fio.setText(self.main.dataEditDeliting[2])
        self.label_spec.setText(self.main.dataEditDeliting[1])

        self.textEdit_Pac_Fio.setText(self.Num_Fio_Pac[1])
        self.textEditl_Pac_Num.setText(self.Num_Fio_Pac[2])

        cursor = connection.cursor()
        
        requets = """SELECT ID_Pat, Pat_FIO, Phone_num, Pat_Card FROM Patient_card
                            WHERE ID_Pat = (SELECT ID_Pat FROM Appointment 
                                            WHERE ID_appointment = %s);"""
        into = [self.main.dataEditDeliting[4]]
        cursor.execute(requets, into)
        CurrentData = cursor.fetchall()
        
        if CurrentData[0][3] == 1:
            self.checkBox_Appointment.setCheckState(2)
        elif CurrentData[0][3] == 0:
            self.checkBox_Appointment.setCheckState(0)

class DelDay(QtWidgets.QDialog, DelDocOrDay.Ui_Form):
    def __init__(self, root):
        super().__init__(root)

        self.setupUi(self) 

        self.MainWindow = root 
        self.label_Up.setText('Выберете врача')
        self.label_Down.setText('Введите дату и время в \nформате: дд.мм.гггг чч.мм')
        
        cursor = connection.cursor()
        requets = """SELECT ID_Doc, Spec, Doc_FIO FROM Doc
                            ORDER BY Spec"""
        cursor.execute(requets)
        DocData = cursor.fetchall()
        
        for i in range(len(DocData)):
            text = "{0} - {1}".format(DocData[i][1], DocData[i][2])
            self.comboBox.addItem(text)
        self.pushButton_Accept.clicked.connect(self.DelDayCheck)

    def DelDayCheck(self):

        text = self.textEdit.toPlainText().split(' ')
        docId = self.comboBox.currentText().split('.')

        self.NoticeDialog = NoticeDialog(self)
        self.NoticeDialog.show()

        cursor = connection.cursor()

        if len(text) == 2:

            requets = """ SELECT ID_appointment FROM Appointment
                                WHERE ID_doc = %s
                                AND Day_appointment = %s
                                AND Time_appointment = %s"""
            into = [docId[0], text[0], text[1]]
            cursor.execute(requets, into)
            self.foundAppoinment = cursor.fetchall()

            if self.foundAppoinment == []:
                self.NoticeDialog.label.setText('Запись не найдена!')
                
            elif len(self.foundAppoinment) > 1:
                self.NoticeDialog.label.setText('Ошибка!\nОбнаружено несколько записей!')

            elif len(self.foundAppoinment) == 1:
                self.NoticeDialog.close()
                self.QuestionDialog = QuestionDialog(self)
                self.QuestionDialog.label_Notification.setText("Вы точно хотите удалить запись?")
                self.QuestionDialog.label_Data.hide()
                self.QuestionDialog.show()
                
                self.QuestionDialog.buttonBox.accepted.connect(self.DelAppoinment)

        else:
            
            self.NoticeDialog.label.setText('Ошибка ввода даты')
    
    def DelAppoinment(self):

        cursor = connection.cursor()

        requets = """DELETE FROM Appointment
                                    WHERE ID_appointment = %s"""
        into = [self.foundAppoinment[0][0]]
        cursor.execute(requets, into)
        connection.commit()

        self.NoticeDialog = NoticeDialog(self)
        self.MainWindow.whoseScheduleIsThis()
        self.NoticeDialog.show()
        self.NoticeDialog.label.setText('Запись удалена!')

class DelDoc(QtWidgets.QDialog, DelDocOrDay.Ui_Form):
    def __init__(self, root):
        super().__init__(root)

        self.setupUi(self) 

        self.MainWindow = root 

class MainWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        # self.showFullScreen()

        self.label_date.setText(datetime.datetime.today().strftime('%d.%m.%Y')) 
        # self.setWindowIcon(QtGui.QIcon('icon.png'))
        
        self.weekdayDefining()
        self.showMaximized() 
        
        self.firstFilling()

        self.pushButtonLeftDay.clicked.connect(self.onLeftDayButton)
        self.pushButtonRightDay.clicked.connect(self.onRightDayButton)
        self.pushButtonLeftWeek.clicked.connect(self.onLeftWeekButton)
        self.pushButtonRightWeek.clicked.connect(self.onRightWeekButton)

        self.pushButtonSearchAppointment.clicked.connect(self.onButtonNewRes)
        self.pushButtonUpdateTable.clicked.connect(self.whoseScheduleIsThis)
        self.pushButtonDateChoose.clicked.connect(self.onButtonDateChoose)
        self.pushButtonEditAppointment.clicked.connect(self.onButtonEditAppointment)
        
        self.pushButtonUpdateRes.clicked.connect(self.onButtonUpdateRes)
        self.tableWidget.selectionModel().selectionChanged.connect(self.onSelectionChanged)

        self.pushButtonChangeAppointmentGreen.clicked.connect(self.onChangeAppointmentGreenButton)
        self.pushButtonChangeAppointmentBlue.clicked.connect(self.onChangeAppointmentBlueButton)

        self.pushButtonDocSearch.clicked.connect(self.onButtonDocSearch)
        self.pushButtonNewDoc.clicked.connect(self.onChooseWhatEdit)

        self.pushButtonPatientSearch.clicked.connect(self.onButtonPatientSearch)


    def onButtonDateChoose(self):
        self.DateChoose = DateChoose(self)
        self.DateChoose.show()

        # self.DateChoose.pushButton.clicked.connect(self.setDate(self.DateChoose.dateEdit.text()))

    def setDate(self,ourDate):
        
        self.label_date.setText(ourDate)
        self.weekdayDefining()
        self.tableFillSpec()

    def onButtonPatientSearch(self):
        self.PatientSearch = PatientSearch(self)
        self.PatientSearch.show()
        w
        self.PatientSearch.pushButtonSearch.clicked.connect(lambda: self.patientSearch(self.PatientSearch.textEdit.toPlainText()))

    def patientSearch(self,pat_name):

        self.pushButtonLeftDay.setEnabled(False)
        self.pushButtonRightDay.setEnabled(False)
        self.pushButtonLeftWeek.setEnabled(False)
        self.pushButtonRightWeek.setEnabled(False)
        self.label_date.setEnabled(False) 
        self.label_weekday.setEnabled(False)
        self.pushButtonUpdateRes.setEnabled(False)
        self.pushButtonNewDoc.setEnabled(False)
        self.PatientSearch.close()
        
        self.tableWidget.clear()

        self.label_date.text()

        cursor = connection.cursor()

        requets = """ SELECT Day_appointment, ID_Doc, ID_Pat FROM Appointment
                            WHERE ID_Pat = (SELECT ID_Pat FROM Patient_card
                                                WHERE Pat_FIO = %s)
                            GROUP BY Day_appointment, ID_Doc, ID_Pat
                            ORDER BY Day_appointment ASC"""
        into = [pat_name]
        cursor.execute(requets, into)
        Pac_Data_From = cursor.fetchall()
        
        Pac_Data_From_SQL=[]

        current_date = date.today() - datetime.timedelta(days = 182)
        for i in range(len(Pac_Data_From)):
            if datetime.datetime.strptime(Pac_Data_From[i][0], '%d.%m.%Y').date() >= current_date:
                Pac_Data_From_SQL.append(Pac_Data_From[i])

        for i in range(len(Pac_Data_From_SQL)):
            
            item = QTableWidgetItem()
            self.tableWidget.setItem(0, i, QtWidgets.QTableWidgetItem(Pac_Data_From_SQL[i][0]))

            requets = """ SELECT Spec, Doc_FIO, ID_Doc FROM Doc
                            WHERE ID_Doc = %s
                                ORDER BY Spec ASC"""
            into = [Pac_Data_From_SQL[i][1]]
            cursor.execute(requets, into)
            Doc_Data_From_SQL = cursor.fetchall()

            self.tableWidget.setItem(1, i, QtWidgets.QTableWidgetItem(str(Doc_Data_From_SQL[0][0])))
            self.tableWidget.setItem(2, i, QtWidgets.QTableWidgetItem(str(Doc_Data_From_SQL[0][1])))

            


            requets = """SELECT ID_appointment,Time_appointment,appointment_status,ID_Pat FROM Appointment
                            WHERE ID_Doc = %s
                            AND Day_appointment = %s
                            AND ID_Pat = %s
                            ORDER BY Time_appointment;"""
            into = [Doc_Data_From_SQL[0][2], Pac_Data_From_SQL[i][0], Pac_Data_From_SQL[i][2]]
            cursor.execute(requets, into)

            CurrentData = cursor.fetchall()
            # ID_appointment,Time_appointment,appointment_status,ID_Pat # 
            #       0               1               2               3   # 
            
            
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
                self.tableWidget.setItem(j+3, i, item)

    def enableWidget(self):
        self.pushButtonLeftDay.setEnabled(True)
        self.pushButtonRightDay.setEnabled(True)
        self.pushButtonLeftWeek.setEnabled(True)
        self.pushButtonRightWeek.setEnabled(True)
        self.label_date.setEnabled(True) 
        self.label_weekday.setEnabled(True)
        self.pushButtonUpdateRes.setEnabled(True)
        self.pushButtonNewDoc.setEnabled(True)

    # def onButtonSearchPat(self):
    #     print("asdasd")
    #     pat_name = 'Pat 85'
    #     self.tableWidget.clear()
    #     cur.execute(""" SELECT Day_appointment FROM Appointment
    #                         WHERE ID_Pat = (SELECT ID_Pat FROM Patient_card
    #                                             WHERE Pat_FIO = (?))
    #                         GROUP BY Day_appointment""",(pat_name,))
    #     Pac_Data_From_SQL = cur.fetchall()

    #     for i in range(len(Pac_Data_From_SQL)):
    #         cur.execute(""" SELECT Time_appointment, ID_Doc FROM Appointment
    #                         WHERE ID_Pat = (SELECT ID_Pat FROM Patient_card
    #                                             WHERE Pat_FIO = (?))
    #                         ORDER BY Time_appointment ASC""",(pat_name,))
            
    #         Time_appointment = cur.fetchall()

            

    #         item2 = QTableWidgetItem()
    #         item2.setText(Pac_Data_From_SQL[0][0])
    #         self.tableWidget.setItem(0, i, item2)

            

    #         for j in range(len(Time_appointment)):
    #             item = QTableWidgetItem()
                 
    #             if len(Time_appointment)+2 > self.tableWidget.rowCount():
    #                 self.tableWidget.setRowCount(len(Time_appointment)+2)

    #             cur.execute(""" SELECT Doc_FIO,Spec FROM Doc
    #                         WHERE ID_Doc = (?)""",(Time_appointment[j][1],))
            
    #             doc_Fio_Spec = cur.fetchall()
                

    #             item.setText('Время - {0}\nВрач - {1}\nСпециальность - {2}'.format(Time_appointment[j][0], doc_Fio_Spec[0][0], doc_Fio_Spec[0][1]))
    #             self.tableWidget.setItem(j+2, i, item)

    def onChooseWhatEdit(self):
        self.ChooseWhatEdit = ChooseWhatEdit()  
        self.ChooseWhatEdit.show()

        self.ChooseWhatEdit.pushButton_New_Appoinment.clicked.connect(self.ChooseWhatEditonButtonNewAppoinment)
        self.ChooseWhatEdit.pushButton_New_Doc.clicked.connect(self.ChooseWhatEditonButtonNewDoc)
        self.ChooseWhatEdit.pushButton_Del_Doc.clicked.connect(self.ChooseWhatEditonButtonDelDoc)
        self.ChooseWhatEdit.pushButton_Del_Appoinment.clicked.connect(self.ChooseWhatEditonButtonDelAppoinment)

    def ChooseWhatEditonButtonNewDoc(self):
        self.NewDocAndSpecWindow = NewDocAndSpecWindow(self)  
        self.NewDocAndSpecWindow.show()
        self.ChooseWhatEdit.close()

    def ChooseWhatEditonButtonDelDoc(self):
        self.DelDoc = DelDoc(self)  
        self.DelDoc.show()
        self.ChooseWhatEdit.close()

    def ChooseWhatEditonButtonDelAppoinment(self):
        self.DelDay = DelDay(self)  
        self.DelDay.show()
        self.ChooseWhatEdit.close()

    def ChooseWhatEditonButtonNewAppoinment(self):
        self.NewAppoimentDayWindow = NewAppoimentDayWindow(self)  
        self.NewAppoimentDayWindow.show()
        self.ChooseWhatEdit.close()

    def onButtonEditAppointment(self):
        
        if self.tableWidget.currentItem() == None:
            self.pushButtonEditAppointment.setText('Ячейка пуста')
        else:

            Sell_Data_Str = self.tableWidget.item(self.tableWidget.currentRow(), self.tableWidget.currentColumn() ).text()
            Sell_Data_Split_Str = Sell_Data_Str.split("\n")  

            if Sell_Data_Split_Str[1] != '- Свободно':
                self.dataEditDeliting = [
                    self.label_date.text(), 
                    self.tableWidget.item(0, self.sel_col ).text(), 
                    self.tableWidget.item(1, self.sel_col ).text(), 
                    self.tableWidget.item(self.tableWidget.currentRow(), self.tableWidget.currentColumn() ).text(),
                    self.tableWidget.item(self.tableWidget.currentRow(), self.tableWidget.currentColumn() ).statusTip()
                    ]
                self.EditDelitingWindow = EditDelitingWindow(self)
                self.EditDelitingWindow.show()
            else:
                self.pushButtonEditAppointment.setText('Ячейка свободна')
                
    def onButtonDocSearch(self):
        self.DocFilther = DocFilther(self)  
        self.DocFilther.show()
        
    def onSelectionChanged(self, selected, deselected):	
        for ix in selected.indexes():
            self.pushButtonUpdateRes.setText("Записать пациента в\nпустую ячейку")
            self.pushButtonChangeAppointmentGreen.setText('Изменить \nстатус \nприёма')
            self.pushButtonChangeAppointmentBlue.setText('Изменить \nстатус \nприёма')
            self.pushButtonEditAppointment.setText("Редактирование/удаление\nзаписи")
            self.sel_row=ix.row()
            self.sel_col=ix.column()

    def onButtonUpdateRes(self, selected):
        
        if self.tableWidget.currentItem() == None:
            self.pushButtonUpdateRes.setText('Ячейка пуста')
        else:

            self.Sell_Data_Str = self.tableWidget.item(self.tableWidget.currentRow(), self.tableWidget.currentColumn() ).text()
            self.Sell_Data_Split_Str = self.Sell_Data_Str.split("\n")  
            
            if self.Sell_Data_Split_Str[1] != '- Свободно':
                self.pushButtonUpdateRes.setText('Записать пациента в ПУСТУЮ\n ячейку')
            else:
                self.ourDate=self.label_date.text()
                self.Doc_Spec = self.tableWidget.item(0, self.sel_col ).text()
                self.Doc_Fio = self.tableWidget.item(1, self.sel_col ).text()
                self.Sell_Data = self.tableWidget.item(self.tableWidget.currentRow(), self.tableWidget.currentColumn() ).text()
                self.newAppointmentCellWindow = newAppointmentCellWindow(self)
                self.newAppointmentCellWindow.show()

    def onChangeAppointmentGreenButton(self):
        
        if self.tableWidget.currentItem() == None:
            self.pushButtonChangeAppointmentGreen.setText('Ячейка пуста')
        else:

            Sell_Data_Str = self.tableWidget.item(self.tableWidget.currentRow(), self.tableWidget.currentColumn() ).text()
            Sell_Data_Split_Str = Sell_Data_Str.split("\n")  
            
            if len(Sell_Data_Split_Str) < 2:
                self.pushButtonChangeAppointmentGreen.setText('Ячейка свободна')
            elif Sell_Data_Split_Str[1] == '- Свободно':
                self.pushButtonChangeAppointmentGreen.setText('Ячейка свободна')
            elif self.tableWidget.item(self.tableWidget.currentRow(), self.tableWidget.currentColumn()).background().color().getRgb() == (163, 198, 192, 255):
                self.pushButtonChangeAppointmentGreen.setText('Уже установленно\n состояние запись\nне подтверждена')
            else:
                self.AppointmentCollor = "'запись не подтверждена'"
                self.dialog = QuestionDialog(self)
                self.dialog.show()
                
                self.dialog.label_Notification.setText(self.dialog.label_Notification.text() + self.AppointmentCollor)
                self.dialog.label_Data.setText(self.dialog.label_Data.text() + self.tableWidget.item(self.tableWidget.currentRow(), self.tableWidget.currentColumn() ).text())
                self.dialog.buttonBox.accepted.connect(self.onChangeAppointmentColor)

    def onChangeAppointmentBlueButton(self):
        if self.tableWidget.currentItem() == None:
            self.pushButtonChangeAppointmentBlue.setText('Ячейка пуста')
        else:

            Sell_Data_Str = self.tableWidget.item(self.tableWidget.currentRow(), self.tableWidget.currentColumn() ).text()
            Sell_Data_Split_Str = Sell_Data_Str.split("\n")  

            if len(Sell_Data_Split_Str) < 2:
                self.pushButtonChangeAppointmentBlue.setText('Ячейка свободна')
            elif Sell_Data_Split_Str[1] == '- Свободно':
                self.pushButtonChangeAppointmentBlue.setText('Ячейка свободна')
            elif self.tableWidget.item(self.tableWidget.currentRow(), self.tableWidget.currentColumn()).background().color().getRgb() == (98, 111, 222, 255):
                self.pushButtonChangeAppointmentBlue.setText('Уже установленно \nсостояние \nзапись подтверждена')
            else:
                self.AppointmentCollor = "'запись подтверждена'"
                self.dialog = QuestionDialog(self)
                self.dialog.show()
                
                self.dialog.label_Notification.setText(self.dialog.label_Notification.text() + self.AppointmentCollor)
                self.dialog.label_Data.setText(self.dialog.label_Data.text() + self.tableWidget.item(self.tableWidget.currentRow(), self.tableWidget.currentColumn() ).text())
                self.dialog.buttonBox.accepted.connect(self.onChangeAppointmentColor)

    def onChangeAppointmentColor(self):
        
        if self.AppointmentCollor == "'запись подтверждена'":
            appointment_Status = 2
        elif self.AppointmentCollor == "'запись не подтверждена'":
            appointment_Status = 1

        appointment_Id = self.tableWidget.item(self.tableWidget.currentRow(), self.tableWidget.currentColumn()).statusTip()

        cursor = connection.cursor()
        requets = """ UPDATE Appointment set appointment_status = %s
                        WHERE ID_appointment = %s"""
        into = [appointment_Status, appointment_Id]
        cursor.execute(requets, into)
        connection.commit()
        self.whoseScheduleIsThis()

    def onButtonNewRes(self):
        self.SearchFreeAppointment = SearchFreeAppointment(self)
        self.SearchFreeAppointment.show()

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
        cursor = connection.cursor()
        cursor.execute("SELECT Spec FROM Doc GROUP BY Spec;")

        self.doc_spec = cursor.fetchall()
        self.whatYouNeed = [0] + self.doc_spec
        
        self.whoseScheduleIsThis()

    def whoseScheduleIsThis(self):
        cursor = connection.cursor()
        if self.whatYouNeed[0] == 0:

            self.docFIO = []
            for i in range(len(self.whatYouNeed)-1):

                request = """ SELECT Doc_FIO , Spec FROM Doc
                                WHERE Spec = %s
                                ORDER BY ID_Doc ASC"""

                into = self.whatYouNeed[i+1]
                cursor.execute(request, into)
                # docFioTmp = cursor.fetchall()
                self.docFIO = self.docFIO + cursor.fetchall()
                
            self.tableFillSpec()
            
        elif self.whatYouNeed[0] == 1:
            
            self.docFIO = self.whatYouNeed
            self.docFIO.pop(0)
            
            self.tableFillSpec()
            self.whatYouNeed = [1] + self.whatYouNeed
        else:
            self.firstFilling()

    def tableFillSpec(self):
        cursor = connection.cursor()
        self.enableWidget()
        self.tableWidget.clear()
        ourDate = self.label_date.text()
        self.tableWidget.setRowHeight(0, 30)
        self.tableWidget.setRowHeight(1, 30)

        for i in range(len(self.docFIO)):
            
            self.tableWidget.setColumnWidth(i, 220)
            
            self.tableWidget.setItem(0, i, QtWidgets.QTableWidgetItem(str(self.docFIO[i][1])))
            self.tableWidget.setItem(1, i, QtWidgets.QTableWidgetItem(str(self.docFIO[i][0])))
           
            # ↓ забиваем ячейки в столбце
            # ↓ запрос на выдачу ID приёмов
            request = """SELECT ID_appointment,Time_appointment,appointment_status,ID_Pat FROM Appointment
                            WHERE ID_Doc = (SELECT ID_Doc FROM Doc WHERE Doc_FIO = %s)
                            AND Day_appointment = %s
                            ORDER BY Time_appointment;"""
            into = (self.docFIO[i][0], ourDate)
            cursor.execute(request, into)

            # ID_appointment,Time_appointment,appointment_status,ID_Pat # 
            #       0               1               2               3   # 
            CurrentData = cursor.fetchall()
            for j in range(len(CurrentData)):
                item = QTableWidgetItem()
                self.tableWidget.setRowHeight(j+2, 150)
 
 
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
                
class NoticeDialog(QtWidgets.QDialog, NoticeDialog.Ui_Dialog):
    def __init__(self,root):
        super().__init__(root)
        self.setupUi(self)
        self.main = root
        self.pushButton.clicked.connect(lambda:self.close())
    def closeParent(self):
        self.close()
        self.main.close()
        
class LogWindow(QtWidgets.QMainWindow, LogWindow.Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self) 
        self.pushButton.clicked.connect(self.authorization)
    def authorization(self):



        global connection
        try:
            connection = connect(
                host="localhost",
                user=self.lineEdit_username.text(),
                password=self.lineEdit_password.text(),
                # user="admin",
                # password="klinika",
                database="asormo",
            )
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