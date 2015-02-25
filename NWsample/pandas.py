import sqlite3
conn = sqlite3.connect('Northwind.db')

c = conn.cursor()

sql = "select city from customers" 

c.execute(sql)