import config
import requests
import json
import os
import time

def getModules(token):
	url = config.hosturl + "Modules"
	payload = {'APIKey' : config.APIKey, 'AuthToken' : token, 'Duration' : '0', 'IncludeAllInfo' : 'false', 'output' : 'json'}

	response = requests.get(url, params = payload)
	data = response.json()
	ids = []
	names = []

	modules = data['Results']
	return modules