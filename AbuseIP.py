#!/usr/bin/env python

import requests
import json


def checkIp1():
    check=str(IP)
    r=requests.get('https://www.abuseipdb.com/check/' +check+'/json?key=[APIKEYGOESHERE]') 
    loaded_content = json.loads(r.content)
    print (json.dumps(loaded_content, sort_keys=True, indent=4))

def report():
    check=str(IP)
    category = raw_input(''' 
        3 Fraud Orders
        4 DDoS Attack 
        9 Open Proxy
        10 Web Spam
        11 Email Spam
        14 Port Scan
        18 Brute-Force
        19 Bad Web Bot
        20 Exploited Host
        21 Web App Attack
        22 SSH
        23 IoT Targeted
Enter Category number from the above list: ''')
    comment = raw_input('Enter a comment: ')
    r=requests.get('https://www.abuseipdb.com/report/json?key= &category=' +category+'&comment=' +comment+'&ip=' +check)
    loaded_content = json.loads(r.content)
    print (json.dumps(loaded_content, sort_keys=True, indent=4))

if __name__ == '__main__':
    print ("\033[H\033[J")
    IP=raw_input('\n Enter IP: ')
    checkIp1()
    while True:
        choice = raw_input('\nWould you like Report this IP? : ')
        if choice.strip() == 'yes' or choice.strip() == 'y':
            report()
            quit()
        elif choice.strip() == 'no' or choice.strip() == 'n':
            quit()
