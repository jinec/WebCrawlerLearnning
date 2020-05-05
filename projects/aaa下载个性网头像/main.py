import requests
import re

url="https://www.woyaogexing.com/touxiang/nv/2018/662775.html"
r=requests.get(url)
allText=r.content.decode('utf-8')
regx=re.compile("<img class=\"(.*?)\" src=\"(.*?)\"")  #空格、=、转行空格都不需要转义字符！  子模式
print(regx.findall(allText))
# 下载图片
num=0
for i,oneurl in regx.findall(allText):
    imgurl="https:"+oneurl
    r = requests.get(imgurl,stream=True)
    imgcontent = r.content
    file = open("./images/"+str(num)+".jpg", 'wb')
    file.write(imgcontent)
    file.close()
    num+=1
print("{}张图片已经下载完".format(num))

# str1="abc1hahaabc1"
#第一种写法
# regx=re.compile("(abc\d)haha\\1")
# print(regx.match(str1).group(0))
# 第二种写法
# print(re.match("(abc\d)haha\\1",str1).group(1))

#findall() 查找字符串中所有匹配的，返回列表形式
# regx=re.compile("abc")
# print(regx.findall(str1))
# str1="2018-09-11 11:20:20"
# regx=re.compile("[-:\s]")
# print(regx.sub(',',str1))
# print(regx.split(str1))


#匹配中文
# [\u4e00-\u9fa5]


