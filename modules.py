import config
import requests
import json
import os
import time

def getModuleIDs(token):
	url = config.hosturl + "Modules"
	payload = {'APIKey' : config.APIKey, 'AuthToken' : token, 'Duration' : '0', 'IncludeAllInfo' : 'false', 'output' : 'json'}

	response = requests.get(url, params = payload)
	data = response.json()
	ids = []
	names = []

	for i in xrange(len(data['Results'])):
		time1 = data['Results'][i]['CourseCloseDate']
		
		if int(time1[6:-10]) > time.time() :
			ids.append(data['Results'][i]['ID'])
			names.append(data['Results'][i]['CourseCode'].replace('/', '-'))
	
	for moduleName in names:
		moduleName = moduleName.replace('/', '-')
		path = os.path.join(config.filepath, moduleName)
		if not os.path.exists(path):
			print "creating paths: " + path
			os.makedirs(path)

	return dict(zip(ids, names))
