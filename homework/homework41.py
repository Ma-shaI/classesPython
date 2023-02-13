import requests
from bs4 import BeautifulSoup
import datetime
import csv
import re


def get_html(url):
    r = requests.get(url)

    return r.text


def write_csv(data):
    with open('posts.csv', 'a', encoding='utf-8-sig') as f:
        writer = csv.writer(f, lineterminator='\r', delimiter=';')
        writer.writerow((data['title'], data['url'], data['user'], data['url_user'], data['date_post']))


def refine_title(s):
    res = s.replace('\u2060', '')
    return res


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    elements = soup.find_all('div', class_='story__main')
    for el in elements:

        try:
            info = el.find('h2')
            if info != None:
                title_info = info.text.strip()
                title = refine_title(title_info)
                print(title)
        except ValueError:
            title = ''

        try:
            info_url = el.find('h2')
            if info_url != None:
                url = info_url.find('a')['href']
        except ValueError:
            url = ''

        try:
            user_info = el.find('a', class_='story__user-link user__nick')
            if user_info != None:
                user = user_info['data-name']
        except ValueError:
            user = ''

        try:
            url_user_info = el.find('a', class_='story__user-link')
            if url_user_info != None:
                url_user = url_user_info['href']
        except ValueError:
            url_user = ''

        try:
            date = el.find('time', class_='caption')
            if date != None:
                date_post = date['datetime']
            else:
                date_post = datetime.datetime.now()
        except ValueError:
            date_post = ''

        data = {
            'title': title,
            'url': url,
            'user': user,
            'url_user': url_user,
            'date_post': date_post
        }

        write_csv(data)


def main():
    url = 'https://pikabu.ru/'
    get_data(get_html(url))


main()
