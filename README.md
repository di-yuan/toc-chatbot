# TOC-chatbot

## 簡介
搜尋並列出2016-2018年熱門韓劇，可以選擇當中有興趣的觀看評價，觀看後可以將喜歡的加入自己的韓劇清單。

## 功能
1. 輸入年：獲得當年熱門韓劇列表
2. 輸入編號：獲得該韓劇的評價
3. 可以選擇是否加入韓劇清單
3. 輸入LIST：觀看我的韓劇清單

## States
![image](https://github.com/di-yuan/toc-pro/blob/master/fsm.png)
1. hello：引導使用者輸入搜尋年分
2. wrong：輸入錯誤時，引導輸入正確
3. search：搜尋使用者輸入年分
4. comment：列出使用者選擇的韓劇評價
5. addYN：是否加入韓劇清單
6. list：觀看韓劇清單

## 使用技術
1. 利用beautifilsoup4抓取網頁資料獲得韓劇及評價
2. Heroku deploy app

## Demo
