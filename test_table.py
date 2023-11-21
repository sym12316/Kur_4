import sys 
import sqlite3 
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import MainWindow_2 as MainWindow
from functools import partial
from PyQt5.QtCore import Qt

import datetime
from datetime import date
# current_date = datetime.datetime.today()
# past_date = datetime.datetime.today() + datetime.timedelta(days=-20)

# print(past_date)

lol = datetime.datetime.today() + datetime.timedelta(days=-5)
Date = lol.strftime('%d.%m.%Y')
print('date 1',Date)

Date2 = datetime.datetime.strptime(Date, '%d.%m.%Y') + datetime.timedelta(days=5)
print('date 2',Date2)

Date3 = Date2.strftime('%d.%m.%Y') 
print('date 3',Date3)

#### ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ####

# conn = sqlite3.connect(r'DB/SAR.DB')
# cur = conn.cursor()
# # data = ['table']
# # ?asdsadasdsda
# docFIOStr = 'Иванов А.А.'
# time = ['9:30','10:00']
# cur.execute("""SELECT ID_appointment FROM Appointment 
# WHERE Time_appointment = (?) 
# AND (ID_Doc = (SELECT ID_Doc FROM Doc WHERE Doc_FIO = (?))
# AND Day_appointment = (?));""",(time[1],docFIOStr,Date,))

# outCurrentData = cur.fetchall()
# print(outCurrentData)


# # outCurrentDataStr = ''.join(outCurrentData[0][1])

# i=0
# print(len(outCurrentData))
# if len(outCurrentData) > 0:
#     outCurrentDataStr2 = int(''.join(map(str,outCurrentData[0])))
#     print(outCurrentDataStr2)
# else:
#     print ('empty')
# # if outCurrentData > 0:
# #     print ('1')

# # else:
# #     print('2')


# # cur.execute("""SELECT Pat_FIO FROM Patient_card
# # WHERE (ID_Pat = (SELECT ID_Pat FROM Appointment
# # WHERE ID_appointment = (?)))""",(outCurrentDataStr2,))
# # a1 = cur.fetchall()
# # a2 = ''.join(a1[0])
# # print('Пациент', a2)



# # cur.execute("""SELECT appointment_status FROM Appointment                      
# # WHERE ID_appointment = (?)""",(outCurrentDataStr2,))
# # b1 = cur.fetchall()
# # b2 = int(''.join(map(str,b1[0])))
# # print('статус',b2)




# # outCurrentDataStr = ''.join(outCurrentData[0])

# # print(outCurrentDataStr)