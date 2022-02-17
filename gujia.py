import requests as req
import time
from openpyxl import Workbook
import random
import re
import os

def get_code_list() -> list:
    
    '''获取所有的股票代码'''
    code_list=[]
    head={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
        }
    for i in range(1,128):
        try:
            print('正在获取第'+str(i)+'张股票代码表')
            if i%10==0:
                time.sleep(2)
            url='http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=1110&TABKEY=tab1&PAGENO='+str(i)+'&random=0.65254399559621'

            r=req.get(url=url,headers=head)
            text1=r.text
            data=re.findall(r'"agdm":"([03].*?)"',text1)
            code_list=code_list+data
            print('获取第'+str(i)+'张股票代码表成功')
        except:
            print('获取第'+str(i)+'张股票代码表失败')
    # print(code_list)
    str_code_list=str(code_list).replace('[','')
    str_code_list=str_code_list.replace(']','')
    with open('股票代码表.txt',mode='w') as file:
        file.write(str_code_list)
    
    return code_list

attr=['爬取时间','股票代码','名称','昨收','开盘价','现价','最高价','最低价','涨跌','涨跌幅']
# url='http://www.szse.cn/api/market/ssjjhq/getTimeData?random=0.12120877863196888&marketId=1&code=000001'
# url='http://www.szse.cn/api/market/ssjjhq/getTimeData?random=0.7261418184125608&marketId=1&code=301188'

def get_stock_price(url:str):
    '''返回个体股票['爬取时间','股票代码','名称','昨收','开盘价','现价','最高价','最低价','涨跌','涨跌幅']等信息'''
    head={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}
    r= req.get(url,headers=head)
    # print(r.status_code)
    # print(r.text)
    json= r.json()
    date_time=json['datetime']
    code= json['data']['code']
    name=json['data']['name']
    zuoshou=json['data']['close']
    open=float(json['data']['open'])
    now=float(json['data']['now'])
    high=float(json['data']['high'])
    low=float(json['data']['low'])
    delta=float(json['data']['delta'])
    deltaPercent=float(json['data']['deltaPercent'])/100
    
    data=[date_time,code,name,zuoshou,open,now,high,low,delta,deltaPercent]
    return data

    
def save_data() -> None:  
    '''持久保存股票信息'''
    wb=Workbook()
    ws=wb.active
    datetime=time.strftime("%Y-%m-%d %H:%M:%S")
    datetime=datetime.replace(':','-')
    ws.title=datetime
    ws.append(attr)
    # code_list=get_code_list()
    gard=0
    if os.path.exists('股票代码表.txt'):
        with open('股票代码表.txt',mode='r',encoding='utf-8') as f:
            code_list=f.read().replace(" ",'')
        code_list=code_list.replace("'","").split(',')
        # print('在的')
    else:
        # print('不在')
        code_list=get_code_list()
    if not os.path.exists('股价'):
        os.makedirs('股价')
    

    for i in code_list:
        gard=gard+1
        print('第'+str(gard)+'次爬取公司股票信息')
        try:
            # if gard==2:
            #     break
            time1=random.randint(1,2)
            time.sleep(time1)

            url='http://www.szse.cn/api/market/ssjjhq/getTimeData?random=0.12120877863196888&marketId=1&code='+i

            data=get_stock_price(url)
            ws.append(data)
            print('第'+str(gard)+'次爬取公司股票信息成功')
            if gard%10==0:
                wb.save('股价/'+datetime+'股价表.xlsx')
        except:
                print('第'+str(gard)+'次爬取失败,url:'+url)
                    # defaul=['第'+str(i)+'次爬取失败,url:'+url]
                    # ws.append(defaul)
                continue

    wb.save('股价/'+datetime+'股价表.xlsx')
    wb.close()
    print('处理完成')
    


save_data()



    















# if r.status_code != 200:
#     print('状态码异常')
