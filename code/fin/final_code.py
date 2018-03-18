import urllib2
import string
import serial
import time
import commands

from urlgrabber import urlopen

from bs4 import BeautifulSoup

import subprocess

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

urlGet=str('http://vps.sensorfaucets.com/stock_db/checking.php?mac=')+mac_id[1]
while 1:
	#print ser.readline()  # Reading the incoming responses
	htmlc = urlopen(urlGet).read()
        parsed_htmlc = BeautifulSoup(htmlc,"html.parser")
        s = parsed_htmlc.get_text()
	ret=str(ser.readline())
	#print ret
	if len(ret) > 3:
		pos=ret.index(",")
		id=str(ret[0:pos])
		pos2=ret.rindex(",")
		cmd = ret[pos+1:pos2]
		val = ret[pos2+1:len(ret)-2]
		#print "%s  %s" % (pos,pos2)
		urlSend=str('http://vps.sensorfaucets.com/stock_db/data_store.php?mac=')+mac_id[1]+str('&id=')+id+str('&value=')+val+str('&cmd=')+cmd
		#print val
		urllib2.urlopen(urlSend)
		print id + cmd + val +"\n"
	else:
		print ret
	S = str(s[3:s.index("m")]) + "," + str(s[35:])
	#S = str(s[35:])
	ser.write(S)
	time.sleep(1) 

