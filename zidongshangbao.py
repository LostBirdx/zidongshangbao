import requests
import sys
sys.stdout = open('/media/lthpc/hd_auto/Liu/xiaobingbiao/zidongshangbao/somefile.txt', 'w')

headers  = {
    'Host':'reserve.25.team',
    'Connection':'keep-alive',
    'Content-Length':'659',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
    'content-type':'application/json',
    # 我自己的
	'token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo0ODAyMCwiZXhwIjoxNjk3NjcyNTYyLCJpc3MiOiJnaW4tYmxvZyJ9.y_o7Cspuhsg7LjsQa2T_xGSW6369oCSOkR1WntyaWTk',  #需要你自己抓取来使用自己的token
    'referer':'https://servicewechat.com/wxd2bebfc67ee4a7eb/58/page-frame.html',
    'Accept-Encoding':'gzip,deflate,br'
}
headers_dky = {
	  'Host':'reserve.25.team',
    'Connection':'keep-alive',
    'Content-Length':'659',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
    'content-type':'application/json',
	'token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozNzQxOSwiZXhwIjoxNzE5NzIzMjgwLCJpc3MiOiJnaW4tYmxvZyJ9.y8fT1eQRlap3_T7aQPb6f6I79OcbSfdMcyzcK7979_Y',  #需要你自己抓取来使用自己的token
    'referer':'https://servicewechat.com/wxd2bebfc67ee4a7eb/58/page-frame.html',
    'Accept-Encoding':'gzip,deflate,br'
}
headers_cxy = {
	  'Host':'reserve.25.team',
    'Connection':'keep-alive',
    'Content-Length':'659',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
    'content-type':'application/json',
	'token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo0ODE2OSwiZXhwIjoxNzIwMjY5NzAwLCJpc3MiOiJnaW4tYmxvZyJ9.8VEOSocH1vydu-GSXsg4zEEedQPMkYZsvp4uZx5mnvI',  #需要你自己抓取来使用自己的token
    'referer':'https://servicewechat.com/wxd2bebfc67ee4a7eb/58/page-frame.html',
    'Accept-Encoding':'gzip,deflate,br'
}


headers_zsy = {
	  'Host':'reserve.25.team',
    'Connection':'keep-alive',
    'Content-Length':'659',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
    'content-type':'application/json',
	'token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo0NzQ5NywiZXhwIjoxNzIxMzYyMDU4LCJpc3MiOiJnaW4tYmxvZyJ9.eQrP6xKTrUTDhn_gbUurLE7qOS2ojLUbqtUjp86MJXc',  #需要你自己抓取来使用自己的token
    'referer':'https://servicewechat.com/wxd2bebfc67ee4a7eb/58/page-frame.html',
    'Accept-Encoding':'gzip,deflate,br'
}



data_cxy = {
	"content": {
		"0": "在京,在校集中住宿",
		"1": "之前已返校或未离校",
		"4": "",
		"5": "低风险",
		"6": "北京市昌平区城北街道清秀园(南区)中国石油大学润杰公寓 经纬度:116.24186930338541,40.21457465277778",
		"7": "正常",
		"8": "37.3以下",
		"9": "绿色",
		"10": "均正常",	
		"11": "无",
		"12": "否",
		"13": "",
		"14": ""
	},
	"version": 16,
	"stat_content": {},
	"location": {
		"province": "北京市",
		"country": "中国",
		"city": "",
		"longitude": 116.24186930338541,
		"latitude": 40.21457465277778
	},
	"sick": "",
	"accept_templateid": ""
}

data = {
	"content": {
		"0": "在京,在校集中住宿",
		"1": "之前已返校或未离校",
		"4": "",
		"5": "低风险",
		"6": "北京市昌平区城北街道中国石油大学(北京)后勤楼 经纬度:116.24984212239583,40.21714735243056",
		"7": "正常",
		"8": "37.3以下",
		"9": "绿色",
		"10": "均正常",
		"11": "无",
		"12": "否",
		"13": "",
		"14": ""
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

data_dky = {
	"content": {
		"0": "在京,在校集中住宿",
		"1": "之前已返校或未离校",
		"4": "",
		"5": "低风险",
		"6": "北京市昌平区城北街道中国石油大学(北京)汇才公寓 经纬度:116.24984212239583,40.21714735243056",
		"7": "正常",
		"8": "37.3以下",
		"9": "绿色",
		"10": "均正常",
		"11": "无",
		"12": "否",
		"13": "",
		"14": ""
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

data_zsy = {
	"content": {
		"0": "在京,在校集中住宿",
		"1": "之前已返校或未离校",
		"4": "",
		"5": "低风险",
		"6": "北京市昌平区城北街道中国石油大学(北京)汇才公寓 经纬度:116.24984212239583,40.21714735243056",
		"7": "正常",
		"8": "37.3以下",
		"9": "绿色",
		"10": "均正常",
		"11": "无",
		"12": "否",
		"13": "",
		"14": ""
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

url = "https://reserve.25team.com/wxappv1/yi/addReport" #进入界面请求
#xbb
response = requests.post(url,headers = headers,json = data)
html = response.text
print(response.status_code)  #返回一个json格式数据
print(html)

#dky
response_dky = requests.post(url,headers = headers_dky,json = data_dky)
html_dky = response_dky.text
print(response_dky.status_code)  #返回一个json格式数据
print(html_dky)


response_zsy = requests.post(url, headers = headers_zsy, json = data_zsy)
html_zsy = response_zsy.text
print(response_zsy.status_code)  #返回一个json格式数据
print(html_zsy)
# OK ,搞定，成功提交问卷





