
#正则表达式
# #1
# import re
# str1='1abchaha1abc'
# #span=(0, 8), match='1abchaha'>   #span=(0, 8), match='1abchaha'>
# regx=re.compile("(\dabc)haha\\1")   #此举可以简化写法，要求字符串中完全相同  span=(0, 12), match='1abchaha1abc'>
# print(regx.match(str1).group(1))
# #2  group()分组函数
# import re
# pattern=re.compile('(\w+)(\w+)')
# str1='hello worald,hahahahhahha efsfsd dsfdsfd'
# result=pattern.match(str1)
# print(result)           #<_sre.SRE_Match object; span=(0, 5), match='hello'>
# print(result.group())   #hello
# print(result.group(1))  #hell
# print(result.group(2))  #o

# #3 split
# import re
# str1="2018-01-28 12:10:20"
# regx=re.compile("[-:\s]")
# print(regx.split(str1))        #['2018', '01', '28', '12', '10', '20']
#4
# sub()
# import re
# str1="2018-01-28 12:10:20"
# regx=re.compile("[-:\s]")
# print(regx.sub(",",str1))    #2018,01,28,12,10,20
# print(regx.subn(",",str1))   #('2018,01,28,12,10,20', 5)
# 5 贪婪模式:在整个表达式匹配成功的前提下，尽可能多的匹配
# import re
# str1='aaa<p>hello</p>bbb<p>world</p>ccc'
# pattern=re.compile("<p>.*</p>")
# print(pattern.findall(str1))      # match模式不行！['<p>hello</p>bbb<p>world</p>']

# #非贪婪模式:在整个表达式匹配成功的前提下，尽可能少的匹配
# import re
# str1='aaa<p>hello</p>bbb<p>world</p>ccc'
# pattern=re.compile("<p>.*?</p>")
# print(pattern.findall(str1))      #['<p>hello</p>', '<p>world</p>']

# # #6
# # 匹配中文#  [\u4e00-\u9fa5]
# import re
# str1='你好，hello，帅哥'
# pattern=re.compile('\w+')
# print(pattern.findall(str1))      #['你好', 'hello', '帅哥']
# #
# pattern1=re.compile('[\u4e00-\u9fa5]')
# print(pattern1.findall(str1))      #['你', '好', '帅', '哥']


# # 7
# # finditer()
# import re
# str1='hello 123,world 321'
# pattern=re.compile('(\w+) (\d+)')
# for i in pattern.finditer(str1):
#     print(i.group(0))
#     hello 123
#     world 321
#     '''
#     print(i.group(1))
#     '''
#     hello
#     world
#     '''
#     print(i.group(2))
#     '''
#     123
#     321
#     '''


# 8、
# import re
# pa=re.compile('[a-zA-Z]{1}')
# str1='123abc456'
# print(re.finditer(pa,str1))
# <callable_iterator object at 0x022ADBB0>

# import re
# pattern=re.compile('([a-z][a-z][a-z])')
# str1='123abc456def789'
# result=pattern.finditer(str1)
# for i in result:
#     print(i.group(0))
#     # print(i.group(1))
#     # print(i.group(2))

