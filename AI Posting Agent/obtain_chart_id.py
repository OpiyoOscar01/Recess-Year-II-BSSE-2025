import requests

post_bot_token = "756697873:AAH5yjnens1LRfcCdxZi1b2g3h4i5j6k7l8m9n0o"  

url = f"https://api.telegram.org/bot{post_bot_token}/getUpdates"

response = requests.get(url)
print(response.json())