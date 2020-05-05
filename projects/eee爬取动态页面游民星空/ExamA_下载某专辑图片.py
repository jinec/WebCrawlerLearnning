from bs4 import BeautifulSoup
import requests
import json

url="http://pic.gamersky.com/home/getimagesindex?sort=time_desc&pageIndex=1&pageSize=50&nodeId=21086"
r=requests.get(url)
data_str=r.json()
print(type(data_str))  #<class 'str'>.仔细查看，此处做了数据反爬措施
# exit()
all_img_dict=json.loads(data_str) #把字符串解析成字典
for i,once_img_dict in enumerate(all_img_dict['body']):
    once_img=once_img_dict['originImg']
    img=requests.get(once_img,stream=True)

    with open("./OneAlbumPic/%s.jpg"%(once_img_dict['title']),'wb') as file:
        for j in img.iter_content(1024):
            file.write(j)
    print("共{0}个图片中的第{1}个图片-{2} 下载完成".format(len(all_img_dict['body']),i+1,once_img_dict['title']))