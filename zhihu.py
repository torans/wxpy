#coding:utf-8

from urllib import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://www.zhihu.com/question/46301335')
obj = BeautifulSoup(html)
title = obj.find('title').get_text()
tt = title.replace(u' - 大数据 - 知乎' ,'')
desc = obj.find('div',{'class':'zm-editable-content'}).get_text()
content_list = obj.findAll('div',{'class':'zm-editable-content clearfix'})
for i in content_list:
    content = i.get_text()
    print tt,desc,content
