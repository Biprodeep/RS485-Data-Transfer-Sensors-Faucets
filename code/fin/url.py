import urllib2
import string
import commands

from urlgrabber import urlopen

from bs4 import BeautifulSoup

import subprocess

mac_id=commands.getstatusoutput("ethtool -P eth0 | awk -F \' \' \'{print $3}\'")
url=str('http://vps.sensorfaucets.com/stock_db/regester.php?mac=')+mac_id[1]+str('&type=HUB')
html = urlopen(url).read()
parsed_html = BeautifulSoup(html,"html.parser")
print parsed_html.get_text()
#html.close()
url=str('http://vps.sensorfaucets.com/stock_db/checking.php?mac=')+mac_id[1]

while 1:
	htmlc = urlopen(url).read()
	parsed_htmlc = BeautifulSoup(htmlc,"html.parser")
	s = parsed_htmlc.get_text()
	p = s[0:5] + s[26:50]
	print p
	
