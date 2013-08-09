#coding=utf-8
from os.path import expanduser
import os
import md5
import re
import pickle
from requests.utils import dict_from_cookiejar
from requests.utils import cookiejar_from_dict
from pymongo import MongoClient
db = MongoClient()


def get_img_save_dic():
    return expanduser('~') + os.sep + \
        'Pictures' + os.sep + 'crawer'


def get_cookie_save_dic():
    return expanduser('~') + os.sep + \
        'Pictures' + os.sep + 'crawer_cookie'


def _check_dic(dic):
    if not os.path.exists(dic):
        os.makedirs(dic)


def save_img(name, content):
    dic = get_img_save_dic()
    _check_dic(dic)
    f = open(os.path.join(dic, name), 'wb')
    f.write(content)
    f.close()


def save_page(url, page_text):
    body = page_text
    m = re.search(r'<body>(.*)</body>', page_text)
    if m:
        body = m.group(1)
    m = md5.new()
    m.update(body)
    body_md5 = m.hexdigest()
    if db.raw_page.find_one({'url': url, 'md5': body_md5}):
        return True

    db.raw_page.insert(
        {'url': url, 'md5': body_md5, 'body': page_text})


def file_save_page(url, page_text):
    html_name = url + '.html'
    with open(html_name, 'w') as f:
        f.write(page_text.encode('utf-8'))


def save_cookie(site_name, username, cookie):
    cookie_dic = get_cookie_save_dic() + os.sep + site_name
    _check_dic(cookie_dic)
    cookie_save_name = os.path.join(cookie_dic, username)
    with open(cookie_save_name, 'w') as f:
        dict_ = dict_from_cookiejar(cookie)
        print 'save cookie: ', dict_
        pickle.dump(dict_, f)


def load_cookie(site_name, username):
    cookie_dic = get_cookie_save_dic() + os.sep + site_name
    cookie_save_name = os.path.join(cookie_dic, username)
    print 'load cookie: ', cookie_save_name
    if not os.path.exists(cookie_save_name):
        return None

    cookie = None
    with open(cookie_save_name) as f:
        dict_ = pickle.load(f)
        if not dict_:
            return None
        print 'load cookie: ', dict_
        cookie = cookiejar_from_dict(dict_)
    return cookie
