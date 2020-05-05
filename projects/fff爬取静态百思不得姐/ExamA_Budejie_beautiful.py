'''
首先，通过右键“查看网页源代码”来查看该网页是静态的还是动态的；
在固定元素处，右键选择“检查”，可以快速定位到其在“F12-Elements”中的源码。
总结：beautiful的定位需要一级一级的递进，有点麻烦，于是引入 lxml。
'''
from bs4 import BeautifulSoup
import bs4
import requests
import re

url="http://www.budejie.com/"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
r=requests.get(url,headers=headers)
soup=BeautifulSoup(r.text,'html.parser')
j_r_c=soup.find("div",attrs={'class':"j-r-c"}) #用这个命令，可以准确定位。因为如果只用下一句进行查询，则找到4个元素。
all_list=j_r_c.find_all("div",attrs={'class':"j-r-list"})

for once_list in all_list:
    once=once_list.contents
    while "\n" in once:  #beautiful中总会引入 '\n'，是一个小问题
        once.remove('\n')

    once_li=once[0].contents
    while "\n" in once_li:
        once_li.remove('\n')

    while "段子" in once_li: #具体打印出来，才发现了这个问题
        once_li.remove("段子")

    for one_li in once_li:
        user_name=one_li.find('a',attrs={"class":"u-user-name"}).text
        add_time=one_li.find('span',attrs={"class":"u-time"}).text
        title=one_li.find('div',attrs={'class':"j-r-list-c-desc"}).find('a').text
        image=one_li.find("div",attrs={"class":"j-r-list-c-img"}).find("img",attrs={"class":"lazy"}).attrs['data-original']#这一句为什么这么长？爬虫与反爬虫之间的斗争。
        print(image)
