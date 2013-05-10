import requests
import getpass
import config
import auth
import json
import modules
import workbin

def login():
	payload = {}
	payload['__VIEWSTATE'] = config.viewstate

	userid = raw_input('User ID: ')
	payload['userid'] = userid

	while True:
		password = getpass.getpass()
		payload['password'] = password
		url = config.formhost + config.APIKey
		response = requests.post(url, data = payload, allow_redirects = True)
		if len(response.text) != 416:
			print "Wrong password, please try again!"
		else:
			print "Login success"
			auth.validate(response.text)
			break

try:
	json_data = open('auth.json')
	data = json.load(json_data)
	token = data['Token']
	if auth.validate(token) == True:
		print "No login required"
	else:
		print "Noooooooooooooooo"

	modules = modules.getModuleIDs(token)
	workbin.getFiles(modules, token)
except:
	login()