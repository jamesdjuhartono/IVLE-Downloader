import config
import requests
import os


def validate(token):
    url = config.hosturl + "Validate"
    payload = {'APIKey': config.APIKey, 'Token': token}
    response = requests.get(url, params=payload)

    data = response.json()
    if data['Success'] is False:
        os.remove('auth.json')
        return False
    else:
        f = open('auth.json', 'w')
        f.write(response.text)
        return True
