#coding=utf-8
from web_page import WebPage
import douban_module as module
import re


class Douban(object):
    def __init__(self):
        self.web_page = WebPage()

    def login(self, email, password):
        print 'do douban login'
        login_url = r'http://www.douban.com/accounts/login'

        r = self.web_page.get(login_url)
        data = {
            'source': 'simple',
            'redir': 'http://www.douban.com',
            'form_email': email,
            'form_password': password,
            'remember': 'on',
            'user_login': u'登录',
        }
        captcha_url = self._get_captcha_img_url(r.text)
        if captcha_url:
            print u'登录需要验证码'
            img_r = self.web_page.get(captcha_url)
            captcha_solution = module.captcha_input(img_r.content)
            if not captcha_solution:
                print 'input captcha code error'
                return False

            data.update({
                'captcha-id': self._get_captcha_id(r.text),
                'captcha-solution': captcha_solution,
            })

        login_post_url = r'http://www.douban.com/accounts/login'
        r = self.web_page.post(login_post_url, data)
        return self._check_log_success(r)

    def visit_group(self, group_url, max_page=15):
        for i in range(max_page):
            url = group_url + r'discussion?start={0}'.format(i * 25)
            print url
            page_r = self.web_page.get(url)
            post_urls = module.get_useful_post_url(page_r.text)
            module.show_link(post_urls)

    def _get_captcha_img_url(self, page_text):
        m = re.search(r'<(.*)class="captcha_image"(.*)>', page_text)
        if m:
            for i in [1, 2]:
                s_m = re.search(r'src="(.*?)"', m.group(i))
                if s_m:
                    name = s_m.group(1)
                    return name

    def _get_captcha_id(self, page_text):
        m = re.search(r'<(.*)name="captcha-id"(.*)>', page_text)
        if m:
            for i in [1, 2]:
                s_m = re.search(r'value="(.*)"', m.group(i))
                if s_m:
                    return s_m.group(1)

    def _check_log_success(self, r):
        if 'login' in r.url:
            return False
        return True
