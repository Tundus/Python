import mysql.connector


def db_exists():

	diadb = mysql.connector.connect(
		host = "localhost",
		user = "default_user",
		passwd = "default_passwd!",
		database = "r2dia_database")

	mycursor = diadb.cursor()

	mycursor.execute("SHOW DATABASES")

	for x in mycursor:
		print (x)

def db_create():

	diadb = mysql.connector.connect(
		host = "localhost",
		user = "default_user",
		passwd = "default_passwd!")

	mycursor = diadb.cursor()

	mycursor.execute("CREATE DATABASE r2diadatabase")


db_create()
db_exists()
