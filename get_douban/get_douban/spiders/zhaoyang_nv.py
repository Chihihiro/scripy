# _*_ coding: utf-8 _*_
import scrapy
from scrapy.http import Request
import hashlib
import urllib
import pandas as pd
import time
import requests
import re
from urllib import request
from http import cookiejar
import http.cookiejar
import urllib.request, urllib.parse, urllib.error
import http.cookiejar
import hashlib
from iosjk import to_sql
from sqlalchemy import create_engine
from items import zhaoyangItem
import re
import time
from engine import *

def login():
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
              'autologin': '1',
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
        print('-------------')
        response = opener.open(request)
        request = urllib.request.Request(post_URL, data=postdata, headers=headers, method='POST')
        response = opener.open(request)
        print(response.read().decode())
        # ll=re.search('"token":"(.+?)"',response,re.DOTALL).group(1)
        # print(ll)
    except urllib.error.URLError as e:
        print(e.code, ':', e.reason)

    cookie_jar.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
    for item in cookie_jar:
        print('Name = ' + item.name)
        print('Value = ' + item.value)

    get_request = urllib.request.Request(get_url, headers=headers)
    get_response = opener.open(get_request)
    print(get_response.read().decode())

    print('cookies 采集')
    data = open('E:\\pycharm\\get_douban\\get_douban\\cookie_jar.txt').read()
    print(data)

    pp = re.search(r'token\s+(.+?)\n.', data, re.DOTALL).group(1)
    token = str(pp)
    print(token)
    print('TOKEN')
    return token



class zhaoyangSpider(scrapy.Spider):
    name = "zhaoyang_nv"  # 这个name是你必须给它一个唯一的名字  后面我们执行文件时的名字
    # start_urls ='https://www.12345fund.com/html/login.html'
    # 这个列表中的url可以有多个，它会依次都执行，我们这里简单爬取一个
    # url = "https://movie.douban.com/top250"

    def start_requests(self):
        token=login()
        R=pd.read_sql("select fund_id from d_fund_info where fund_full_name is not NULL",engine5)
        Result=to_list(R)



        # name = []
        for i in Result:
            q=i[0]

            url = 'https://www.12345fund.com/api/v1/fill_fund/get_history_nav?fund_id={}&rows=5000&page=1&token={}'.format(q, token)
            print(url)
            # r = requests.get(url).content.decode('utf8')




            user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
            headers = {'User-Agent': user_agent}
            yield scrapy.Request(url, callback=self.parse,meta={'fund_id':q},headers=headers)

    def parse(self, response):
        fund_id = response.meta['fund_id']

        # response.body = response.body.decode()
        # item['fund_id'] =re.search('"fund_id":"(.+?)"', response.body.decode(), re.DOTALL).group(1)
        r=response.body.decode()
        # r = re.fi('"data":\[(.+?)\]', r)
        r = r.replace('{"message":"成功","data":[', '')
        r = r.replace('],"code":0}', '')
        r = r.replace('},', "}|")
        r = r.replace('null', '"null"')
        dd = r.split('|')
        o=[]
        for i in dd:
            print(i)
            a = eval(i)
            df = pd.DataFrame([a])
            print(df)
            o.append(df)
        result = pd.concat(o)
        df = result.iloc[:, [0, 3, 5]]
        df["fund_id"]=fund_id
        # df["added_nav"]=df["added_nav"].apply(lambda x: x.replace("null",None))
        df["added_nav"] = df["added_nav"].replace("null", np.nan)
        df["nav"] = df["nav"].replace("null", np.nan)
        df["source_id"]='020004'
        df["is_del"]=0
        print(df)
        try:
            to_sql("d_fund_nv", engine5, df, type="update")
            time.sleep(1.2)
        except BaseException:
            pass
        else:
            pass






