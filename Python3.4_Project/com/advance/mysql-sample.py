#!/usr/bin/python3

import pymysql

db = pymysql.connect("localhost", "root", "root123456", "mysql")

cursor = db.cursor()

cursor.execute("select version()")

data = cursor.fetchone()

print("Database version: %s " % data)

db.close()