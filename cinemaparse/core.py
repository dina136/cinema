'''Cinema module 2'''
import requests
from bs4 import BeautifulSoup
class CinemaParser:
    '''Class Cinema'''
    def __init__(self, town='msk'):
        '''Какой город'''
        self.city = town
        self.content = None
    def extract_raw_content(self):
        '''Дастаёт информацию со страницы'''
        waypage = requests.get('https://msk.subscity.ru/')
        self.content = waypage.text
    def print_raw_content(self):
        '''Выводит изъятую информацию со страницы'''
        soup = BeautifulSoup(self.content)
        print(soup.prettify())
TOWN_PARSER = CinemaParser('spb')
TOWN_PARSER.extract_raw_content()
TOWN_PARSER.print_raw_content()
