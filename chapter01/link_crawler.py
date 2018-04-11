import re
import urlparse
from download_example import download

def link_crawler(seed_url, link_regex):
    """Crawl from the given seed URL following links matched by link_regex
    """
    crawl_queue = [seed_url]
    # keep track which URL's have seen before
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        # filter for links matching our regular expression
        for link in get_links(html):
            #print link
            if re.match(link_regex, link):
                link = urlparse.urljoin(seed_url, link)
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)

def get_links(html):
    """Return a list of links from html
    """
    #print html
    # a regular expression to extract all links from the webpages
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']>', re.IGNORECASE)
    # list of all links from the webpage
    return webpage_regex.findall(html)

link_crawler('http://example.webscraping.com', '/places/default/view');
