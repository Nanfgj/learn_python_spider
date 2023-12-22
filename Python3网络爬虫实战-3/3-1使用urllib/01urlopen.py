import socket
import urllib.request
import urllib.parse
import urllib.error
from urllib import request, parse

# 基本测试
# response = urllib.request.urlopen('https://www.python.org')
# print(response.read().decode('utf-8'))  # 获取网页源码
#
# print(type(response))  # <class 'http.client.HTTPResponse'>
#
# print(response.status)  # 200
# print(response.getheaders())
# print(response.getheader('Server'))  # nginx

# data参数
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())

# timeout
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')

# Request
# request = urllib.request.Request('https://python.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

# 设置多个参数
url = 'http://httpbin.org/post'
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
           'Host': 'httpbin.org'}
dict = {'name': 'Germey'}
data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))
