import psycopg2
import sys 
import pprint 

def main():
	conn_string = ("dbname='test' user='leah' host='localhost' password='leah'")
	conn = psycopg2.connect(conn_string)
	cursor = conn.cursor()
	cursor.execute
	cursor.execute("SELECT * FROM potluck")
	records = cursor.fetchall()
	pprint.pprint(records)

if __name__ == "__main__":
	main()][]