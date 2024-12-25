import sqlite3 as sql
import pandas as pd

import sys
from PyQt5 import QtWidgets, uic

connection = sql.connect('Database_rasp.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Group1 (
id INTEGER PRIMARY KEY,
tt TEXT NOT NULL
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS Group2 (
id INTEGER PRIMARY KEY,
tt TEXT NOT NULL
);
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS Group3 (
id INTEGER PRIMARY KEY,
tt TEXT NOT NULL
)
''')

for i in range(1, 31):
        cursor.execute('INSERT INTO Group1 (tt) VALUES (?)', ("0"))
        cursor.execute('INSERT INTO Group2 (tt) VALUES (?)', ("0"))
        cursor.execute('INSERT INTO Group3 (tt) VALUES (?)', ("0"))

connection.commit()
connection.close()