#coding=utf-8

from douban import Douban


def dbg_site(web_page):
    pass


def main():
    douban = Douban()
    if not douban.login('zmtest100@gmail.com', 'douban100'):
        print 'login failed'
        return

    print 'login success'
    group_1 = r'http://www.douban.com/group/beijingzufang/'
    douban.visit_group(group_1, 40)

if __name__ == '__main__':
    main()
