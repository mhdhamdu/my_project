import mysql.connector
from datetime import datetime


class employeemanager():
    def __init__(self):
     try:
        self.connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="MuHamdammed@77",
            database="company_db"
        )
     except Exception as e:
         print(e)
