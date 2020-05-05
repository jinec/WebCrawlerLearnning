from lxml import etree
import requests
import re

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
for page in range(3,5):  #其实现在只有第一页了
    url="http://www.budejie.com/"+str(page)
    r=requests.get(url,headers=headers)
    html=etree.HTML(r.content.decode('utf-8'))
    all_li=html.xpath("//div[@class='j-r-list']/ul/li")

    for one_li in all_li:
        uname=one_li.xpath("./div/div[2]/a/text()")[0]
        add_time=one_li.xpath("./div/div[2]/span//text()")[0]
        title=one_li.xpath("./div[2]/div/a/text()")[0]
        image=one_li.xpath("./div[2]/div[2]/a/img/@data-original")[0]
        print(uname,add_time,title,image)
        resp_img=requests.get(image,stream=True,headers=headers)
        houzhuiming=image[-4:]
        save_title=title[:15] #截取一下，不然去做名字的话，字符串太长了
        save_title=re.sub("[/\\\\:\*\?><\"|]",'',save_title)
        with open("./Budejie/"+save_title+houzhuiming,"wb") as file:
            for j in resp_img.iter_content(1024):
                file.write(j)

#/\*:?><"|
