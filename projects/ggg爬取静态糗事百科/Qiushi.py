#-*- coding:utf-8 -*-
'''
首先，判断一下是静态网页还是动态网页,结果是静态网页
'''

from lxml import etree
import requests

url="https://www.qiushibaike.com/text/" #段子那里
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
r=requests.get(url,headers=headers)
html=etree.HTML(r.text)
list_div=html.xpath("//div[@class='col1 old-style-col1']/div")
save_info=[]
num = 0
for once_div in list_div:
    user_img=once_div.xpath("./div[1]/a[1]/img/@src")
    if user_img: #有可能会出现的匿名用户，这个时候取不到头像，
        user_img="https:"+user_img[0]
        user_name = once_div.xpath("./div[1]/a[2]/h2/text()")[0].strip()

        user_age=once_div.xpath("./div[1]/div/text()")[0]
        user_sex=once_div.xpath("./div[1]/div/@class")[0]
        user_sex=user_sex[14:-4]
        num +=1
    else:
        user_img="https://static.qiushibaike.com/images/thumb/anony.png?v=b61e7f5162d14b7c0d5f419cd6649c87"
        user_name="匿名用户"
        user_age=0
        user_sex="man"
    print(user_img)
# print(num)
# exit()


    user_content = ''.join(once_div.xpath("./a[1]/div/span/text()"))
    user_content=user_content.strip()
    save_info.append("%s,%s,%s,%s,%s"%(user_name,user_sex,user_age,user_img,user_content))
    #保存用户头像
    with open("./QiushiHeadimage/"+user_name+".jpg",'wb') as fileimg:
        r_img=requests.get(user_img,headers=headers,stream=True)
        # print(r.text())
        for j in r_img.iter_content(1024):
            fileimg.write(j)





#把用户信息保存到文件里
with open("Qiushi.txt",'a',encoding='utf-8') as file:
    for once_info in save_info:
        file.write(once_info+"\n")

