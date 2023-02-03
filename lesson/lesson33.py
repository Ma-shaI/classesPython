# Парсинг

from bs4 import BeautifulSoup
import re

# def get_copywriter(tag):
#     whois = tag.find('div', class_='whois').text.strip()
#     if 'Copywriter' in whois:
#         return tag
#     else:
#         return None

def get_salary(s):
    pattern = r'\d+'
    # res = re.search(pattern, s).group()
    res = re.findall(pattern, s)[0]
    print(res)

f = open('index.html', encoding='utf-8').read()
soup = BeautifulSoup(f, 'html.parser')

salary = soup.find_all('div', {"data-set": 'salary'})

for i in salary:
    get_salary(i.text)

# copywriter = []
# row = soup.find_all('div', class_='row')
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
# print(copywriter)

# row = soup.find('div', class_='name').text
# row = soup.findAll('div', class_='name')
# print(row)
# for r in row:
#     print(r.text)

# row = soup.find_all('div', class_='row')[1].find('div', class_='links')
# print(row)
# row = soup.find_all('div', {"data-set": 'salary'})
# print(row)

# row = soup.find('div', string='Alena').parent.parent
# row = soup.find('div', string='Alena').find_parent(class_='row')
# print(row)

# row = soup.find('div', id='whois3').find_next_sibling()
# row = soup.find('div', id='whois3').find_previous_sibling()
# print(row)
