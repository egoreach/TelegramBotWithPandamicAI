from bs4 import BeautifulSoup
import lxml
import requests

url = 'https://xn--80aesfpebagmfblc0a.xn--p1ai/'


def parser():
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    chis = soup.find_all('div', class_='cv-countdown__item-value _accent')
    for i in chis[1]:
        return i.text


