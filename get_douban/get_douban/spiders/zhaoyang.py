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

def multiple_replace(text, idict):
    rx = re.compile('|'.join(map(re.escape, idict)))

    def one_xlat(match):
        return idict[match.group(0)]

    return rx.sub(one_xlat, text)

class zhaoyangSpider(scrapy.Spider):
    name = "zhaoyang"  # 这个name是你必须给它一个唯一的名字  后面我们执行文件时的名字
    # start_urls ='https://www.12345fund.com/html/login.html'
    # 这个列表中的url可以有多个，它会依次都执行，我们这里简单爬取一个
    # url = "https://movie.douban.com/top250"

    def start_requests(self):
        token=login()

        Result = range(158896,200000)
        # name = []
        for q in Result:
            url = 'https://www.12345fund.com/api/v1/fill_fund/get_basic_data?fund_id={}&token={}'.format(q, token)
            print(url)
            # r = requests.get(url).content.decode('utf8')
            user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
            headers = {'User-Agent': user_agent}
            yield scrapy.Request(url, callback=self.parse,meta={'fund_id':q},headers=headers)

    def parse(self, response):
        fund_id = response.meta['fund_id']
        item=zhaoyangItem()
        # response.body = response.body.decode()
        # item['fund_id'] =re.search('"fund_id":"(.+?)"', response.body.decode(), re.DOTALL).group(1)
        item["fund_full_name"]=re.search('"fund_name":(.+?),', response.body.decode(), re.DOTALL)
        item["foundation_date"] = re.search('"statistic_date":"(.+?) 00:00:00"', response.body.decode(), re.DOTALL)
        item["fund_manager"] = re.search('"fund_manager":(.+?),', response.body.decode(), re.DOTALL)
        item["fund_status"] = re.search('"fund_status":(.+?),', response.body.decode(), re.DOTALL)
        item["fund_manager_nominal"] = re.search('"fund_issue_org":\["(.+?)"\]', response.body.decode(), re.DOTALL)
        item["fund_member"] = re.search('"fund_member":(.+?),', response.body.decode(), re.DOTALL)
        item["fund_name"] = re.search('"fund_name":(.+?),', response.body.decode(), re.DOTALL)
        item["reg_code"] = re.search('"reg_code":(.+?),', response.body.decode(), re.DOTALL)
        item["fund_type_structure"]=re.search('"fund_type_allocation":(.+?),', response.body.decode(), re.DOTALL)
        item["open_date"] = re.search('"open_date":(.+?),', response.body.decode(), re.DOTALL)
        item["type_name"] = re.search('"fund_type_strategy":(.+?),', response.body.decode(), re.DOTALL)
        # item["typestandard_name"] = re.search('"manage_type":(.+?),', response.body.decode(), re.DOTALL)
        item["data_freq"] = re.search('"data_freq":(.+?),', response.body.decode(), re.DOTALL)
        item["fund_custodian"] = re.search('"fund_custodian_bank":(.+?),', response.body.decode(), re.DOTALL)
        item["locked_time_limit"] = re.search('"locked_time_limit":(.+?),', response.body.decode(), re.DOTALL)
        item["min_purchase_amount"] = re.search('"min_purchase_amount":(.+?)\}', response.body.decode(), re.DOTALL)
        item["open_date"] = re.search('"open_date":(.+?),', response.body.decode(), re.DOTALL)
        item["purchase_status"] = re.search('"purchase_status":(.+?),', response.body.decode(), re.DOTALL)
        item["fund_stockbroker"] = re.search('"fund_stockbroker":(.+?),', response.body.decode(), re.DOTALL)
        item["redemption_status"] = re.search('"redemption_status":(.+?),', response.body.decode(), re.DOTALL)
        item["recommendation_end"] = re.search('"recommendation_end":(.+?),', response.body.decode(), re.DOTALL)
        item["reg_time"] = re.search('"reg_time":(.+?),', response.body.decode(), re.DOTALL)
        item["orientation"] = re.search('"orientation":(.+?),"recommendation_end"', response.body.decode(), re.DOTALL)

        idict = {'null': None, '}': ''}
        print(time.asctime(time.localtime(time.time())))
        for i in item.keys():
            if item[i]:
                item[i] = item[i].group(1).strip('[]').replace('"','')
                item[i] = multiple_replace(item[i],idict)

                # if item[i]=='null':
                #     del item[i]
        item["data_source"] = 2
        item['fund_id'] = fund_id
        # item['fund_id'] = hashlib.md5(item['fund_name'].encode()).hexgidex()

        print(now2)
        return item




