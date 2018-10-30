#!/usr/bin/python

from creepy import Crawler
from threading import Lock
import argparse

class TestCrawler(Crawler):
    def __init__(self):
        super(TestCrawler, self).__init__()
        self.process_lock = Lock()

    def process_document(self, doc):
        self.process_lock.acquire()
        print 'GET', doc.status, doc.url
        self.process_lock.release()

c = TestCrawler()
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="site/url for crawling", required=True)
args = parser.parse_args()
site = args.url
c.crawl(site)
