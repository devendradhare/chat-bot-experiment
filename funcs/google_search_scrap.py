import requests
from bs4 import BeautifulSoup


def search(query):
    # query = input('Enter your query: ')
    URL = "https://www.google.co.in/search?q=" + query
    print(URL)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
    }

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find(class_="dDoNo vrBOv vk_bk").get_text()
    # print(result)
    return result


# while True:
#     try:
#         query()
#     except Exception:
#         print('Sorry no result, please be clear')
#     user_input = input('To continue press y: ')
#     if user_input != 'y':
#         break
