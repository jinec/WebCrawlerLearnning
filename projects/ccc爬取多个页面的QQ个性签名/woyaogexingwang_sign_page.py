from bs4 import BeautifulSoup
import requests
import re

headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
def download_onePage(url):

    # 设置消息头，防封，现在只是设置了user-agent，模仿是正常的浏览器访问

    # 请求该网站，
    r=requests.get(url,headers=headers)
    #把得到的html数据解析成bs4节点的形式
    soup=BeautifulSoup(r.content.decode("utf-8"),'html.parser')
    #爬取个性签名
    signDiv=soup.find("div",attrs={"class":"cont_body"}) #找到这个div
    all_p=signDiv.find_all("p",)[2:-2] #找到div里面的所有的p标签，并且满足标签内文字为数字开头的

    signList=[]
    for once_p in all_p:
        if once_p.find(['img','span']) == None:
            once_str = once_p.text  # 取到每个标签内的文字。此处如果用string就把 换行引进来了
            sign = re.sub("[\d\.\s]", '', once_str)  # 把文字里的数字 点 空格替换为空，得到的就是个性签名
            signList.append(sign)
        else:
            continue
    print(signList)

    return signList

def saveToFile(signList,filename="woyaogexing_sign.txt"):
    with open(filename,'a',encoding='utf-8') as file:
        for once_sign in signList:
            file.write(once_sign+"\n")

def getUrls():
    url="https://www.woyaogexing.com/gexing/"
    r=requests.get(url,headers=headers)
    soup=BeautifulSoup(r.content.decode('utf-8'),'html.parser')
    eight_url=soup.find_all("div",attrs={"class":"li_brief cl"})
    urlList=[]
    for once_url in eight_url:
        once_real_url="https://www.woyaogexing.com"+once_url.find("a",attrs={"class":"brief_title"}).attrs['href']
        urlList.append(once_real_url)
    return urlList


if __name__=="__main__":
    all_urls=getUrls()
    num=0
    for url in all_urls:
        signList=download_onePage(url)
        saveToFile(signList)
        num+=1
        print("第%d个网址签名下载成功"%(num))