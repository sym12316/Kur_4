import sys 
import sqlite3 
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import MainWindow_2 as MainWindow
from functools import partial
from PyQt5.QtCore import Qt

import datetime
from datetime import date
current_date = datetime.datetime.today()
past_date = datetime.datetime.today() + datetime.timedelta(days=-20)

print(past_date)

lol = datetime.datetime.today() + datetime.timedelta(days=-6)
Date = lol.strftime('%d.%m.%Y') 
print(Date)


conn = sqlite3.connect(r'DB/SAR.DB')
cur = conn.cursor()
# data = ['table']

docFIOStr = 'Иванов А.А.'
time = ['9:30','10:00']
cur.execute("""SELECT ID_appointment FROM Appointment 
WHERE Time_appointment = (?) 
AND (ID_Doc = (SELECT ID_Doc FROM Doc WHERE Doc_FIO = (?))
AND Day_appointment = (?));""",(time[1],docFIOStr,Date,))
appointmentPac = cur.fetchall()

print(appointmentPac)