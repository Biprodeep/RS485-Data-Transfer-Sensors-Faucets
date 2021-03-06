import urllib2
import string
import serial
import time
import commands
import RPi.GPIO as GPIO
import time
import json

from urlgrabber import urlopen

from bs4 import BeautifulSoup

import subprocess

# Initializing GPIO functions here 
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Such parameters are required for the sensors so I use them
ser = serial.Serial(     
     port='/dev/ttyUSB0',
     baudrate = 9600,
     parity=serial.PARITY_NONE,
     stopbits=serial.STOPBITS_ONE,
     bytesize=serial.EIGHTBITS,
     timeout=0.75
     )
mac_id=commands.getstatusoutput("ethtool -P eth0 | awk -F \' \' \'{print $3}\'")
urlReg=str('http://vps.sensorfaucets.com/stock_db/regester.php?mac=')+mac_id[1]+str('&type=HUB')
html = urlopen(urlReg).read()
parsed_html = BeautifulSoup(html,"html.parser")
print parsed_html.get_text()

urlGet=str('http://vps.sensorfaucets.com/stock_db/hub_machine_checking.php?mac=')+mac_id[1]
i=0
while 1:
	ret=str(ser.readline())
	print ser.readline()  # Reading the incoming responses
	# When my data shelf is empty I will get data from the server untill then it will be locked.
	if i==0:
		jsonc = json.load(urlopen(urlGet))
	if len(ret) > 3:
		pos=ret.index(",")
		id=str(ret[0:pos])
		pos2=ret.rindex(",")
		cmd = ret[pos+1:pos2]
		val = ret[pos2+1:len(ret)-2]
		urlSend=str('http://vps.sensorfaucets.com/stock_db/data_store.php?mac=')+mac_id[1]+str('&id=')+id+str('&value=')+val+str('&cmd=')+cmd
		urllib2.urlopen(urlSend)
		print id + cmd + val +"\n"
	else:
		print ret
	# Sending the JSON indices one by one in respective iteration cycles.
	ser.write(jsonc[i])
	i+=1
	# Case when my data has been distributed to the protocol
	if i==len(jsonc):
		i=0
	time.sleep(2.5) 

'''
def switch_pressed():
	# Checking the state of the switch connected to the PIN40 
        input_state = GPIO.input(21)
        if input_state == False:
                print('Button Pressed')
		machlst=str('http://vps.sensorfaucets.com/stock_db/machinelist.php?mac=')+mac_id[1]
'''

