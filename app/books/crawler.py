import requests
from bs4 import BeautifulSoup
import urllib.request
import os

def book_requests(url):
    URL = url
    response = requests.get(URL)
    search_html = response.text
    soup = BeautifulSoup(search_html)
    return soup


def research_page_crawler(research_keyword='javascript'):
    url = 'http://www.yes24.com/searchcorner/Search?keywordAd=&keyword=&domain=ALL&qdomain=%C0%FC%C3%BC&Wcode=001_005&query=' + research_keyword
    soup = book_requests(url)
    div_goodsList = soup.select_one('div.goodsList')
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

def detail_page_crawler(book_research_list_data, name="생활코딩! HTML+CSS+자바스크립트", ):
    soup = book_requests(book_research_list_data[name])
    em_imgBdr = soup.find('em', class_='imgBdr')
    imgURL = em_imgBdr.find("img")['src']
    outpath = os.path.dirname('/home/kimdooh/바탕화면/')
    download_URL = em_imgBdr.find("img")["alt"] + '.jpg'
    image_path = outpath + '/' + download_URL
    # URL download
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
    #목차

    book_detail_info_dict={
        'title' : title,
        'image_path': image_path,
        'category' : categories_order_detail,
        'book_intro' : book_intro,
    }
    return book_detail_info_dict