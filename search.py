# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 19:04:15 2018

@author: Ju
"""

import requests
from bs4 import BeautifulSoup

name = []
comment = []

def search_drama(year):
    if year == "2016":
        r = requests.get("https://chi.gogoblog.tw/search.php?mode=subject&qstr=2016韓劇排行")
    if year == "2017":
        r = requests.get("https://chi.gogoblog.tw/search.php?mode=subject&qstr=2017韓劇排行")
    if year == "2018":
        r = requests.get("https://chi.gogoblog.tw/search.php?mode=subject&qstr=2018韓劇排行")

    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'html.parser')
        con = soup.find('tbody')
        drama = con.find_all('tr')

        name.clear()
        comment.clear()
        for i in drama:
            namei = i.find('a')
            if namei is not None:
                name.append(namei.string)
            
            commenti = i.find_all('td')
            commenti = commenti[len(commenti) - 1].text
            commenti = commenti.split('\r\n            ')
            temp = commenti[len(commenti) - 1].split('\n')
            commenti[len(commenti) - 1] = temp[0]
            commenti.pop(0)
            commentj = ''
            for j in commenti:
                commentj += j

            if commentj is not "":
                comment.append(commentj)
        
        comment.pop(0)

