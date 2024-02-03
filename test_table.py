import sys 
import sqlite3 
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
# import MainWindow_2 as MainWindow
from functools import partial
from PyQt5.QtCore import Qt

import datetime
from datetime import date
# current_date = datetime.datetime.today()
# past_date = datetime.datetime.today() + datetime.timedelta(days=-20)

# print(past_date)

# lol = datetime.datetime.today() + datetime.timedelta(days=-5)
# Date = lol.strftime('%d.%m.%Y')
# print('date 1',Date)

# Date2 = datetime.datetime.strptime(Date, '%d.%m.%Y') + datetime.timedelta(days=5)
# print('date 2',Date2)

# Date3 = Date2.strftime('%d.%m.%Y') 
# print('date 3',Date3)

#### ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ####

conn = sqlite3.connect(r'DB/SAR.DB')
cur = conn.cursor()
Date = "28.11.2023"
# data = ['table']
# # ?asdsadasdsda
docFIOStr = 'Иванов А.А.'
# time = ['9:30','10:00']
cur.execute("""SELECT ID_appointment,Time_appointment,appointment_status FROM Appointment 
WHERE (ID_Doc = (SELECT ID_Doc FROM Doc WHERE Doc_FIO = (?))
AND Day_appointment = (?)) ORDER BY Time_appointment;""",(docFIOStr,Date,))

outCurrentData = cur.fetchall()
# print(outCurrentData[1][1])
# print(len(outCurrentData))
asd = outCurrentData[1][0]
print(outCurrentData)

# for x in range(len(outCurrentData)):
#     asd = ('------\n{0}|\n{1}-{2} |'.format(outCurrentData[x][1], outCurrentData[x][0],outCurrentData[x][2]))
#     print(asd)
# print('------')

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