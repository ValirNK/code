from bs4 import BeautifulSoup
import requests
import re
import time
import datetime
import os

urls = [
    'https://www.dns-shop.ru/product/ce717676673b1b80/24-60-sm-televizor-led-dexp-h24f7000cw-belyj/',
    # 'https://www.dns-shop.ru/product/7c0c6b08337d3332/4-smartfon-dexp-a440-8-gb-seryj/',
    # 'https://www.dns-shop.ru/product/604d038170e83333/split-sistema-royal-premium-arcs-07hpn1f1/',
    # 'https://www.dns-shop.ru/product/f1481b7e0f251b80/7-planset-dexp-ursus-s670-mix-32-gb-3g-fioletovyj/'
]

def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0)'}
    result = requests.get(url, headers=headers)
    print(result.text)
    return result.content

def main():
    for url in urls:
        source = get_html(url)


if __name__ == '__main__':
    tm = int(time.time()) # 1635405822
    req = requests.post('http://127.0.0.1:8888', data={'unixtime': tm})
    print(req.text)

