'''
To make a Raspberry Pi communicate with a set of weighing machines over serial and send/recieve the responses according to the client requirements.
.
Author: Biprodeep Roy
.
Company: Teknik
.
Version: v1.0

'''
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

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
    
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
c=0
while 1:
	ret=str(ser.readline())
	print ser.readline()  # Reading the incoming responses
	# When my data shelf is empty I will get data from the server untill then it will be locked.
	if len(ret) > 3:
		pos=ret.index(",")
		id=str(ret[0:pos])
		pos2=ret.index('*')
		pos3=ret.rindex(",")
		pos4=ret.rindex(";")
		macc=ret[pos+1:pos2]
		val = ret[pos2+1:pos3]
		cmd = ret[pos3+1:pos4]
		print "****))Sending to server:"+str(id)+"," + str(macc)+"," + str(val) +","+ str(cmd) +"\n"
		urlSend=str('http://vps.sensorfaucets.com/stock_db/data_store.php?mac=')+macc+str('&id=')+id+str('&value=')+val+str('&cmd=')+cmd
		urllib2.urlopen(urlSend)
		#print id + cmd + val +"\n"
	else:
		print ret
	htmlc = urlopen(urlGet).read()
	parsed_htmlc = BeautifulSoup(htmlc,"html.parser")
	if c==0:
		s = parsed_htmlc.get_text()
		print "From Server:"+s
		i=0
		if len(s)<2:     # if all commands are acknowledged
			continue
	slist=find(s,";")
	S = str(s[i:(find(s,";")[c])])
	i=find(s,";")[c]+1
	c=c+1
	if c==len(slist):
		c=0
	print "Sending to Arduino:"+S
	ser.write(S)
	# When my data shelf is empty I will get data from the server untill then it will be locked.
	seconds=0
	while seconds<1:
		ret=str(ser.readline())
		if len(ret) > 3:
                	pos=ret.index(",")
                	id=str(ret[0:pos])
                	pos2=ret.index('*')
                	pos3=ret.rindex(",")
                	pos4=ret.rindex(";")
                	macc=ret[pos+1:pos2]
                	val = ret[pos2+1:pos3]
                	cmd = ret[pos3+1:pos4]
                	print "****))Sending to server:"+str(id)+"," + str(macc)+"," + str(val) +","+ str(cmd) +"\n"
			urlSend=str('http://vps.sensorfaucets.com/stock_db/data_store.php?mac=')+macc+str('&id=')+id+str('&value=')+val+str('&cmd=')+cmd
			urllib2.urlopen(urlSend)
                	break
        	else:
			seconds+=0.1
			time.sleep(0.1)
