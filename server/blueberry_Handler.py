import sqlite3
import random
import string
import datetime

	
blueberry_db = '__HOME__/blueberry.db'


def request_handler(request):
	 # SQL
	conn = sqlite3.connect(blueberry_db)  # connect to that database (will create if it doesn't already exist)
	c = conn.cursor()  # make cursor into database (allows us to execute commands)
	c.execute('''CREATE TABLE IF NOT EXISTS blueberry_table (word str, timing timestamp);''') # run a CREATE TABLE command

	if request['method'] == 'GET':
		allthings = c.execute('''SELECT  word,timing FROM blueberry_table ORDER BY timing DESC;''').fetchall()
		things = []

		if len(allthings) >= 1:
			for data in allthings:
				things.append(data[0])
			return things

		else:
			return ''' Not enough values are there in the database'''
			

	# POST:
	else:
		text = request['form']['text']
					   
		c.execute('''INSERT into blueberry_table VALUES (?,?);''', (text,datetime.datetime.now()))
		
	conn.commit() # commit commands
	conn.close() # close connection to database