import sqlite3


def write_table(db=None, table=None, filepath=None):
    """Populate a table in db given a csv file.  All parameters are strings."""
    
    if not db.endswith('.db'):
        db += '.db'

    conn = sqlite3.connect(db)
    c = conn.cursor() #context in which you execute sql commands 

    c.execute('drop table if exists %s' % table) # delete table from db, if exists, otherwise create table will fail

    sqlcreate_format = 'CREATE TABLE ' + table + ''' (%s CHAR default "", %s integer default 0, %s CHAR default "", %s CHAR default "")'''

    sql = "INSERT INTO %s VALUES (?, ?, ?, ?)" % table #sqlite formatter will insert values from tuple

    lineno = 0
    with open(filepath) as csvfile:
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


def titanic_data():
    """Specific case for titanic data"""
    write_table(db='titanic.db', table='passengers', filepath='ch03_titanic.csv')


