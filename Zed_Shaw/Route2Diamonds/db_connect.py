import mysql.connector


def db_exists():

	diadb = mysql.connector.connect(
		host = "localhost",
		user = "r2dia",
		passwd = "defaultpwd",
		database = "r2diamonds_db")

	mycursor = diadb.cursor()

	mycursor.execute("SHOW DATABASES")

	for x in mycursor:
		print (x)

def db_create():

	diadb = mysql.connector.connect(
		host = "localhost",
		user = "r2dia",
		passwd = "defaultpwd")

	mycursor = diadb.cursor()

	mycursor.execute("CREATE DATABASE r2diamonds_db")


db_create()
db_exists()
