#-*- coding:utf-8 -*-
'''
    requests.get(url,params,**kwargs)#使用get请求访问网站
url 请求网址   params 附带参数
**kwargs 关键字参数
    cookis 请求时附带cookie
    data post请求时的参数
    files 上传文件 files={"file":****,"file":****}
    proxies
    verify
'''


# import requests
# import re
# url="http://www.ibeifeng.com"
# #requests.get(url,params,**kwargs) 使用get请求访问网站   url 请求网址   params 附带参数
# response=requests.get(url)
# #返回对象形式
# print(type(response))
# #查看状态码
# print(response.status_code)
# #查看编码
# print(response.encoding)
# #查看源代码 text 自动解析编码格式
# rep_text=response.text
# regx=re.compile("content=\"(.*?)\"")
# print(regx.findall(rep_text))
# print(response.text)
#
'''
情况一：默认解析编码是 gbk 。所以，有时候需要自定义解析编码，比如 utf-8 。代码如下
'''
# print(response.content.decode('utf-8'))
'''
情况二：返回的数据有时候是json格式的，需要转换为字典或者列表
'''
import requests
import re
url="https://github.com/timeline.json"
response=requests.get(url) #返回的是json格式的字符串
# ##原始做法
# # print(response.text)
# # # #由结果，推测返回的是否为字典格式
# # text=response.text
# # print(text('message'))
# #结果显示为字符串格式，无法得到键值,接下来怎么搞?
# # # #把返回到的json格式字符串转换为字典或者列表  该 json为requests模块内带的
text=response.json()
print(type(text))
# #求出键值
print(text['message'])



