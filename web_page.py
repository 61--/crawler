#coding=utf-8
import requests
from urlparse import urlparse


class WebPage(object):
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml'
            ',application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'en,zh-CN;q=0.8,zh;q=0.6,en-US;q=0.4',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu '
            'Chromium/28.0.1500.71 Chrome/28.0.1500.71 Safari/537.36'
        }

    def get(self, url):
        self._update_headers(url)
        r = self.session.get(
            url,
            headers=self.headers)
        return r

    def post(self, url, data):
        self._update_headers(url)
        r = self.session.post(
            url,
            data=data,
            headers=self.headers)
        return r

    @property
    def cookies(self):
        return self.ssession.cookies

    @property
    def status_code(self):
        return self.session.status_code

    def _update_headers(self, url):
        self.headers['Referer'] = url,
        self.headers['Host'] = urlparse(url).hostname
