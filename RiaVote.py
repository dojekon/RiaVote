import requests
import json
import threading
import time
import logging
import configparser

# Настройка логгирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Задание общих параметров для запроса
url = 'https://ria.ru/services/vote/add/'
headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru,en;q=0.9,cy;q=0.8',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Origin': 'https://rsport.ria.ru',
    'Referer': 'https://rsport.ria.ru/20231219/boss-of-year-2023-1911702814.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.771 YaBrowser/23.11.2.771 Yowser/2.5 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'sec-ch-ua': '"Chromium";v="118", "YaBrowser";v="23", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}

def read_config(filename='config.ini'):
    config = configparser.ConfigParser()
    config.read(filename)
    return config['Vote']['vote_id'], config['Vote']['vote_answer_id'], config['Vote']['g_recaptcha_response']

def vote(vote_id, vote_answer_id, g_recaptcha_response):
    data = {
        'vote_id': vote_id,
        'vote_answer_id%5B%5D': vote_answer_id,
        'g_recaptcha_response': g_recaptcha_response 
    }

    response = requests.post(url, headers=headers, data=data)
    return response

def vote_in_thread(vote_id, vote_answer_id, g_recaptcha_response, thread_number):
    while True:
        response = vote(vote_id, vote_answer_id, g_recaptcha_response)
        if response.status_code == 200:
            logging.info(f'Thread {thread_number}: Vote successful')
        else:
            logging.error(f'Thread {thread_number}: Vote failed. Status code: {response.status_code}, Response: {response.text}')
        time.sleep(10)

# Чтение параметров из конфигурационного файла
vote_id, vote_answer_id, g_recaptcha_response = read_config()

# Запуск 10 потоков
threads = []
for i in range(10):
    thread = threading.Thread(target=vote_in_thread, args=(vote_id, vote_answer_id, g_recaptcha_response, i + 1))
    threads.append(thread)
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()
