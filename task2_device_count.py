#!/usr/bin/env python
#AUTHOR Tobias Huelsdau, <thulsdau@cisco.com>
#COPYRIGHT 2015 Cisco Systems
# line added by greg

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
#Construct HTTP header with login ticket for subsequent calls
auth_headers = {'Content-type': 'application/json', "X-Auth-Token": ticket}

#!!!FIXME!!! Make GET request to the network-device API to get the network device count
req = requests.get('https://%s/api/v1/!!!FIXME!!!' % APIC_IP, verify=False, headers=auth_headers)
# This is the raw response from APIC-EM
print('Raw response from APIC-EM: ' + req.text)
# Parse json response from APIC-EM
apic_answer = req.json()
# Output raw python data structure parsed from JSON to see what's really in there
print('Python data structure parsed from JSON: ')
pprint(apic_answer)
#!!!FIXME!!! Extract device count from apic-em response
device_count = apic_answer['!!!FIXME!!!']
print('Number of devices for this APIC-EM: ' + str(device_count))
#Submit solution to Exercise Tracking System
ET_DATA['exercise'] = 'Task 2: Count'
ET_DATA['solution'] = device_count
req = requests.post('http://devnetexpress.pythonanywhere.com/submit', headers = headers, data=json.dumps(ET_DATA))
et_answer = req.json()
print('%s: %s' % (et_answer['result'],et_answer['reason']))
