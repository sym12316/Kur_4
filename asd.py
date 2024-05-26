import sys 
import sqlite3 
import datetime
import configparser
import hashlib
from datetime import date
import mysql.connector

from getpass import getpass
from mysql.connector import connect, Error

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt

from UI import UI_LogWindow as LogWindow
from UI import UI_MainWindow as MainWindow


try:
    with connect(
        host="localhost",
        user="admin",
        password="klinika",

        # user=self.lineEdit_username.text(),
        # password=self.lineEdit_password.text(),
        
        database="asormo",
    ) as connection:
        global cursor 
        cursor = connection.cursor()
        cursor = connection.cursor()
        
        pat_name = "Казакова Ирина Петровна"

        requets = """ SELECT Day_appointment, ID_Doc, ID_Pat FROM Appointment
                            WHERE ID_Pat = (SELECT ID_Pat FROM Patient_card
                                                WHERE Pat_FIO = %s)
                            GROUP BY Day_appointment, ID_Doc
                            ORDER BY Day_appointment ASC"""
        into = [pat_name]
        cursor.execute(requets, into)
        Pac_Data_From = cursor.fetchall()
        print("\n",Pac_Data_From)



        

except Error as e:
    print(e)
    


def asd():
    requets = """%s"""
    into = []
    cursor.execute(requets, into)
    result = cursor.fetchall()
    print(result)
    connection.commit()


    cursor = connection.cursor()

cursor = connection.cursor()
requets = """ UPDATE Appointment set appointment_status = %s
                        WHERE ID_appointment = %s"""
                        into = [appointment_Status, appointment_Id]
    cursor.execute(requets, into)
connection.commit()


