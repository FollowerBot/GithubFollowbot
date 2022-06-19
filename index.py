from fake_headers import Headers
from random import randrange
import requests
import json
import time

i = 0
while True:
    i = i + 1
    print(f'Starting Round #{i}')

    # Random Headers
    header = Headers()
    headers = header.generate()

    # Random Proxy
    random_proxy = requests.get('https://public.freeproxyapi.com/api/Proxy/Mini').json()
    proxy = random_proxy['host'] + ":" + str(random_proxy['port'])
    proxies = {
        'http': 'http://' + proxy,
    }

    # Get ~30 Random Users
    random_group = randrange(10000)  # Mostly active people hopefully
    users = requests.get(f'https://api.github.com/users?client_id=ID&client_secret=SECRET&per_page=100&since={random_group}', headers=headers, proxies=proxies)
    json_data = json.loads(users.text)

    # Follow everyone in list!
    for user in json_data:
        username = user['login']
        headers = {
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': 'token TOKEN'
        }
        response = requests.put(f'https://api.github.com/user/following/{username}?client_id=ID&client_secret=SECRET', headers=headers, proxies=proxies)
        print(f'Followed {username}!')

    # Trying not to spam sorry github!
    print(f'Completed Following Round #{i}...Sleeping for a few seconds')
    time.sleep(10)
