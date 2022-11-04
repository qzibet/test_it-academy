import time
import requests

from bs4 import BeautifulSoup as bs4

URL = 'https://akipress.com/allnews/'

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
HEADERS = {
    'User-agent': USER_AGENT,
    'cookie': 'ig_did=01871311-84F2-4539-9C0B-4361EDC483B7; ig_nrcb=1; mid=Y01VcwAEAAFWnArvQ5zTZ86sPdCB; csrftoken=AeUQixef8wgLw7VsaNdwvv44uR3YiHit; sessionid=4702698194%3Akhx1l014Bcxv83%3A20%3AAYfCGcK2C3ZbGVKflzfBznDPTzxqhI2UUtQ1LsEVfw; ds_user_id=4702698194; shbid="19244\0544702698194\0541697548853:01f74bcd8187c9b96409cb50abad4a1d64b906af6041e6c030ba7de1be7eff13323d377e"; shbts="1666012853\0544702698194\0541697548853:01f730343bf1924c34c4d35e7ee192ed9a1c5953632779c9ac1f5bb0c64636307210508d"; datr=tFZNYyTZClyJesymZdQTEUOt; rur="RVA\0544702698194\0541697549045:01f71a8b88af4a2dbc80af62ef25e0bdd0fc658849aeaccf0cc7d95c9720ce538e65da1a"',
    'x-csrftoken': 'AeUQixef8wgLw7VsaNdwvv44uR3YiHit'
    }

def benchmark(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f'Скорость: {end_time - start_time}')
    return wrapper

@benchmark
def get_response():
    url = 'https://i.instagram.com/api/v1/web/likes/2950411866377891770/like/'
    response_list = []
    for i in range(5):
        response = requests.post(url, headers=HEADERS)
        print(response)
        response_list.append(response)
        time.sleep(1)
    
    return response_list

print(get_response())


def get_soup(html, tag, tag_class):
    soup = bs4(html, 'html.parser')
    result = soup.find_all(tag, class_=tag_class)
    return result


def get_result(soup):
    for item in soup:
        print(item.text)


# if __name__ == '__main__':
#     html = get_response(URL, HEADERS)
#     soup = get_soup(html, 'a', 'newstitle')
#     get_result(soup)
