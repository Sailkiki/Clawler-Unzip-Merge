# coding=utf-8
import json
import re
import os
import sys
import time
from urllib.request import urlretrieve
import requests
from lxml import etree

ff = open("Log.txt", "w+")

url = "https://theme.npm.edu.tw/opendata/DigitImageSets.aspx?Key=^^2&pageNo="

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
}

##我是2680 - 3018 大概是298-336页
##i为页数， 一页9个文物
for i in range(298, 337):
    temp1 = url
    url += str(i)
    resp = requests.get(url, headers=head, stream=True)
    time.sleep(1)
    resp.encoding = 'utf-8'
    et = etree.HTML(resp.text)
    ww = et.xpath('//ul[@class="painting-list"]/li/a/@href')
    # print(ww)


    for j in range(0, len(ww)):
        resp2 = requests.get("https://theme.npm.edu.tw/opendata/"+ww[j], headers=head, stream=True)
        resp2.encoding = 'utf-8'
        obj = re.compile(r'<li><span>(?P<ID>.*?)</span>(?P<ID_info>.*?)</li>'
                         r'<li><span>(?P<Dynasty>.*?)</span>(?P<Dy_info>.*?)</li>'
                         r'<li><span>(?P<Class>.*?)</span>(?P<Cl_info>.*?)</li>'
                         r'<li><span>(?P<Function>.*?)</span>(?P<Func_info>.*?)</li>'
                         r'<li><span>(?P<Matreial>.*?)</span>(?P<Ma_info>.*?)</li>')
        res = obj.finditer(resp2.text)
        time.sleep(1)

        for item in res:
            data = {}
            ID = item.group("ID")
            ID_info = item.group("ID_info")
            data[ID] = ID_info

            Dynasty = item.group("Dynasty")
            Dy_info = item.group("Dy_info")
            data[Dynasty] = Dy_info

            Class = item.group("Class")
            Cl_info = item.group("Cl_info")
            data[Class] = Cl_info

            Function = item.group("Function")
            Func_info = item.group("Func_info")
            data[Function] = Func_info

            Matreial = item.group("Matreial")
            Ma_info = item.group("Ma_info")
            data[Matreial] = Ma_info

            jsonStr = json.dumps(data)
            print(json.dumps(data, ensure_ascii=False), file=ff, flush=True)
            print(json.dumps(data, ensure_ascii=False), file=sys.stdout)

            ##在目录下新建文件夹Origin_JSON, 并且把网页上的第一段json做成json文件并保存
            with open ('./Origin_JSON/{}.json'.format(ID_info), 'w') as fp:
                json.dump(data, fp, ensure_ascii=False)

            ##下载模块，下载压缩包, 存入zips文件夹
            et2 = etree.HTML(resp2.text)
            urlList = et2.xpath("//div[@class='project-img']/a/@href")
            temp = "https://theme.npm.edu.tw/opendata/"
            temp += urlList[0]
            r = requests.get(temp, headers=head, stream=True)
            time.sleep(1)
            with open("./zips/{}.zip".format(ID_info), "wb") as code:
                code.write(r.content)


    print("第{}页采集成功！".format(i))
    url = temp1
