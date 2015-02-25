import sqlite3 

def try_fetchone(cursor):
	count = 0
	while (True):
		r = cursor.fetchone()
		if r == None:
			break
		else:
			count += 1
			print ("Row %d:" % count), r

dbconn = sqlite3.connect ('Northwind.db') 

dbconn.text_factory = bytes

cursor = dbconn.cursor()

sql = "select * from customers" 

cursor.execute(sql)
try_fetchone(cursor)

cursor.close()
dbconn.close()

#import plotly.plotly as py
from plotly.graph_objs import *

trace1 = Scatter(
     x=df['City'],
     y=df['CustomerID'],
     text=country_names,
     mode='markers'
)
layout = Layout(
     xaxis=XAxis( title='Life Expectancy' ),
     yaxis=YAxis( type='log', title='GNP' )
)
data = Data([trace1])
fig = Figure(data=data, layout=layout)
py.iplot(fig, filename='world GNP vs life expectancy')