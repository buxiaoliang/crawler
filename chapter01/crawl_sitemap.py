import re
from download_example import download

def crawl_sitemap(url):
    # download the sitemap file
    sitemap = download(url)
    print sitemap
    # extract the sitemap links
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    # download each link
    for link in links:
        print link
        html = download(link)
        # scrape html here
        # ...

crawl_sitemap('http://example.webscraping.com/sitemap.xml')
