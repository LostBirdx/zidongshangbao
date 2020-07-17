import requests
headers  = {
    'Host':'reserve.25.team',
    'Connection':'keep-alive',
    'Content-Length':'659',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
    'content-type':'application/json',
    # 我自己的
	'token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo0ODAyMCwiZXhwIjoxNjg4OTUxMzU0LCJpc3MiOiJnaW4tYmxvZyJ9.l9pG0JCHYK9GlDpQr8m1KlIMxuk4mER4cGciKal2zuc',
    'referer':'https://servicewechat.com/wxd2bebfc67ee4a7eb/58/page-frame.html',
    'Accept-Encoding':'gzip,deflate,br'
}
data = {
	"content": {
		"0": "否",
		"1": "",
		"2": "",
		"3": "",
		"4": "",
		"5": "否",
		"6": "否",
		"7": "否",
		"8": "正常",
		"9": "37.2及以下",
		"10": "xx省xx市xx县 经纬度:123456789,987654321",
		"11": "否",
		"12": "",
		"13": "",
		"14": "正常（体温37.2及以下）",
		"15": "否",
		"16": ""
	},
	"version": 14,
	"stat_content": {
		"今日是否在京": "否",
		"今日是否在湖北？": "否",
		"今日是否“密切接触”疑似或确诊人群？": "否",
		"今日是否在集中隔离点隔离": "否"
	},
	"location": {
		"province": "湖南省",
		"country": "中国",
		"city": "邵阳市",
		"longitude": 123456789,
		"latitude": 987654321
	},
	"sick": "正常（体温37.2及以下）",
	"accept_templateid": ""
}
url = "https://reserve.25team.com/wxappv1/yi/addReport" #进入界面请求
response = requests.post(url,headers = headers,json = data)
html = response.text
print(response.status_code)  #返回一个json格式数据
print(html)

# OK ,搞定，成功提交问卷