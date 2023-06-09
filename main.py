import requests
from bs4 import BeautifulSoup
import os
import time
from datetime import datetime
import json

from core.vars import *
from core.send_price import send_price
from core.get_price import get_price
from core.scrape_info import scrape_info

start_time = datetime.now()

def send_out_of_stock():
    content = f'@everyone The product is out of stock'
    payload = {
        'content': content,
    }
    json_payload = json.dumps(payload)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(web_hook, data=json_payload, headers=headers)

def print_statistics(total_requests, below_min_price_count, uptime):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Total Requests: {total_requests} | Below Min Price Count: {below_min_price_count} | Uptime: {uptime} | Current Price: {current_price}")

while True:
    total_requests += 1

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    stock_badge = soup.find('span', class_='badge stoc-alert no-stock badge-secondary')
    if stock_badge is not None:
        send_out_of_stock()
        break

    current_price = get_price(soup)
    if current_price <= min_price:
        below_min_price_count += 1

        image_url, phone_title = scrape_info(soup)
        send_price(image_url, phone_title, current_price)

        elapsed_time = datetime.now() - start_time
        uptime = str(elapsed_time).split(".")[0]
        print_statistics(total_requests, below_min_price_count, uptime)

        time.sleep(3600)
    else:
        elapsed_time = datetime.now() - start_time
        uptime = str(elapsed_time).split(".")[0]
        print_statistics(total_requests, below_min_price_count, uptime)

    time.sleep(10)  # Pause execution for 30 seconds