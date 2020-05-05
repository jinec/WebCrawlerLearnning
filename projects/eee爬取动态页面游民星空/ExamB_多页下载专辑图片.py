from bs4 import BeautifulSoup
import requests
import json
import os
import re
import time
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
#根据gid获取某一系列的所有图片路径，包含小图大图和标题
def one_group(gid):
    url="http://pic.gamersky.com/home/getimages?jsondata=%7B%22generalId%22%3A%22"+str(gid)+"%22%2C%22sort%22%3A%22hot_desc%22%2C%22pageIndex%22%3A1%2C%22pageSize%22%3A50%2C%22gameId%22%3A%220%22%2C%22tagId%22%3A%220%22%7D"
    #可以通过 “UrlEncode编码/UrlDecode解码 - 站长工具” 进行URL解析后查看来进行对比，这样比较清晰
    r=requests.get(url,headers=headers)
    json_str=r.json()
    group_img_dict=json.loads(json_str)
    # 大图路径，小图路径，itemTitle
    all_img=[]
    for once_img_dict in group_img_dict['body']:
        once_img=[]
        originImg=once_img_dict['originImg']
        smallImg=once_img_dict['smallImg']
        itemTitle=once_img_dict['title']
        itemTitle= re.sub("[\s]","_",itemTitle)#这个空格删除
        once_img.append(itemTitle)
        once_img.append(originImg)
        once_img.append(smallImg)
        # print(once_img)
        all_img.append(once_img)
    return all_img

def saveToFile(all_img):
    base_path = "./MulPagesPic" #基础文件夹
    save_path = base_path + "/" + all_img[0][0] #基础文件夹+组名
    #判断外层文件夹是否储存在
    if os.path.exists(save_path):  # 判断文件或者文件夹是否存在
        pass
    else:
        os.mkdir(save_path)  # 创建文件夹方法
    origin_path=save_path+"/originImg" #大图保存的路径
    small_path=save_path+"/smallImg" #小图保存的路径
    #判断路径是否存在，创建
    if os.path.exists(origin_path)==False:
        os.mkdir(origin_path)
    if os.path.exists(small_path)==False:
        os.mkdir(small_path)
    num=1
    for once_img in all_img: #从所有的图片列表中取到一张图片的信息
        # 请求一张图片大图的连接
        originImg=requests.get(once_img[1],headers=headers,stream=True)
        with open(origin_path+'/'+str(num)+'.jpg','wb') as file:
            for big in originImg.iter_content(1024):
                file.write(big)
        # 请求一张图片小图的连接
        smallImg=requests.get(once_img[2],headers=headers,stream=True)
        with open(small_path+'/'+str(num)+'.jpg','wb') as file1:
            # file.write(smallImg.raw.read())
            for small in smallImg.iter_content(1024):
                file1.write(small)
        num+=1

#获取一页中所有的gid
def getPageGid(pageid=1):
    url="http://pic.gamersky.com/home/getimagesindex?sort=time_desc&pageIndex="+str(pageid)+"&pageSize=50&nodeId=21089"
    r=requests.get(url,headers=headers)
    all_gid_str=r.json()
    all_gid_dict=json.loads(all_gid_str)
    all_gid=[]
    for once_gid_dict in all_gid_dict['body']:
        gid=once_gid_dict['generalId']
        all_gid.append(gid)
    # print(all_gid)
    # exit()
    return all_gid

if __name__ =="__main__":
    for page in range(1,3): #range生成页数.注意：此处每页上的专辑列表是动态加载的
        all_gid=getPageGid(page) #获取到这一页中的gid
        num=1
        for gid in all_gid:
            all_img=one_group(gid)
            saveToFile(all_img)

            print("第%d组下载成功"%(num))
            num+=1
            time.sleep(2) #每下载一组停2秒
        print("第%d页下载成功"%(page))
        time.sleep(10) #每下载一页停10秒
