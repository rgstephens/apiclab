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
# Encode username and password to json
logindata = json.dumps({'username':APIC_USERNAME,'password':APIC_PASSWORD})
headers = {'Content-type': 'application/json'}
# Make POST request to /ticket to get login ticket
req = requests.post('https://%s/api/v1/ticket' % APIC_IP, data=logindata, verify=False, headers=headers)
# Get ticket from APIC-EM response
ticket = req.json()['response']['serviceTicket']
# Construct HTTP header with login ticket for subsequent calls
auth_headers = {'Content-type': 'application/json', "X-Auth-Token": ticket}

#!!!FIXME!!! Make GET request to the network-device API to get the network device range from 1 to 10
req = requests.get('https://%s/api/v1/!!!FIXME!!!' % APIC_IP, verify=False, headers=auth_headers)
# Parse json response from APIC-EM
apic_answer = req.json()
# Uncomment next line to output the raw python data structure of the variable "apic_answer"
#pprint(apic_answer)

#!!!FIXME!!! APIC-EM Response contains a list with all ten hosts
for device in apic_answer['!!!FIXME!!!']:
    #pprint(device)
    print(str(device['serialNumber']) + '\t' + str(device['managementIpAddress']) + '\t' + str(device['hostname']))

#Submit solution to Exercise Tracking System
ET_DATA['exercise'] = 'Task 3: Show Devices'
ET_DATA['solution'] = apic_answer['response'][0]['serialNumber']
req = requests.post('http://devnetexpress.pythonanywhere.com/submit', headers = headers, data=json.dumps(ET_DATA))
et_answer = req.json()
print('%s: %s' % (et_answer['result'],et_answer['reason']))