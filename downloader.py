import requests
import getpass
import config
import auth
import json
import modules
import workbin
import os

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

currdir = os.getcwd()
authdir = os.path.join(currdir, "auth.json")

while True:
	if os.path.exists(authdir):
		with open(authdir) as fi:
			data = json.load(fi)
			token = data['Token']
			if auth.validate(token) == False:
				login()

		modules = modules.getModules(token)
		workbin.getFiles(modules, token)
		break
	else:
		login()