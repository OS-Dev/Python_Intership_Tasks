# Osmel Savon
#python3

###### Task 2 - MySQL and Intercom   #######
	#a. Retrive user table from MySql database
	#b. Use query results to create users in Intercom
	#c. Save users on Intercom

from intercom.client import Client
intercom = Client(personal_access_token='my_personal_access_token')
import msql.connector

config = {
	'user': 'root',
	'password': '',
	'host': '127.0.0.1',
	'database': 'users',
	'raise_on_warnings': True,
	'use_pure': False,
}

cnx = mysql.connector.connect(**config)

query = (***SELECT * FROM user***)
cursor = cnx.cursor()
cursor.excute(query)
for (id,name,email) in cursor:
	print(id,name,email)
	user = intercom.users.create(id=id, name=name, email=email)
	intercom.users.save(user)