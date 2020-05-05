
#SSL验证  verify 以安全的方式访问网站
# import requests
# url="http://www.12306.cn"
# r=requests.get(url)
# # print(r.text)
# #乱码了。怎么办？
# print(r.content.decode("utf-8"))
#我有证书，看不出结果啦
###########程序改正
# import requests
# url="http://www.12306.cn"
# r=requests.get(url,verify=False)
# print(r.content.decode("utf-8"))
