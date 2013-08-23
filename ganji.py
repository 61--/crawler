#coding=utf-8
from web_page import WebPage
import ganji_module as module


class Ganji(object):
    def __init__(self):
        self.web_page = WebPage()
        pass

    def view_person_all(self, page=30):
        for i in range(page):
            page_url = r'http://bj.ganji.com/fang1/haidian/a1o{0}m1/'.format(
                i + 1)
            r = self.web_page.get(page_url)
            urls = module.get_post_urls(r.text)
            print urls
            for url in urls:
                r = self.web_page.get(url)
                if module.check_useful(r.text):
                    module.show_link(url)

    def _get_page(self, url):
        r = self.web_page.get(url)
        if 'confirm' in r.url:
            pass
        return r
        pass
