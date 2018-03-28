# _*_ coding: utf-8 _*_
import pandas as pd
import time
import requests
from random import choice
from urllib.error import URLError, HTTPError
import re
from http import cookiejar
import http.cookiejar
import urllib.request as rq, urllib.parse, urllib.error
import http.cookiejar
import hashlib
login_url = 'https://www.12345fund.com/html/login.html'
post_URL = 'https://www.12345fund.com/api/v1/account/login_safe'
get_url = 'https://www.12345fund.com/html/fundDetail.html?fundId=102015'  # 利用cookie请求訪问还有一个网址

hash = hashlib.md5()
hash.update('339377'.encode('utf-8'))
hs1 = hash.hexdigest()
hash = hashlib.sha1()
hash.update(hs1.encode('utf8'))
passw = hash.hexdigest()
print(passw)

values = {'account_name': 'E00002199',
          'autologin':'1',
          'passwordmd5': passw}


postdata = urllib.parse.urlencode(values).encode()
user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
headers = {'User-Agent': user_agent}

cookie_filename = 'cookie_jar.txt'
cookie_jar = http.cookiejar.MozillaCookieJar(cookie_filename)
handler = urllib.request.HTTPCookieProcessor(cookie_jar)
opener = urllib.request.build_opener(handler)

request = urllib.request.Request(login_url, headers=headers)
try:
    print ('-------------')
    response = opener.open(request)
    request = urllib.request.Request(post_URL, data=postdata, headers=headers,method='POST')
    response = opener.open(request)
    print(response.read().decode())
except urllib.error.URLError as e:
    print(e.code, ':', e.reason)

cookie_jar.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
for item in cookie_jar:
    print('Name = ' + item.name)
    print('Value = ' + item.value)

get_request = urllib.request.Request(get_url, headers=headers)
get_response = opener.open(get_request)
print(get_response.read().decode())

print ('cookies 采集')



data = open('C:\\Users\\63220\\PycharmProjects\\QQX\\cookie_jar.txt').read()
print(data)

pp = re.search(r'token\s+(.+?)\n.',data,re.DOTALL).group(1)
token = str(pp)
print(token)
print ('TOKEN')
# exit()

# token采集结束-------------------------------------------------------------------------------------------------------

fileobj = open('C:\\Users\\63220\\Desktop\\org914.txt','r')
try:
    strings = fileobj.read()
finally:
    fileobj.close()
x= strings.split('\n')
print(x)


Result=[]

for q in x:
    url='https://www.12345fund.com/api/v1/dt_search/search_like?all_name={}&token={}'.format(q,token)
    print(url)
    # proxy_list = [{'https': '180.169.5.126'}, {'https': '120.77.210.59'}, {'https': '175.155.24.8'},
    #               {'https': '218.75.144.25'}, {'https': '46.191.239.111'}, {'https': '61.178.238.122'},
    #               {'https': '178.33.62.155'}, {'https': '188.38.105.21'}, {'https': '138.117.143.226'},
    #               {'https': '181.39.223.96'}, {'https': '177.66.245.186'}, {'https': '180.76.134.106'}]
    proxy_list = [{'https': '220.166.188.245:9728'}]
    proxy = choice(proxy_list)
    # for proxy in proxy_list:
    print(proxy)

    proxy_support = rq.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_support)
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen(url)
    html = response.read().decode("utf-8")
    print(html)
    r = html
    print(proxy, '正确')





    #
    # html = response.read().decode("utf-8")
    # print(html)
    # r=html
    print('down')
    exit()

