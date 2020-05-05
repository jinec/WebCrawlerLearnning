#-*- coding:utf-8 -*-
# 上传文件
#引入一个专门用来测试 requests请求的网站  http://www.httpbin.org/ 里有很多接口
#文件上传必须用 post
# 1.1
import requests
#先本地文件读取,，转为字典
file_dict={'file':open('a.txt','rb')}
#
url="http://www.httpbin.org/post"   #这个网址并不是 浏览器中的地址！！！
response=requests.post(url,files={'file':open('a.txt','rb')})
print(response.text)
# '''
#  "files": {
#     "file": "hello word!"
#   },
# '''
#多试试
# #1.2
# 代入 data
# import requests
# url="http://www.httpbin.org/post"
# response=requests.post(url,data={"aaa":"bbb"})
# print(response.text)
# '''
# "form": {
#     "aaa": "bbb"
#   },
# '''
# #1.3
# json模块  用的不多，多用字典形式
# # import json
# #小普及
# ## 把字典转为 json
# # dict1={"aaa":"bbb"}
# # print(json.dumps(dict1))
# #把json转为字典，用  loads
# #例子
# import json
# import requests
# url="http://www.httpbin.org/post"
# response=requests.post(url,data=json.dumps({"aaa":"bbb"}))
# print(response.text)
# '''
#   "json": {
#     "aaa": "bbb"
#   },
# '''