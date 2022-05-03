import json
import requests
from pprint import pprint
import time


from_date = int(time.time()) - (2 * 24 * 3600)
url = 'https://api.stackexchange.com/2.3/search/advanced'
params = {'order': 'desc', 'sort': 'activity', 'tagged': 'python', 'site': 'stackoverflow', 'fromdate': from_date}
response = requests.get(url, params=params)
for message in response.json()['items']:
    print(message['question_id'],message['title'])
