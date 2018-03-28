# _*_ coding: utf-8 _*_
# import pandas as pd
# import time
# import requests
# import re
# from urllib import request
# from http import cookiejar
# import http.cookiejar
# import urllib.request, urllib.parse, urllib.error
# import http.cookiejar
# import hashlib
# login_url = 'https://www.12345fund.com/html/login.html'
# post_URL = 'https://www.12345fund.com/api/v1/account/login_safe'
# get_url = 'https://www.12345fund.com/html/fundDetail.html?fundId=102015'  # 利用cookie请求訪问还有一个网址
#
#
#
# ID=[]
# for n in range(1,999999):
#     n=str(n)
#     if len(n)==1:
#         y='00000'+n
#         ID.append(y)
#     elif len(n)==2:
#         y='0000'+n
#         ID.append(y)
#     elif len(n)==3:
#         y='000'+n
#         ID.append(y)
#     elif len(n)==4:
#         y='00'+n
#         ID.append(y)
#     elif len(n)==5:
#         y='0'+n
#         ID.append(y)
#     else:
#         y=n
#         ID.append(y)
# print(ID)
#
# for I in ID:
#     hash = hashlib.md5()
#     hash.update(I.encode('utf-8'))
#     hs1 = hash.hexdigest()
#     hash = hashlib.sha1()
#     hash.update(hs1.encode('utf8'))
#     passw = hash.hexdigest()
#     # print(passw)
#
#     values = {'account_name': 'E00002199',
#               'autologin':'1',
#               'passwordmd5': passw}
#
#
#     postdata = urllib.parse.urlencode(values).encode()
#     user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
#     headers = {'User-Agent': user_agent}
#
#     cookie_filename = 'cookie_jar.txt'
#     cookie_jar = http.cookiejar.MozillaCookieJar(cookie_filename)
#     handler = urllib.request.HTTPCookieProcessor(cookie_jar)
#     opener = urllib.request.build_opener(handler)
#
#     request = urllib.request.Request(login_url, headers=headers)
#     # print(request)
#     response = opener.open(request)
#     request = urllib.request.Request(post_URL, data=postdata, headers=headers, method='POST')
#     response = opener.open(request)
#     print(response.read().decode())
#     a=response.read().decode()
#     vv='没有权限'
#     if vv not in a:
#         print(I)
#     else:
#         pass

    # try:
    #     print ('-------------')
    #     response = opener.open(request)
    #     request = urllib.request.Request(post_URL, data=postdata, headers=headers,method='POST')
    #     response = opener.open(request)
    #     print(response.read().decode())
    #     # ll=re.search('"token":"(.+?)"',response,re.DOTALL).group(1)
    #     # print(ll)
    #
    #
    #
    # except urllib.error.URLError as e:
    #     print(e.code, ':', e.reason)


    # cookie_jar.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
    # for item in cookie_jar:
    #     print('Name = ' + item.name)
    #     print('Value = ' + item.value)
    #
    # get_request = urllib.request.Request(get_url, headers=headers)
    # get_response = opener.open(get_request)
    # print(get_response.read().decode())
    #
    # print ('cookies 采集')
    #
    #
    #
    # data = open('C:\\Users\\63220\\PycharmProjects\\QQX\\cookie_jar.txt').read()
    # print(data)
    #
    # pp = re.search(r'token\s+(.+?)\n.',data,re.DOTALL).group(1)
    # token = str(pp)
    # print(token)
    # print ('TOKEN')