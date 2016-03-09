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
#just for compatibility between Python2 and Python3
try:
    input = raw_input
except NameError:
    pass

# Read hostname from keyboard
hostname = input('Input Hostname (e.g. CAMPUS-Access1): ')
# If you are tired of typing, replace previous line with: hostname = 'RTR-SP2.prime.ciscofrance.com'
# If user just pressed ENTER above, make RTR-SP2.prime.ciscofrance.com the default hostname for convenience
if hostname == '':
    hostname = 'CAMPUS-Access1'

## Login to APIC-EM APIs
# Encode username and password to json
logindata = json.dumps({'username':APIC_USERNAME,'password':APIC_PASSWORD})
headers = {'Content-type': 'application/json'}
# Make POST request to /api/v1/ticket to get login ticket
req = requests.post('https://%s/api/v1/ticket' % APIC_IP, data=logindata, verify=False, headers=headers)
# Get ticket from APIC-EM response
ticket = req.json()['response']['serviceTicket']
# Construct HTTP header with login ticket for subsequent calls
auth_headers = {'Content-type': 'application/json', "X-Auth-Token": ticket}

#!!!FIXME!!! Make GET request to the network-device API to get the network device range from 1 to 500
req = requests.get('https://%s/api/v1/!!!FIXME!!!' % APIC_IP, verify=False, headers=auth_headers)
# Parse json response from APIC-EM
apic_answer = req.json()
# Uncomment next line to output the raw python data structure of the variable "apic_answer"
#pprint(apic_answer)

# Response contains a list with the hosts
for device in apic_answer['response']:
    # !!!FIXME!!! get hostname of this device
    deviceHostname = device['!!!FIXME!!!']
    # Compare hostname of this device to the one we are searching for
    if deviceHostname == hostname:
        # Found the device!
        #!!!FIXME!!! get ID of device
        deviceID = device['!!!FIXME!!!']

# Print device id
print('Device ID: ' + deviceID)

#!!!FIXME!!! Make GET request to the Network Device Configuration API to get the running config (for a specific network device id)
req = requests.get('https://%s/api/v1/!!!FIXME!!!' % (APIC_IP,deviceID), verify=False, headers=auth_headers)
# Parse json response from APIC-EM
apic_answer = req.json()
# Uncomment next line to output the raw python data structure of the variable "apic_answer"
#pprint(apic_answer)
#!!!FIXME!!! get running config from response
running_config = apic_answer['!!!FIXME!!!']
# Print running config of device
print(running_config)

#Submit solution to Exercise Tracking System
ET_DATA['exercise'] = 'Task 4 (optional): Running Config'
ET_DATA['solution'] = running_config.splitlines()[1]
req = requests.post('http://devnetexpress.pythonanywhere.com/submit', headers = headers, data=json.dumps(ET_DATA))
et_answer = req.json()
print('%s: %s' % (et_answer['result'],et_answer['reason']))