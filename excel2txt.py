#coding:utf-8

import jieba
import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

data = xlrd.open_workbook('d://test.xlsx')
table = data.sheets()[0]
nrows = table.nrows
hotwords = {}
count = 1
for i in range(1,nrows):
    #list = table.row_values(i)    #1
    job = jieba.cut(table.col(1)[i].value,cut_all=True)
    for x in job:
        #print x
        f = open('d://hotwords.txt','a+')
        lines = f.readlines()
        for i in lines:
            line = i
        if x in line:
            count = count + 1
            f.write(x+str(count))
            f.write('\n')
            print u'该关键词已出现过，累加中...  :' + x
        else:
            f.write(x+str(count))
            f.write('\n')
            print u'新词：' + x


