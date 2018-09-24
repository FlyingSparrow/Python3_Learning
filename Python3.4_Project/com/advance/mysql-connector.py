#!/usr/bin/python3

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root123456"
)

print(mydb)

print()
print()
print("Create database demo")

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE runoob_db")
