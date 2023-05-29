import os
from dotenv import load_dotenv

load_dotenv()
url = '' # the url to the phone u want to keep a watch on
web_hook = os.getenv('web_hook')
min_price = 6969.00 #the min price of the phone this is the price that triggers the bot to send a message

# DONT TOUCH
total_requests = 0
below_min_price_count = 0