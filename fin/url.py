import urllib2
#import urllib
#import html2text
import string

from bs4 import BeautifulSoup

import subprocess

bashCommand = "ethtool -P eth0 | awk -F ' ' '{print $3}'"
mac_id_rpi = str(subprocess.check_output(['bash','-c', bashCommand]))
#url=str("http://vps.sensorfaucets.com/stock-db/regester.php?mac=%s") % mac_id_rpi, + "&type=HUB" 
#url = urllib.urlencode(str("http://vps.sensorfaucets.com/stock-db/regester.php?mac=" + mac_id_rpi + "&type=HUB"))


html = urllib2.urlopen("http://vps.sensorfaucets.com/stock_db/regester.php?mac=b8:27:eb:e9:4d:b1&type=HUB").read()
parsed_html = BeautifulSoup(html,"html.parser")
print parsed_html.get_text()
#print url
#print "http://vps.sensorfaucets.com/stock-db/regester.php?mac=b8:27:eb:e9:4d:b1&type=HUB"

while 1:
	htmlc = urllib2.urlopen("http://vps.sensorfaucets.com/stock_db/checking.php?mac=b8:27:eb:e9:4d:b1").read()
	parsed_htmlc = BeautifulSoup(htmlc,"html.parser")
	s = parsed_htmlc.get_text()
	p = s[0:5] + s[26:38]
	print p
	
