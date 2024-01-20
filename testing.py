from pprint import pprint

import requests as requests


def process():
    url = 'http://localhost:5000/api/process'
    param = \
        {
            'id': 'test',
            'sentences': ['one', 'two', 'three'],
            'voice': 'default'
        }

    r = requests.post(url, json=param)
    if r.status_code == 200:
        print(r.json())
    else:
        print('failed')
        pprint(r)


def retrieve():
    url = 'http://localhost:5000/api/retrieve?v_id=test'
    r = requests.get(url)
    if r.status_code == 200:
        print(r.json())
    else:
        print('failed')
        pprint(r)


if __name__ == "__main__":
    retrieve()
