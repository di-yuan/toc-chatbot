# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 18:44:54 2018

@author: Ju
"""

import requests
from bs4 import BeautifulSoup

pic = []

def search_pic(name):

    r = requests.get("https://www.google.com.tw/search?biw=1164&bih=593&site=webhp&tbm=isch&sa=100&q="+name)

    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'html.parser')
        con = soup.find('div', id = 'search').find('img').get('src')
  
        pic.clear()
        pic.append(con)