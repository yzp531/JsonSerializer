#coding=gbk
'''
@author: zhengpeiyuan@baidu.com
'''


def add_path(path):
    '''���Ŀ¼��sys.path��'''
    import sys
    if path not in sys.path:
        sys.path.insert(0, path)


add_path('../bin')
