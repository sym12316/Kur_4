import sys 
import sqlite3 
import datetime
import configparser
from datetime import date
from datetime import timedelta

c = '15.10.2024'
b = datetime.datetime.strptime(c, '%d.%m.%Y')
# timedelta (Month = 6)
a = date.today()
# d = 
print(a)
print(a - timedelta(days = 182))