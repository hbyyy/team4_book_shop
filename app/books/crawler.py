import os
import urllib.request

import requests
from bs4 import BeautifulSoup

from config import settings


def book_requests(url):
    URL = url
    response = requests.get(URL)
    search_html = response.text
    soup = BeautifulSoup(search_html)
    return soup


def research_page_crawler(research_keyword):
    url = 'http://www.yes24.com/searchcorner/Search?keywordAd=&keyword=&domain=ALL&qdomain=%C0%FC%C3%BC&Wcode=001_005&query=' + research_keyword
    soup = book_requests(url)
    div_goodsList = soup.select_one('div.goodsList')
    if div_goodsList is None:
        return None
    td_goods_infogrp = div_goodsList.select('td.goods_infogrp')

    search_list = []
    href_list = []
    for i, ii in enumerate(td_goods_infogrp):
        test = ii.select_one('a')
        search_list.append(str(test.select_one('strong')).replace("<strong>", "").replace("</strong>", ""))

        href = 'http://www.yes24.com' + test['href']
        href_list.append(href)
    print(href_list)
    print(search_list)
    book_research_list_data = {}
    for href, title in zip(href_list, search_list):
        book_research_list_data[title] = href
    return book_research_list_data


def detail_page_crawler(url):
    soup = book_requests(url)
    em_imgBdr = soup.find('em', class_='imgBdr')
    imgURL = em_imgBdr.find("img")['src']
    pwd_path = os.getcwd()

    # print(em_imgBdr.find("img")["alt"])

    outpath = os.path.join(settings.MEDIA_ROOT, 'books', 'image')
    image_name = em_imgBdr.find("img")["alt"] + '.jpg'
    image_path = outpath + '/' + image_name
    # URL download
    # image_url = urllib.request.urlretrieve(imgURL, image_path)
    image_url = urllib.request.urlretrieve(imgURL, image_path)
    # title
    h2_gd_name = soup.select_one('h2.gd_name')
    title = h2_gd_name.getText()
    # 카테고리
    categories = soup.find("dl", class_="yesAlertDl")
    categories_order = categories.find('ul', class_='yesAlertLi')
    categories_order_detail = []
    for i in categories_order.find('li').find_all('a'):
        categories_order_detail.append(i.get_text())
    # ['국내도서', 'IT 모바일', '웹사이트', 'HTML/JavaScript/CSS/jQuery']
    # 책소개
    book_intro = soup.find('div', id='infoset_introduce')
    book_introduce_textarea = book_intro.select_one('textarea', class_='txtContentText').get_text().replace("\r\n", "")
    # 목차

    book_detail_info_dict = {
        'title': title,
        'image_path': image_path,
        'image_name': image_name,
        'category': categories_order_detail,
        'book_intro': book_introduce_textarea,
    }
    return book_detail_info_dict
