from bs4 import BeautifulSoup
import requests
'''
智联招聘信息抓取
职位名称，公司名称，薪资水平，地理位置

查找 ：右键选择“查找网页源代码”后，发现找不到想要的data；但是按F12后选择“Elements”，发现其实存在的。
关键位置：按F12后，在功能中选择“network”-->“XHR”-->“sou?pageSize”。接着在 “preview”中便可以找到所需要的的“data”

'''

# url="https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=538&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%A1%8C%E6%94%BF%E5%8A%A9%E7%90%86&kt=3&lastUrlQuery=%7B%22pageSize%22:%2260%22,%22jl%22:%22538%22,%22kw%22:%22%E8%A1%8C%E6%94%BF%E5%8A%A9%E7%90%86%22,%22kt%22:%223%22%7D" #真正的链接
# r=requests.get(url)
# jobData=r.json()
# for once_data in jobData['data']['results']:
#     jobName=once_data['jobName']
#     companyName=once_data['company']['name']
#     money=once_data['salary']
#     position=once_data['city']['display']
#     print(jobName,companyName,money,position)

if __name__=="__main__":
    url="https://fe-api.zhaopin.com/c/i/sou?at=f96d2a6dc6154cd29b931e0ed66f4fca&rt=018b557965434557918ac2eb13458da8&_v=0.09721550&x-zp-page-request-id=65537611e13f4ab4b8f455449b6b5451-1588655687971-271840&x-zp-client-id=6e36ebbd-4eed-4270-9c92-21f635704379&MmEwMD=5e.LpXjMbNWsgvkcSraCTLvMH0Uqqwf1kXXVclIHMyk7pVvj5J8NBzH9DHN0_QIe8YlwKiZViDee.CRiiVhnT7XBg8horsnG2lR4YKlQt.KU0vZrgmvI48HbxrR7td5_3BYbWd5u0wUF8wom63f7B6tAsjWH.9xnr5EZ1W.UJl7Xv_BJ8w0EGl.3Sq1WxQsgaLKbuyqb0lxpRAY4VBQozo9BLeb3U1xmaaDbM0GSQyMs79y.wa0Gk2UMa1vkE5UhKbzYnHhWszugTxMYqnrl7UnqLb89W1Hv1T5.vw5q9b_r7qsSYVKzdUin7Wz.Ixf_jefzBgvPVAz3ar3WBzRGc7HewiC9B_w0BMp_D_OhqejkyKMY_6_kp7ITu70rp0vEF38IAUwJ88rGWeOE7cHLTPpz_"
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "referer":"https://sou.zhaopin.com/?jl=801&kw=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&kt=3",
    }
    r = requests.post(url,headers=headers,)
    print(r.status_code)
    exit()
    jobData = r.json()