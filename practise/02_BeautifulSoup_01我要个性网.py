#由于正则有些难，人们都不太会，所以引入 BeautifulSoup，其特点：按一层一层的节点来分析
#安装1 pip install beautifulsoup4
#安装2 conda install beautifulsoup4

#1 我要个性网
from bs4 import BeautifulSoup  #区分大小写
import requests            #get 我要个性网
import re
# # 反爬虫手段headers：User-Agent（伪装正常的浏览器访问），Referer（从哪个网页跳过来的）
url='https://www.woyaogexing.com/gexing/zt/690691.html'
# url="http://httpbin.org/get"  #伪静态,这句会干扰网页的读取
headers={
    "Referer":"https://www.baidu.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
}
r=requests.get(url,headers=headers)
print(r.encoding)
response_text=r.content.decode('utf-8')

# 2 引入BeautifulSoup
soup=BeautifulSoup(response_text,'html.parser') #第一个参数为html代码；第二个参数html.parser为 以何种方式去解析；
# print(soup)
print(type(soup))
#进一步取用什么符号？点（.）:按一层一层的节点来分析
# print(soup.head)
# print(soup.body)
print(soup.head.title)
#优点：好用！但有缺点，看下面：
print(soup.head.meta)
#只返回了3个中的第一个值，非列表：<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
###这个问题，怎么解决？


#3 引入四大对象：
# 3.1 取标签tag
print(soup.head.meta.name)
print(soup.head.meta.attrs)
print(soup.body.img.attrs)
# 3.2 取文本
# string属性
print(soup.head.title.string)
# strings属性,结果为迭代器：<generator object _all_strings at 0x02ADB720>
print(soup.head.strings)
for i in soup.head.strings:
    print(i)
# 3.3 BeautifulSoup 对象
print(soup.name) # [document]
print(soup.attrs) # {}


#4 回到开始的问题，怎么从“只返回了3个中的第一个值” 演变为 返回值是一个列表
# 4.1 contents的功能
print(soup.head)
print(soup.head.contents) #返回是一个列表，缺点是列表元素中含有“\n”。
#举例子：取到个性标签名
print(len(soup.body.contents)) #返回元素一共15个，怎么去其中的“\n”元素？
#小技巧
outdiv=soup.body.contents
while '\n' in outdiv:
    outdiv.remove('\n')
print(len(outdiv)) #返回元素还剩7个
# print(outdiv[2])

# 4.2 接下来一层一层的去遍历的话太麻烦了，我们用搜索吧。引入 find_all，列表返回
print(len(soup.find_all("div")))   #查找所有的div标签,共51个。
# print(soup.find_all("div",id='main')) #查找id='main'的div标签
print(soup.find_all("div",attrs={"class":"subnav-l z"}))#查找class='subnav-l z'的div标签
# 接下来，想一想怎么只要 里面的标签a？
print(len(soup.find_all("div",attrs={"class":"subnav-l z"})))
# thisclass = soup.find_all("div",attrs={"class":"subnav-l z"})
# print(thisclass[0].find_all("a"))
# for one_a in thisclass[0].find_all("a"):
#     print(one_a.string)

# 注意一：当属性较多时，保险起见，可以id 与class一起用
# print(soup.find_all("div",attrs={"class":"qmContMain wp mt10 cl"},id='main'))
# 注意二：上面这个class的内容太长了，从其性质出发，可以简写
# print(soup.find_all("div",attrs={"class":"qmContMain"},id='main')) #注意这个简写只适用于 class属性
# 看一下类似的其他例子
# print(soup.find_all("div",attrs={"class":"z"}))  #功能上，可以用后面的字符代替，但是这z返回的元素太多了。
#注意三：当返回的列表元素只有一个的时候，可以用 find()函数来代替 find_all()函数
thisclass = soup.find("div",attrs={"class":"subnav-l z"})
print(type(thisclass))#注意返回值不是列表，而是一个<class 'bs4.element.Tag'>对象
print(thisclass.find_all("a"))
for one_a in thisclass.find_all("a"):
    print(one_a.string)