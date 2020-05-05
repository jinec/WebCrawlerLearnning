# -*- coding:utf-8 -*-
'''
关于find_all()函数的详细用法
'''
from bs4 import BeautifulSoup
import requests
import re
##读取本机的文件
soup=BeautifulSoup(open("a.html","r",encoding="utf-8").read(),"html.parser")

# 需求一：想要找以 one开头的信息
print(soup.find_all("div",attrs={"class":"one."}))#结果为[]，看出：BeautifulSoup的方法用不了，返回正则法！
# print(soup.find_all("div",attrs={"class":re.compile("one.")}))
print(len(soup.find_all("div",attrs={"class":re.compile("one.")})))

# 需求二：两个属性的find_all怎么读取？
print(soup.find_all(["span","h1"])) #可以同时并列查询
# 再进一步
print(soup.find_all(["span","h1"],attrs={"aid":"1"}))  #aid毕竟不是id啊

# 需求三：怎么找所有的h标签
# print(soup.find_all(re.compile("h."))) #结果显示，找的过多了，接着修改
print(soup.find_all(re.compile("h[1-6]")))#标签名使用正则

#需求四：查找文本中内容包含 woshi
print(soup.find_all(text=re.compile("woshi.*")))

# 需求五：限定条数
print(soup.find_all(text=re.compile("woshi.*"),limit=2))  #limit限制取前几条

#注意：find_all,返回的是 列表；当该列表只有一个元素时，可用find代替
