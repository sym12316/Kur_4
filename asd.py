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
        requets = """SELECT Spec FROM Doc GROUP BY Spec"""
        cursor.execute(requets)
        result = cursor.fetchall()
        print(result)



        

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




requets = """SELECT ID_Pat, Pat_FIO, Phone_num, Pat_Card FROM Patient_card
                WHERE ID_Pat = (SELECT ID_Pat FROM Appointment 
                                WHERE ID_appointment = (?));"""
into = [self.main.dataEditDeliting[4]]
cursor.execute(requets, into)
CurrentData = cursor.fetchall()
