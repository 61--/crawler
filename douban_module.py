#coding=utf-8
import re
import webbrowser


g_dbg_text_index = 0


def dbg_get_text_code(text):
    code = [
        'big5',
        'big5hkscs',
        'cp950',
        'gb2312',
        'gbk',
        'gb18030',
        'hz',
        'iso2022_jp_2',
        'utf-8',
        'utf_8_sig',
        'utf_7',
        'utf_16',
        'utf_32',
        'utf_32_be',
        'utf_32_le',
        'utf_16_be',
        'utf_16_le',
    ]
    code_index = 0
    try:
        while True:
            try:
                text.decode(code[code_index], 'ignore')
                print 'current encode: ', code[code_index]
                break
            except UnicodeDecodeError:
                print 'catch error'
                code_index += 1
    except Exception as ex:
        print text
        print repr(text)
        test = u'租'
        print repr(test)
        raise ex


def captcha_input(img_data):
    f = open('captcha.png', 'wb')
    f.write(img_data)
    f.close()

    while True:
        print u'输入验证码'
        code = raw_input()
        print u'输入: [{0}]'.format(code)
        print u'是否保存(yes)'

        yes = raw_input()
        if yes == 'yes':
            return code


def show_link(urls):
    print urls
    for url in urls:
        webbrowser.open(url)


def dbg_save_page(page_text, name='test.html'):
    pass


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


def get_useful_post_url(group_text):
    print group_text
    useful_urls = []
    title_infos = re.findall(r'<td class="title">(.*?)</td>', group_text, re.S)
    for title_info in title_infos:
        m_href = re.search(r'<a href="(.*?)"', title_info)
        if not m_href:
            continue
        m_title = re.search(r'title="(.*?)"', title_info)
        if not m_title:
            continue
        href = m_href.group(1)
        title = m_title.group(1)

        if _useful_title(title):
            print href, u' ======== ', title
            useful_urls.append(href)

    return useful_urls
