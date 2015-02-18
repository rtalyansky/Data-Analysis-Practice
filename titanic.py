import sqlite3

conn = sqlite3.connect('titanic.db')
c = conn.cursor() #context in which you execute sql commands 

c.execute('drop table if exists passengers')

sqlcreate_format = '''CREATE TABLE passengers (%s CHAR default "", %s integer default 0, %s CHAR default "", %s CHAR default "")'''

sql = "INSERT INTO passengers VALUES (?, ?, ?, ?)" #sqlite formater that you can insert tuple of values 
#executemany lets you insert multiple tupls 

lineno = 0
with open('ch03_titanic.csv') as csvfile:
    for row in csvfile: #reads line by line 
        lineno += 1
        r = row.strip().split(',') #strip eliminates line ends/spaces, split makes a list  
        t = tuple(r) 
        if lineno == 1: #only the first line in special 
            sqlcreate = sqlcreate_format % t #tuple 
            #print(sqlcreate)
            c.execute(sqlcreate)
        else:
            #print(t)
            #print(sql)
            c.execute(sql, t) 

conn.commit()
conn.close()