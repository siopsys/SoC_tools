#!/usr/bin/env python

import json
import requests
from bs4 import BeautifulSoup

def checkIp1():
    check=str(IP)
    r=requests.get('https://www.abuseipdb.com/check/' +check+'/json?key=<YOURAPIHERE>&days=365')
    loaded_content = json.loads(r.content)
    print (json.dumps(loaded_content, sort_keys=True, indent=4))

    print '\ncomments:\n'
    url = 'https://www.abuseipdb.com/check/' + check
    myheaders = {'User-Agent': 'Mozilla/5.0'}
    source_code = requests.get(url, headers=myheaders).text
    soup = BeautifulSoup(source_code, "lxml")

    for table_data in soup.find_all('td', {'data-title': 'Comment'}):
        print(table_data.get_text()).replace('\n', ' ')

    print ('\nweb link: https://www.abuseipdb.com/check/' +check)

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
    r=requests.get('https://www.abuseipdb.com/report/json?key=<YOURAPIHERE>&category=' +category+'&comment=' +comment+'&ip=' +check)
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
