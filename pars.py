import requests
import lxml
from bs4 import BeautifulSoup


url = 'https://xn--80aesfpebagmfblc0a.xn--p1ai/'


def parser() -> str:
    """Возвращает число заболевших за сутки"""
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    chis = soup.find_all('div', class_='cv-countdown__item-value _accent')

    return chis[1].text
