from pprint import pprint

import requests as requests

s = "With these changes, " \
    "your extension will display a " \
    "popup with a button, and when the" \
    " button is pressed, it will make " \
    "the specified request using the fetch " \
    "API. Adjust the code according to your " \
    "specific requirements and extension design."

def process():
    url = 'http://localhost:5000/api/process'
    param = \
        {
            'id': 'test',
            'sentences': [s],
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
    process()
