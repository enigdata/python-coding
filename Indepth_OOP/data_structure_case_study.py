from urllib.request import urlopen
from urllib.parse import urlparse
import re
import sys

LINK_REGEX = re.compile("<a [^>]*href=['\"]([^'\"]+)['\"][^>]*>")

class LinkCollector:
    def __init__(self, url):
        self.url = "" + urlparse(url).netloc 
        self.collect_links = set()
        self.visited_links = set()

    def collect_links(self, path = "/"):
        full_url = self.url + path 
        self.visited_links.add(full_url)
        page = str(urlopen(full_url).read())
        links = LINK_REGEX.findall(page)
        self.collect_links = links.union(self.collect_links)
        print(links)
        

if __name__ == "__main__":
    LinkCollector(sys.argv[1]).collect_links()

