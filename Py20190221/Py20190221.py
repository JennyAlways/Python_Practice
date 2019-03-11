# -*- coding: utf-8 -*-
#传函数参数是数字，定义循环将文本循环制定次数，rewrite content
#传函数参数是文件名，读文件


#定义参数
def REWRITE(count,filename,content):
    file = open(filename,"a")
    for number in range(count):
        file.write(content)
    file.close()


REWRITE(3,"20190221.txt","Harry Potter\n")
REWRITE(3, "201902212.txt", "Ha? Reporter!")
REWRITE(9, "20190221.txt", "Great")
        

