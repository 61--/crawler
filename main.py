#coding=utf-8

from douban import Douban
from web_page import WebPage
from ganji import Ganji


def dbg_site(web_page):
    pass


def main():
    douban = Douban()
    if not douban.login('zmtest100@gmail.com', 'douban100'):
        print 'login failed'
        return

    print 'login success'
    group_1 = r'http://www.douban.com/group/beijingzufang/'
    douban.visit_group(group_1, 60)
    group_2 = r'http://www.douban.com/group/zhufang/'
    douban.visit_group(group_2, 60)


def test_proxy():
    web_page = WebPage()
    web_page.set_proxy('204.12.223.173:7808')
    r = web_page.get(r'http://www.baidu.com/')
    print r.text


def view_ganji():
    ganji = Ganji()
    ganji.view_person_all(10)
    pass

if __name__ == '__main__':
    '''
    test_proxy()
    '''
    '''
    view_ganji()
    '''
    main()
