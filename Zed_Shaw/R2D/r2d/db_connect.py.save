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
		mycursor.execute("CREATE TABLE gamestate(id INT AUTO_INCREMENT PRIMARY KEY, pl_name VARCHAR(64), tools VARCHAR(255), room VARCHAR(30), health INT, ts TIMESTAMP)")
		save_data("Rayban_sunglasses",'reception', 1000, 'Player1')

	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_BAD_DB_ERROR:
			print ("Database connection error!: {}".format(err))
		else:
			raise 
	finally:
		if (diadb.is_connected()):
			mycursor.close()
			diadb.close()

def save_data(tools, room, health, name="Player1"):

	diadb = db_connect()
	mycursor = diadb.cursor()
	mycursor.execute("USE r2diamonds_db")
	query = "INSERT INTO gamestate(pl_name, tools, room, health) "\
		"VALUES(%s, %s, %s, %s)"
	params = (name, tools, room, health)

	try:
		mycursor.execute(query, params)
		diadb.commit()

	except mysql.connector.Error:
		raise

	finally:
		if (diadb.is_connected()):
			mycursor.close()
			diadb.close()


def load_data(p_name):

	diadb = db_connect()
	mycursor = diadb.cursor()
	mycursor.execute("USE r2diamonds_db")

	query = "SELECT tools, room, health  FROM gamestate WHERE pl_name = %s ORDER BY ts DESC"

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

def delete_gamestate(roll_back_stage_num):
	try:
		diadb = db_connect()
		mycursor = diadb.cursor()

		mycursor.execute("USE r2diamonds_db")
		mycursor.execute("SELECT MAX(id) FROM gamestate")
		res = mycursor.fetchone()
		max_id = res[0]
		param = int(max_id) - int(roll_back_stage_num)

		query = "DELETE FROM gamestate WHERE id > %s"
		mycursor.execute(query, (param, ))
		diadb.commit()
		mycursor.execute("SELECT * FROM gamestate WHERE id > %s", (param, ))
		records = mycursor.fetchall()
		if len(records) == 0:
			print ("\nRecord Deleted successfully")

	except mysql.connector.Error as error:
		print("Failed to delete record from table: {}".format(error))
	finally:
		if (diadb.is_connected()):
			mycursor.close()
			diadb.close()
			print ("MySQL connection is closed!")

def drop_db(db_name):

	diadb = db_connect()
	mycursor = diadb.cursor()

	mycursor.execute("DROP DATABASE {}".format(db_name))

def encode_dict(dikt):
	encoded = []
	for k,v in dikt.items():
		if v == True:
			encoded.append(k)

	return '?'.join(encoded)


def decode_dict(meta):
	lets_dict = dict()

	spl_meta = meta.split('?')

	for elem in spl_meta:
		lets_dict[str(elem)] = True

	return lets_dict

#list_dbs()
#drop_db('r2diamonds_db')
#create_db()
