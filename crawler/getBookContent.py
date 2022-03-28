from base64 import decode, encode
import requests  as req
from lxml import etree
import json
import re
bookname = input()
bookname =  re.sub(r'"','',bookname)


url = 'https://www.xbiquge.la/modules/article/waps.php?searchkey='+bookname
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
}

r= req.post(url=url,headers=header)
r.encoding = r.apparent_encoding
htmlEtree = etree.HTML(r.text)
content = htmlEtree.xpath('//table')[0]
content= str(etree.tostring(content))
contentUrl = re.findall(r'<a href="(.*?)" target="_blank">',content,re.S)[0]




url = contentUrl
r = req.get(url=url,headers=header)
r.encoding = r.apparent_encoding
htmlEtree = etree.HTML(r.text)
title = htmlEtree.xpath('//*[@id="info"]/h1/text()')
content = htmlEtree.xpath('//*[@id="list"]/dl/dd/a/@href')
contentName = htmlEtree.xpath('//*[@id="list"]/dl/dd/a/text()')
contentName.insert(0,title[0])
strContent = ','.join(content)
strContentName = '---'.join(contentName)
with open('content.txt',mode='w',encoding='utf-8') as f:
    f.write(strContent)
with open('contentName.txt',mode='w',encoding='utf-8') as f:
    f.write(strContentName)

print(json.dumps('更新目录成功'))