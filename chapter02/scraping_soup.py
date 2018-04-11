from bs4 import BeautifulSoup
import urllib2

url = 'http://example.webscraping.com/places/default/view/Afghanistan-1'
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
# locate the area row
tr = soup.find(attrs={'id': 'places_area__row'})
# locate the area tag
td = tr.find(attrs={'class': 'w2p_fw'})
# extract the text from this tag
area = td.text
print area
