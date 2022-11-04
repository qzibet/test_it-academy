import requests
from bs4 import BeautifulSoup as b

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 OPR/91.0.4516.77'
HEADERS = {'User_agent': USER_AGENT}

URL = 'https://www.mashina.kg/search/bmw/all/?color_multiple=4&currency=2&sort_by=price+asc&time_created=all&page={page}'

def parse_mashina():
    for i in range(1, 9):
        response = requests.get(URL.format(page=i))
        soup = b(response.text, 'html.parser')
        price_d = soup.find_all('strong')
        car_name = soup.find_all('h2', class_='name')
        all_views = soup.find_all('div', class_='listing-icons views')

        result = []

        for item, cars, view in zip(price_d, car_name, all_views):
            car_name = 'Ⓜ️ ' + cars.text.replace(' ', '').replace('\n', '')
            car_price ='Цена:' + item.text.replace('\n', '')
            car_views = 'Количество просмотров: ' + view.text.replace(' ', '')
            one_elem = {
                'car_name': car_name,
                'car_price': car_price,
                'car_views': car_views,
            }
            result.append(one_elem)
        
        return result
