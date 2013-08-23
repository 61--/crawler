#coding=utf-8
import re
import webbrowser


def get_post_urls(page_text):
    print page_text
    raise 34
    urls = []
    title_infos = re.findall(
        r'<a class=.list-info-title.(.*?)>', page_text, re.S)
    for title_info in title_infos:
        print '=================='
        m = re.search("href='(.*?)'", title_info)
        if m:
            url = 'http://bj.ganji.com' + m.group(1)
            urls.append(url)
    print urls
    return urls


g_keywords = [
    u'中关村',
    u'黄庄',
    u'知春',
    u'人大',
    u'双榆树',
    u'圆明园',
    u'西苑',
    u'苏州街',
    u'稻香',
]


def _useful_title(title):
    search = u'.*('
    first = True
    for Keyword in g_keywords:
        if not first:
            search += u'|'
        else:
            first = False
        search += Keyword
    search += ').*'
    print search
    m = re.search(search, title)
    if m:
        return True
    return False


def check_useful(page_text):
    m = re.search(r'<div class=.summary-cont.>(.*>)</div>', page_text)
    if m:
        content = m.group(1)
        if _useful_title(content):
            return True
    return False


def show_link(url):
    webbrowser.open(url)
