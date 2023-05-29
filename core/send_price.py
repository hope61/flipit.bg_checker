import requests
import json
from .vars import min_price, url, web_hook

def send_price(image_url, phone_title, current_price):
    content = f'@everyone'
    payload = {
        'content': content,
        'embeds': [
            {
                'title': f"✅ ``{phone_title}`` is below the price of **{min_price} лв**.",
                'image': {
                    'url': image_url
                },
                'fields': [
                    {
                        'name': '**💰 Price**',
                        'value': f"\n{current_price}лв\n",
                        'inline': False
                    },
                    {
                        'name': '**👆 Click me**',
                        'value': f"[Click here to view the Phone]({url})",
                        'inline': False
                    }
                ]
            }
        ]
    }

    # Convert the payload to JSON format
    json_payload = json.dumps(payload)

    # Set the headers
    headers = {
        'Content-Type': 'application/json'
    }

    # Send the POST request to the webhook URL
    response = requests.post(web_hook, data=json_payload, headers=headers)