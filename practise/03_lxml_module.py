####lxml的基础知识
from lxml import etree
ahtml=open("a.html",'r',encoding="utf-8").read()
# print(ahtml)
#etree 解析html
html=etree.HTML(ahtml)
print(type(html))
'''
xpath 取到的都是列表；
xpath的用法在浏览器查看源代码时可以直接用；
'''
#part1：选取节点的语法
print(html.xpath("/html/head/title")[0].text) #从根节点找title的文字部分  类似于BeautifulSoup中的ysoup.head.title
print(html.xpath("//title")[0].text) #直接找到title。类似soup.find()

outdiv=html.xpath("/html/body/div")
print(outdiv[0].xpath("./div/ul/li/span")[0].text) # ./ 当前目录

print(html.xpath("//li"))
print(html.xpath("//li[@mid='1']/span")[0].text) # //nodename[@属性名='属性值']
print(html.xpath("//li[@mid]/span")) #只想要属性名为mid的，不限定属性值；li[@mid="*"]是不正确的写法！

#print(html.xpath("//li[3]")) #取指定位置的li  从1开始
#print(html.xpath("//li[last()]")) #最后一个
#print(html.xpath("//li[last()-1]")) #倒数第二个
#print(html.xpath("//li[position()<4]")) #前三个
# 取6-8怎么办？返回值是列表，再进一步切片就可以了

print(html.xpath("//*[@mid]")) #找到任意属性为mid 的标签


#part2：取文本 两种方式
#1.标签后/text()
print(html.xpath("//span/text()"))
# 2.对某一个对象.text
print(html.xpath("//li[@mid='1']/span")[0].text)

##part3：取属性  标签后/@attrname
print(html.xpath("//li/@mid"))      #['1', '2', '3']
print(html.xpath("//li/@*"))        #['1', '2', '3', '1']，多了一个 a="1"

##part4：选取（有li元素大于2的)ul标签 不常用
print(html.xpath("//div[@class='one2']/ul[li>2]/li/text()")) #['1', '2', '3', '1', '2']

##part5：nodes()的用法。注意对比下面的异同点
print(html.xpath("//div[@class='one2']/node()"))  #类似于BeautifulSoup中的子节点contents
print(html.xpath("//div[@class='one2']/text()"))   #除去去其中的子节点模块

#part5：运算符的应用
print(html.xpath("//div[@class='one2'] | //div[@class='two']"))

##总结，2个方面
# （1）标签与text
# （2）“/”与“//”
