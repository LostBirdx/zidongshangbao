
import requests
import sys
from datetime import datetime
import time
import math
import random

MAX_SLEEP_TIME = 60



headers = {
	'Host':'reserve.25team.com',
    'Connection':'keep-alive',
    'Content-Length':'678',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
    'content-type':'application/json',
	'token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo0ODAyMCwiZXhwIjoxNjk3NjcyNTYyLCJpc3MiOiJnaW4tYmxvZyJ9.y_o7Cspuhsg7LjsQa2T_xGSW6369oCSOkR1WntyaWTk',  #需要你自己抓取来使用自己的token
    'referer':'https://servicewechat.com/wxd2bebfc67ee4a7eb/82/page-frame.html',
    'Accept-Encoding':'gzip,deflate,br'
}
headers_lql = {
	  'Host':'reserve.25.team',
    'Connection':'keep-alive',
    'Content-Length':'659',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
    'content-type':'application/json',
	'token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo5NDU4NSwiZXhwIjoxNzM3NTU1NzY2LCJpc3MiOiJnaW4tYmxvZyJ9.RltPKjpuDwMvRY-9V5sfDtzDMGR9PthXHRhs5zK5Ei4',  #需要你自己抓取来使用自己的token
    'referer':'https://servicewechat.com/wxd2bebfc67ee4a7eb/58/page-frame.html',
    'Accept-Encoding':'gzip,deflate,br'
}
# data = {
# 	"content": {
# 		"0": "不在校-京外",
# 		"1": "",
# 		"2": "近期无返京计划",
# 		"3": "",
# 		"4": "",
# 		"5": "放假离校",
# 		"6": "重庆市垫江县桂溪街道桂西大道南段南阳公园 经纬度:107.33515,30.3268",
# 		"7": "否",
# 		"8": "37.3°C以下",
# 		"9": "正常",
# 		"10": "否",
# 		"11": "",
# 		"12": "",
# 		"13": "否",
# 		"14": "",
# 		"15": "否",
# 		"16": "均正常",
# 		"17": "否",
# 		"18": "否",
# 		"19": "",
# 		"20": "",
# 		"21": "否",
# 		"22": "否",
# 		"23": "否",
# 		"24": "是",
# 		"25": "20210323",
# 		"26": "",
# 		"27": "是",
# 		"28": "20210413",
# 		"29": "",
# 		"30": "是",
# 		"31": "20211219",
# 		"32": "",
# 		"33": "",
# 		"34": ""
# 	},
# 	"version": 20,
# 	"stat_content": {},
# 	"location": {
# 		"province": "重庆市",
# 		"country": "中国",
# 		"city": "",
# 		"longitude": 107.33515,
# 		"latitude": 30.3268
# 	},
# 	"sick": "",
# 	"accept_templateid": ""
# }

data_lql = {
	"content": {
		"0": "在京在校-集中住宿",
		"1": "汇才公寓",
		"6": "北京市昌平区城北街道上旧路中国石油大学 经纬度:116.24984212239583,40.21714735243056",
		"7": "否",
		"8": "37.3以下",
		"9": "正常",
		"10": "否",	
		"13": "否",
		"15": "否",
		"16": "均正常",
		"17": "否",
        "18": "否",
        "21": "否",
		"22": "否",
		"23": "否",
        "24": "是",
        "25": "2021.05.14",
		"27": "是",
		"28": "2021.06.15"
	},
	"version": 16,
	"stat_content": {},
	"location": {
		"province": "北京市",
		"country": "中国",
		"city": "",
		"longitude": 116.24984212239583,
		"latitude": 40.21714735243056
	},
	"sick": "",
	"accept_templateid": ""
}

data = {
	"content": {
		"0": "在京在校-集中住宿",
		"1": "汇才公寓",
		"2": "",
		"3": "",
		"4": "",
		"5": "",
		"6": "北京市昌平区城北街道中国石油大学汇才公寓4号楼 经纬度:116.23128,40.22077",
		"7": "否",
		"8": "37.3°C以下",
		"9": "正常",
		"10": "否",
		"11": "",
		"12": "",
		"13": "否",
		"14": "",
		"15": "否",
		"16": "均正常",
		"17": "否",
		"18": "否",
		"19": "",
		"20": "",
		"21": "否",
		"22": "否",
		"23": "否",
		"24": "是",
		"25": "20210323",
		"26": "",
		"27": "是",
		"28": "20210413",
		"29": "",
		"30": "是",
		"31": "20211119",
		"32": "",
		"33": "",
		"34": ""
	},
	"version": 20,
	"stat_content": {},
	"location": {
		"province": "北京市",
		"country": "中国",
		"city": "",
		"longitude": 116.23128,
		"latitude": 40.22077
	},
	"sick": "",
	"accept_templateid": ""
}

url = "https://reserve.25team.com/wxappv1/yi/addReport" #进入界面请求


print(datetime.now())
response_lql = requests.post(url,headers = headers_lql,json = data_lql)
html_lql = response_lql.text
print("lql:\n")
print(response_lql.status_code)  #返回一个json格式数据
print(html_lql)
#
response = requests.post(url,headers = headers,json = data)
html = response.text
print("xbb:\n")
print(response.status_code)  #返回一个json格式数据
print(html)
