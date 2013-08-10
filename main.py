#coding=utf-8
from web_page import WebPage
#from web_page import download_img
#from verification import get_verification
from web_page import do_douban_login
import save


def main():
    web_page = WebPage()
    email = 'zmtest100@gmail.com'
    password = 'douban100'
    r = do_douban_login(
        web_page, email, password)
    return
    save.file_save_page('douban', r.text)

    url = 'http://www.douban.com/group/'
    r = web_page.get(url)
    save.file_save_page('douban_2', r.text)

    save.save_cookie('douban', email, web_page.cookies)
    print '========================'
    '''
    code = get_verification('test.img')
    print code
    return

    url = r'http://www.baidu.com/img/bdlogo.gif'
    download_img(web_page, url)
    '''


if __name__ == '__main__':
    main()
