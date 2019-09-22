import mysql.connector


def db_exists():

	diadb = mysql.connector.connect(
		host = "localhost",
		user = "defaultuser",
		passwd = "defaultpasswd",
		database = "r2diadatabase")

	mycursor = diadb.cursor()

	mycursor.execute("SHOW DATABASES")

	for x in mycursor:
		print (x)

def db_create():

	diadb = mysql.connector.connect(
		host = "localhost",
		user = "defaultuser",
		passwd = "defaultpasswd")

	mycursor = diadb.cursor()

	mycursor.execute("CREATE DATABASE r2diadatabase")


db_create()
db_exists()
