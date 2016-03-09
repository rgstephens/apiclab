#!/usr/bin/env python
#AUTHOR Tobias Huelsdau, <thulsdau@cisco.com>
#COPYRIGHT 2015 Cisco Systems

#import URL and Login data for APIC-EM
from devnetexpress import APIC_IP, APIC_USERNAME, APIC_PASSWORD, ET_URL, ET_DATA

#requests is a 3rd party lib for http calls
import requests
#disable Certificat warning
try:
    requests.packages.urllib3.disable_warnings()
except:
    pass
#json lib
import json
#import pprint function from pprint module
#nice way to output python data structures
from pprint import pprint

## Login to APIC-EM APIs
#Encode username and password to json
logindata = json.dumps({'username':APIC_USERNAME,'password':APIC_PASSWORD})
headers = {'Content-type': 'application/json'}
#Make POST request to /ticket to get login ticket
req = requests.post('https://%s/api/v1/ticket' % APIC_IP, data=logindata, verify=False, headers=headers)
#Get ticket from APIC-EM response
ticket = req.json()['response']['serviceTicket']
print('Login Ticket: ' + ticket)
#Construct HTTP header with login ticket for subsequent calls (if we were to make more...)
auth_headers = {'Content-type': 'application/json', "X-Auth-Token": ticket}

