
import requests as req
import json
import  re
index=json.loads(input(''))
if index['method']=='primary':
    chapter=int(index['chapter'])-1
elif index['method']=='back':
    chapter=int(index['chapter'])-1-1
elif index['method']=='forward':
    chapter=int(index['chapter'])-1+1
with open('content.txt',mode='r',encoding='utf-8') as f:
    allUrl=f.read().split(',')
if chapter==-1:
    raise '这是第一章，无法回退'
url='https://www.xbiquge.la'+allUrl[chapter]
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
}

r = req.get(url=url,headers=header)
r.encoding = r.apparent_encoding
clearText = re.sub('\\r','',r.text)
title = re.findall(r'<h1>(.*?)</h1>',clearText,re.S)[0]
contents = re.findall(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<',clearText,re.S)
obj = []
ids = 1
for i in contents:
    obj.append({'id':ids,'content':i})
    ids+=1

dic = {
    'title':title,
    'content':obj,
    'chapter':chapter+1
}
dicJson = json.dumps(dic)
# print(dicJson)
# print(title,content)
# with open(file='book.json',mode='w',encoding='utf-8') as f:
#     f.write(dicJson)
print(dicJson)
# print(type(index['chapter']))
