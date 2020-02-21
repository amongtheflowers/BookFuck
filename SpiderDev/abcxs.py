# -*- coding: utf-8 -*-
# __author__ flower
# CreateTime 2020-02-21


'''
abc小说网抓取
'''

import requests
from bs4 import BeautifulSoup


headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        }

params = {'s': 3166108066185075505, 'ie': 'gbk', 'q': '财运天降'}
search_response = requests.get('https://www.abcxs.com/s.php', params=params).text

bookbox = BeautifulSoup(search_response, 'lxml').find_all('div', attrs={'class': 'bookbox'})
print(bookbox)

