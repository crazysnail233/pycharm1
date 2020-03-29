import requests
from lxml import etree
from urllib import request
import os
import re


def parse_page(url):
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
   }
    r = requests.get(url,headers=headers)
    r.raise_for_status = r.apparent_encoding
    text = r.text
    html = etree.HTML(text)
    imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
    for img in imgs:
        img_url = img.get('data-original')
        alt = img.get('alt')
        suffix = os.path.splitext(img_url)[1]
        alt = re.sub(r'[？,:]','',alt)
        filename1 = alt + suffix
        print(filename1)
        request.urlretrieve(img_url,filename1)



def main():
    for x in range(1,101):
        url = f'https://www.doutula.com/photo/list/?page={x}'
        parse_page(url)
        break

if __name__ =='__main__':
    main()