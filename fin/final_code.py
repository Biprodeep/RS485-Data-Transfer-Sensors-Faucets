import urllib2
#import urllib
#import html2text
import string
import serial
import time
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
bashCommand = "ethtool -P eth0 | awk -F ' ' '{print $3}'"
mac_id_rpi = str(subprocess.check_output(['bash','-c', bashCommand]))
html = urllib2.urlopen("http://vps.sensorfaucets.com/stock_db/regester.php?mac=b8:27:eb:e9:4d:b1&type=HUB").read()
parsed_html = BeautifulSoup(html,"html.parser")
print parsed_html.get_text()
while 1:
      print ser.readline()  # Reading the incoming responses
      htmlc = urllib2.urlopen("http://vps.sensorfaucets.com/stock_db/checking.php?mac=b8:27:eb:e9:4d:b1").read()
      parsed_htmlc = BeautifulSoup(htmlc,"html.parser")
      s = parsed_htmlc.get_text()
      S = str(s[0:5] + s[26:])
      ser.write(S)
      time.sleep(0.3)  

