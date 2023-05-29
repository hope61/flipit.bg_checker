import os
from dotenv import load_dotenv

load_dotenv()
url = 'https://flip.bg/magazin/apple/mobilen-telefon-apple-iphone-xs-256gb-space-grey/158/?%D1%81%D1%8A%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D0%B5=Dobro'
web_hook = os.getenv('web_hook')
min_price = 800.00

total_requests = 0
below_min_price_count = 0