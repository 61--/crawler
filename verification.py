#coding=utf-8


def get_verification(img_name):
    while True:
        print img_name
        print u'输入验证码'
        code = raw_input()
        print u'输入: [{0}]'.format(code)
        print u'是否保存(yes)'

        yes = raw_input()
        if yes == 'yes':
            return code
