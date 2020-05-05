from bs4 import BeautifulSoup
import requests
import re
#设置请求网址

url="https://www.woyaogexing.com/gexing/zt/690691.html"
# 设置消息头，防封，现在只是设置了user-agent，模仿是正常的浏览器访问
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
# 请求该网站，
r=requests.get(url,headers=headers)
#把得到的html数据解析成bs4节点的形式
soup=BeautifulSoup(r.content.decode("utf-8"),'html.parser')


#爬取个性签名
signDiv=soup.find("div",attrs={"class":"cont_body"}) #找到这个div
all_p=signDiv.find_all("p",text=re.compile("^\d.*")) #找到div里面的所有的p标签，并且满足标签内文字为数字开头的
for once_p in all_p:
    once_str=once_p.string #取到每个标签内的文字
    print(re.sub("[\d\.\s]",'',once_str)) #把文字里的数字 点 空格替换为空，得到的就是个性签名