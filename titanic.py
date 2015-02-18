import sqlite3

conn = sqlite3.connect('titanic.db')
c = conn.cursor() #context in which you execute sql commands 

c.execute('drop table if exists passengers') # delete table from db, if exists, otherwise create table will fail

sqlcreate_format = '''CREATE TABLE passengers (%s CHAR default "", %s integer default 0, %s CHAR default "", %s CHAR default "")'''

sql = "INSERT INTO passengers VALUES (?, ?, ?, ?)" #sqlite formatter will insert values from tuple

lineno = 0
with open('ch03_titanic.csv') as csvfile:
    for row in csvfile: #reads line by line
        lineno += 1
        r = row.strip().split(',') #strip eliminates line ends/spaces, split separates input line by commas, makes a list
        t = tuple(r) # produce tuple out of a list, to pass it to format statement
        if lineno == 1: #first line is special: contains names of columns
            sqlcreate = sqlcreate_format % t #tuple 
            #print(sqlcreate)
            c.execute(sqlcreate)
        else: # rest of the lines are data rows
            #print(t)
            #print(sql)
            c.execute(sql, t) 
            #executemany lets you insert multiple tuples 

conn.commit()
conn.close()

