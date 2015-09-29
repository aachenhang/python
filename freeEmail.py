# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json

mobile = '13726230735'
stime = '2015-08-21+10%3A20%3A51.297'
content = '测试一下短信能发么'
url = 'http://apis.baidu.com/shanghaidiyiinformation/smsinterface/smsinterface?name=test11&pwd=0390131DFF0CDCE885A33C2A155B&content='+content+'&mobile='+mobile+'&stime='+stime+'&sign=%E7%AC%AC%E4%B8%80%E4%BF%A1%E6%81%AF&type=pt&extno=123'


req = urllib2.Request(url)

req.add_header("apikey", "649945717e4090aaab24eda5dced6d2e")

resp = urllib2.urlopen(req)
content = resp.read()
if(content):
    print(content)
