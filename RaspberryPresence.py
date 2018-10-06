"""
Copyright (c) 2018 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

__author__ = "Healkan Cheung"
__copyright__ = "Copyright (c) 2018 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.0"

import requests
import bluetooth
import time
import RPi.GPIO as GPIO


#setup for WebEx Teams
url = "https://api.a6.ciscospark.com/v1/messages"
headers = {
    'Content-Type': "application/json; charset=utf-8",
    'Authorization': "Bearer <Bearer ID>",
    'Cache-Control': "no-cache"
    }

#setting up pinout
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)

print 'Checking'
x = True
init = True


while True:
    print "Checking " + time.strftime("%a,  %d %b %Y %H:%M:%S", time.gmtime())
    result = bluetooth.lookup_name('<Bluetooth address>', timeout=5)
    if (result != None):
        print "In"
        if (x != True) or (init == True):
            x = True
            init = False
            payload = "{\n  \"toPersonEmail\" : \"<email address>\",\n  \"text\" : \"Device is in the house\"\n}"
            response = requests.request("POST", url, data=payload, headers=headers)
            GPIO.output(8, True)
    else:
        print "Out"
        if (x == True):
            x = False
            payload = "{\n  \"toPersonEmail\" : \"<email address>\",\n  \"text\" : \"Device is out of the house\"\n}"
            response = requests.request("POST", url, data=payload, headers=headers)
            GPIO.output(8, False)
    time.sleep(5)
