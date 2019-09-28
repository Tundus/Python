import mysql.connector
from mysql.connector import errorcode

def list_dbs():

	diadb =  db_connect()
	mycursor = diadb.cursor()

	mycursor.execute("SHOW DATABASES")

	for x in mycursor:
		print (x)

def db_connect():

	try:
		diadb = mysql.connector.connect(
			host = "localhost",
			user = "r2dia",
			passwd = "defaultpwd")

	except mysql.connector.Error as err:
		raise err

	return diadb

def create_db():

	diadb = db_connect()
	mycursor = diadb.cursor()

	try:
		mycursor.execute("CREATE DATABASE r2diamonds_db")
		mycursor.execute("USE r2diamonds_db")
		mycursor.execute("CREATE TABLE gamestate(id INT AUTO_INCREMENT PRIMARY KEY, pl_name VARCHAR(64), tools VARCHAR(255), room VARCHAR(30), ts TIMESTAMP)")

	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_BAD_DB_ERROR:
			print ("Database connection error!: {}".format(err))
		else:
			raise 

def save_data(tools, room, name="Player1"):

	diadb = db_connect()
	mycursor = diadb.cursor()
	mycursor.execute("USE r2diamonds_db")
	query = "INSERT INTO gamestate(pl_name, tools, room) "\
		"VALUES(%s, %s, %s)"
	params = (name, tools, room)

	try:
		mycursor.execute(query, params)

		diadb.commit()
		mycursor.close()
		diadb.close()

	except mysql.connector.Error:
		raise


def load_data(p_name):

	diadb = db_connect()
	mycursor = diadb.cursor()
	mycursor.execute("USE r2diamonds_db")

	query = "SELECT *  FROM gamestate WHERE pl_name = %s ORDER BY ts DESC"

	#print (query, % params)

	try:
		mycursor.execute(query, (p_name,))
		record = mycursor.fetchone()
		return record

	except mysql.connector.Error:
		raise

	finally:
		if (diadb.is_connected()):
			mycursor.close()
			diadb.close()

def drop_db(db_name):

	diadb = db_connect()
	mycursor = diadb.cursor()

	mycursor.execute("DROP DATABASE {}".format(db_name))

def encode_dict(dikt):
	encoded = []
	for k,v in dikt.items():
		if v == True:
			encoded.append(k)
	
	return encoded

#list_dbs()
#drop_db('r2diamonds_db')
#create_db()

t = dict()
t['Yellow_key'] = True
t['Big_meat_chunk'] = True
T = ' '.join(encode_dict(t))
print ("%r" % T)

save_data(T, 'meat')
a = load_data('Player1')
for i in a:
	print (i)
