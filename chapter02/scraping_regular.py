import re
import urllib2

url = 'http://example.webscraping.com/places/default/view/Afghanistan-1'
html = urllib2.urlopen(url).read()
data = re.findall('<tr id="places_area__row">.*?<td\s*class=["\']w2p_fw["\']>(.*?)</td>', html)

print data
