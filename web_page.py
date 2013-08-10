#coding=utf-8
import requests
import re
from file_save import save_img
#import save
import verification
from requests.utils import dict_from_cookiejar
from urlparse import urlparse


class WebPage(object):
    def __init__(self):
        self.cookies = None

    def get(self, url):
        head = self._make_head(url)
        r = requests.get(
            url,
            cookies=self.cookies,
            headers=head)
        print 'get cookie: ', r.cookies
        print 'get head: ', r.headers
        return r

    def post(self, url, data):
        head = self._make_post_head(url)
        print 'post old cookie: ', self.cookies
        r = requests.post(
            url,
            data=data,
            cookies=self.cookies,
            headers=head)
        print 'post cookie: ', r.cookies
        print dict_from_cookiejar(r.cookies)
        print 'post head: ', r.headers
        return r

    def _make_post_head(self, url):
        headers = self._make_head(url)
        headers.update({
            'Origin': urlparse(url).hostname})
        return headers

    def _make_head(self, url):
        cookiesheaders = {
            'Accept': 'text/html,application/xhtml+xml,' +
            'application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'gb18030,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'en,zh-CN;q=0.8,zh;q=0.6,en-US;q=0.4',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.bit_length0'
            ' (X11; Linux i686) AppleWebKit/537.bit_length4'
            ' (KHTML, like Gecko)'
            ' Chrome/22.bit_length0.'
            'as_integer_ratio1229.as_integer_ratio79'
            ' Safari/537.bit_length4',
            'Referer': url,
            'Host': urlparse(url).hostname
        }
        '''
        cookie_str = self._make_head_cookie()
        if cookie_str:
            cookiesheaders.update(
                {'Cookie': cookie_str})
        print cookiesheaders
        '''
        return cookiesheaders

    def _make_head_cookie(self):
        if self.cookies is None:
            return None
        dict_ = dict_from_cookiejar(self.cookies)
        if not dict_:
            return None
        dict_line = ''
        first = True
        for k, v in dict_.items():
            if not first:
                dict_line += ';'
            dict_line += k + '='
            dict_line += v
            first = False
        return dict_line


def download_img(web_page, url):
    r = web_page.get(url)
    type_ = r.headers['content-type']
    m = re.match(r'image/(.*)', type_)
    if m:
        m_n = re.match(r'.*/(.*)[.](.*)', url)
        if m_n:
            img_name = m_n.group(1) + '.' + m.group(1)
            save_img(img_name, r.content)
            return img_name


def _get_login_verify_img_url(text):
    m = re.search(r'<(.*)class="captcha_image"(.*)>', text)
    if m:
        for i in [1, 2]:
            s_m = re.search(r'src="(.*?)"', m.group(i))
            if s_m:
                name = s_m.group(1)
                return name


def _get_login_verify_id(text):
    m = re.search(r'<(.*)name="captcha-id"(.*)>', text)
    if m:
        for i in [1, 2]:
            s_m = re.search(r'value="(.*)"', m.group(i))
            if s_m:
                return s_m.group(1)


def do_douban_login(web_page, email, password):
    '''
    cookie = save.load_cookie('douban', email)
    if cookie:
        web_page.cookies = cookie
        url = r'http://www.douban.com/'
        r = web_page.get(url)
        return r
    '''

    url = r'http://www.douban.com/accounts/login'
    r = web_page.get(url)
    web_page.cookies = r.cookies

    print 'bid: ', r.cookies['bid']
    print dict_from_cookiejar(r.cookies)
    data = {
        'source': 'simple',
        'redir': 'http://www.douban.com/',
        'form_email': email,
        'form_password': password,
        'remember': 'on',
        'user_login': u'登录',
    }

    verify_url = _get_login_verify_img_url(r.text)
    if verify_url:
        img_name = download_img(web_page, verify_url)
        verify_id = _get_login_verify_id(r.text)
        solution = verification.get_verification(img_name)
        data.update({
            'captcha-id': verify_id,
            'captcha-solution': solution
        })
    print 'post ' + '#' * 30
    post_url = r'http://www.douban.com/accounts/login'
    r = web_page.post(post_url, data)
    web_page.cookies = r.cookies
    print dict_from_cookiejar(r.cookies)
    return r
