import config
import json
import requests
import getpass


def login():
    payload = {}
    payload['__VIEWSTATE'] = config.viewstate #Should be removed once browser based auth is in place
    payload['userid'] = raw_input('User ID: ')
    payload['password'] = getpass.getpass()

    url = config.ivlelogin + config.APIKey
    response = requests.post(url, data=payload, allow_redirects=True)

    if len(response.text) != 416: #This too hackish, will try to do proper browser based authentication
        print "Wrong username or password, please try again!"
        return "NULL"
    else:
        with open(config.authfile, 'w') as fi:
            fi.write('{"Token": "' + response.text + '"}') #rewrite the token with new value
        print "Login success"
        return response.text

def isValid(token):
    url = config.hosturl + "Validate"
    payload = {'APIKey': config.APIKey, 'Token': token}
    response = requests.get(url, params=payload)
    return response.json()['Success']

def authenticate():
    with open(config.authfile) as fi:
        token = json.load(fi)['Token']
        
    while not isValid(token):
        token = login()

    return token
