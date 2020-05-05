'''
import requests
import re
import json
'''

# # 1. cookies
# import requests
# url="http://www.ibeifeng.com"
# response=requests.get(url)
# print(response.cookies)


# # 1.2 使用cookie传值的形式模拟登陆
# import requests
# url="http://www.antvv.com/login/dologin.php"
# # # 登录界面中，demo4为network中的返回文件。返回的是 response header中的set cookie#
# response=requests.post(url,data={'uname':'admin',"upwd":'123456'})
# cookie=response.cookies  #set_cookie变量,保存到本机上面
# # #再次登录，带上cookie
# url1="http://www.antvv.com/login/index.php"
# res1=requests.get(url1,cookies=cookie)
# print(res1.text)
# 注意，我这个地址是我自己的服务器 localhost，你们可能用不了的，


# #1.3 不适合请求地址多的情况，接着改进：
# #使用session方法，模拟成浏览器访问
# import requests
# s1=requests.session()
# s1.post('http://www.antvv.com/login/dologin.php',data={"uname":"admin","upwd":"123456"})
# response=s1.get('http://www.antvv.com/login/index.php')
# print(response.text)
