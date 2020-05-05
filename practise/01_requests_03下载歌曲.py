'''
注意：好像第一首歌下载不了
'''

# #下载歌曲
# import requests
# url="http://isure.stream.qqmusic.qq.com/C400000REfGM1pJbCp.m4a?vkey=152D5448654536CF51343594E1B38F02AF3E2A3EC57628668DC41D237BCBC62455E99BF5F8FF8EF3F3D534F604B0D7837DF34C2B376E902C&guid=7960966290&uin=0&fromtag=66"
# response=requests.get(url)
# #先作为文本
# # print(response.text)
# #作为文本，显示乱码；接着转为 字节形式
# print(response.content)
# 字节形式可以实现，接下来修改代码
# 1.2  初步完成
# import requests
# url="http://isure.stream.qqmusic.qq.com/C400000REfGM1pJbCp.m4a?vkey=152D5448654536CF51343594E1B38F02AF3E2A3EC57628668DC41D237BCBC62455E99BF5F8FF8EF3F3D534F604B0D7837DF34C2B376E902C&guid=7960966290&uin=0&fromtag=66"
# response=requests.get(url)
# songByte=response.content
# #写入文件
# file=open("jinec1.mp3","wb")
# file.write(songByte)
# file.close()

## 1.3
# # content 不太好，引入 stream=True.....raw...read
# import requests
# url="http://isure.stream.qqmusic.qq.com/C400000REfGM1pJbCp.m4a?vkey=152D5448654536CF51343594E1B38F02AF3E2A3EC57628668DC41D237BCBC62455E99BF5F8FF8EF3F3D534F604B0D7837DF34C2B376E902C&guid=7960966290&uin=0&fromtag=66"
# response=requests.get(url,stream=True)
# songByte=response.raw.read()
## print(songByte)
## 合成文件
# file=open("jinec1.mp3","wb")
# file.write(songByte)
# file.close()


# 1.4问题延伸
# 文件比较大时，为了节省内存空间，采取：2种方法
# 方式1，response.raw.read()中代入数值！以便一点一点去读如内存
# 方式2：合成文件中，引入自动关闭
# with open("jinec2.mp3",'wb')as file:
#     for i in response.iter_content(1024):
#         file.write(i)
