
import imp


import time
num = 1
while True:
    time.sleep(1)
    num += 1
    with open('检测.txt',mode='w',encoding='utf-8') as f:
        f.write(str(num//60)+'分钟')

