from bs4 import BeautifulSoup
import requests

def find_acronyms(link='http://www.easy-forex.com/au/currencyacronyms/'):
    r = requests.get(link)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    cur_list = list()
    for row in soup.find('table').find('tbody').find_all('tr'):
        cur_list.append(row.find_all('td')[1].get_text())
    return cur_list

