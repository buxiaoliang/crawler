import lxml.html
import urllib2
import csv
import re

class ScrapeCallback:
    def __init__(self):
        self.writer = csv.writer(open('countries.csv', 'w'))
        self.fields = ('area', 'population', 'iso', 'country', 'capital', 'continent', 'tld', 'currency_code', 'currency_name', 'phone','postal_code_format', 'postal_code_regex', 'languages', 'neighbours')
        self.writer.writerow(self.fields)
        print 'init'

    def __call__(self):
        print 'call'
        html = urllib2.urlopen('http://example.webscraping.com/places/default/view/Afghanistan-1').read()
        tree = lxml.html.fromstring(html)
        row = []
        for field in self.fields:
            row.append(tree.cssselect('table > tr#places_{}__row > td.w2p_fw'.format(field))[0].text_content())
        self.writer.writerow(row)

if __name__ == '__main__':
    scrape_callback = ScrapeCallback()
    scrape_callback()
