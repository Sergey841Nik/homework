import requests
import fake_useragent
from bs4 import BeautifulSoup
from time import sleep

user = fake_useragent.UserAgent().random

headers = {'user-agent': user} 

def get_url():
    for count in range(1, 2): #"пройтись" с первой по желаемую страницу 
        "Функция генератор собирает ссылки на карточки автомобилей на сайте drom.ru" 

        url = f"https://auto.drom.ru/lada/vesta/page{count}/"
        response = requests.get(url, headers=headers)
        soul = BeautifulSoup(response.text, "lxml")
        data = soul.find_all('a', class_= 'g6gv8w4 g6gv8w8 _1ioeqy90')
        for i in data:
            tegi_href = i.get('href')
            _ = tegi_href.split('.')
            if _[-1] == 'html':
                yield tegi_href
        
def array():
    """
    Функция генератор "заходит" в карточки автомобилей, по ссылке переданной функцией get_url 
    и собирает информацию об автомобиле (название, цена, пробег и ссылку на карточку автомобиля)
    """
    for url_car in get_url():
        response = requests.get(url_car, headers=headers)
        sleep(3) #имитируем человека, работаем помедленее
        soul = BeautifulSoup(response.text, "lxml")
        data_name = soul.find('div', class_='css-987tv1 eotelyr0')
        name = data_name.find('h1', class_='css-1tjirrw e18vbajn0').text
        
        price = soul.find('div', class_='wb9m8q0').text.replace('₽','')
        price= price.replace(' ','_')
        
        if soul.find('span', class_='css-1osyw3j ei6iaw00') is None:
            probeg = '-'
        else:
            probeg = soul.find('span', class_='css-1osyw3j ei6iaw00').text
        # print(probeg, url_car)
        yield name, int(price), probeg, url_car
        

