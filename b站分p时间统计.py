import requests as req
import re
import numpy as np
url = 'https://www.bilibili.com/video/'+input('请输入bv号')+'?spm_id_from=333.999.0.0'
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

r = req.get(url=url,headers=header)

allTime = re.findall(r'","duration":(.*?),"vid"',r.text,re.S)
# print(len(allTime))
# print(allTime[0])
allNumberTime = np.array(allTime,dtype=np.int32)
# print(allNumberTime)
sumTime = np.sum(allNumberTime[int(input('输入起始位置'))-1:int(input('输入结束位置'))])
print(str(round(sumTime/60//60))+'小时'+str(round(sumTime/60%60))+'分钟'+str(sumTime%60)+'秒')