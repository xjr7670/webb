#-*- coding:utf-8 -*-
import urllib
import re
import requests

#获取每页链接

page_url = []
girl_url = []
n = 0
def tuigirl():
    pageurl = get_pageurl()
    for l in pageurl:
        content = get_mainContent(l, r'class="gdnl"', r'<div class="fy3">')
        girlurl = get_girlurl(content)
        for u in girlurl:
            pic_content = get_mainContent(u, r'class="xjtpks"', r'class="foont"')
            get_picurl(pic_content)

def get_pageurl():
    for i in range(1, 8):
        source_url = "http://www.tuigirl.com/models/mlist?page=" + str(i)
        page_url.append(source_url)
    else:
        return page_url

def get_mainContent(url, start, end):
    get_girlist = urllib.urlopen(url).read()
    main_content_start = get_girlist.find(start)
    main_content_end = get_girlist.find(end, main_content_start)
    main_content = get_girlist[main_content_start:main_content_end]
    return main_content

def get_girlurl(content):
    domain = "http://www.tuigirl.com"
    url_start = content.find(r'/models')
    url_end = content.find('"', url_start)
    urlc = content[url_start:url_end]
    l = domain + urlc
    
    while url_start != -1:
        girl_url.append(l)
        s = open('link.txt', 'a+').write(l+'\r\n')
        url_start = content.find(r'/models', url_end)
        url_end = content.find('"', url_start)
        urlc = content[url_start:url_end]
        l = domain + urlc
    else:
        return girl_url

def get_picurl(pic_content):
    picurl = []
    domain = "http://www.tuigirl.com"
    
    pattern = re.compile(r'src="(.*?)"', pic_content)
    
    for pic in pattern:
        purl = domain + pic
        picurl.append(purl)
    else:
        for ul in picurl:
            download_pic(ul)
        else:
            print "finish page"

def download_pic(url):
    img = requests.get(url).content
    open('img' + str(n)+'.jpg', 'wb').write(img)
    n += 1
    

tuigirl()
