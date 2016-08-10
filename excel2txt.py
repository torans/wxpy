#coding:utf-8

import jieba
import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

data = xlrd.open_workbook('h://bigdata/data/test.xlsx')
table = data.sheets()[0]
nrows = table.nrows
hotwords = {}
count = 1
for i in range(1,nrows):
    #list = table.row_values(i)    #1
    job = jieba.cut(table.col(1)[i].value,cut_all=True)
    for x in job:
        #print x
        if x !='':
            f = open('h://bigdata/data/gy581.txt','a+')
            f.write(x)
            f.write('\n')
            print u'写入：' + x
            f.close()
        else:
            print u'关键词为空'

