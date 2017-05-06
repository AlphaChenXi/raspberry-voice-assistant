#coding=utf-8
import socket
import time
import sys
import os
import json
import requests
import urllib2

reload(sys)
sys.setdefaultencoding( "utf-8" ) 

#将HOST_IP和HOST_PORT更改为你的树莓派ip和端口
HOST_IP = "192.168.43.173"
HOST_PORT = 7653

#将client_id和client_secret更改为你自己注册的
auth_url = 'https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=*******&client_secret=*******&'
res = urllib2.urlopen(auth_url)
json_data = res.read()
access_token=json.loads(json_data)['access_token']

print("Starting socket: TCP...")
host_addr = (HOST_IP, HOST_PORT)
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
print("TCP server listen @ %s:%d!" %(HOST_IP, HOST_PORT) )
socket_tcp.bind(host_addr)
socket_tcp.listen(1)

print("Receiving package...")
while True:
	try:
		socket_con, (client_ip, client_port) = socket_tcp.accept()
		data = socket_con.recv(100).split('\n')[0]

		if len(data)>0: 
			print("Received: %s" %data)
#将key更改为你自己的key
		tulingurl = 'http://www.tuling123.com/openapi/api?key=******&userid=002&info='+data
		databack = requests.get(tulingurl).text

		value = json.loads(databack)

		subvalue = value['code']
		if subvalue==100000:
	   		readcontent =value['text']

		elif subvalue==200000:
			readcontent= value['text']

		elif subvalue==302000:
			readcontent= value['text']
			if value['list']:
				i = 1
				for news in value['list']:
					readcontent = readcontent +','+ str(i) + ',来自' + news['source'] + ',内容是,' + news['article']
					i = i + 1
		elif subvalue==308000:
			readcontent= value['text']
			if value['list']:

				for cai in value['list']:
					readcontent = readcontent+ cai['name'] + '，材料是' + cai['info']
			break
		elif subvalue==40001:
			readcontent='参数错误'
		elif subvalue==40002:
			readcontent='请求内容为空'
		elif subvalue==40004:
			readcontent='当天请求次数已用完'
		elif subvalue==40007:
			readcontent='数据格式异常'  
		else:
			readcontent='出错了请重说'	
		print 'reply:'+readcontent


		#将cuid更改为你自己的cuid
		readurl = "http://tsn.baidu.com/text2audio?tex="+readcontent+"&lan=zh&cuid=*******&ctp=1&tok="+access_token
		readcom ='mplayer "'+readurl+'\"'
			
		try:
			os.system(readcom)
		except:
			print 'something wrong please try again'		
		time.sleep(1)
		continue
	except Exception as e:
		print e  
		socket_tcp.close()
		sys.exit(1)
