
#Osmel Savon

#python3

#Task 1
    #a. Use Popen to start all commands simultaneously and record total elapsed time
    #b. Use poll() to ensure proper termination
    #c. Return total elapsed time, average/maximum/minimum execution time amount all commands

from subprocess import Popen
import time


####### Task 1 - Running command using Subprocess(Popen)
results = []
commands = [
    'sleep 3',
    'ls -l /',
    'find /',
    'sleep 4',
    'find /usr',
    'date',
    'sleep 5',
    'uptime'
]
# Start Time
start_time = time.time()
# Popen
output = subprocess.Popen(commands,universal_newlines=True, shell = True)
while (output.poll() is None):
    time.sleep(1)
# End Time
end_time = time.time()
# Total Time
total_time = float(end_time - start_time)
print(total_time)


#For Loop - Get indivual times and store value
for command in commands:
    start_ptime = time.time()
    p = subprocess.Popen([command],shell = True)
    while (p.poll() is None):
        time.sleep(1)
    end_ptime = time.time()
    total_ptime = float(end_ptime - start_ptime)
    results.append(total_ptime)

print(total_time, (sum(results)/len(results)), max(results), min(results))

###### Task 2 - MySQL and Intercom   #######

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
