import requests
import os
import json
import config

def getFiles(modules, token):
	url = config.hosturl + "Workbins"
	payload = {'APIKey' : config.APIKey, 'AuthToken' : token, 'Duration' : '0', 'TitleOnly' : 'false'}

	for moduleID in modules.keys():
		payload['CourseID'] = moduleID

		response = requests.get(url, params = payload)
		data = response.json()
		for i in xrange(len(data['Results'])):
			folders = data['Results'][i]['Folders']
			for f in xrange(len(folders)):
				# make path first
				path = os.path.join(config.filepath, modules[moduleID])
				path = os.path.join(path, folders[f]['FolderName'])
				if not os.path.exists(path):
					os.makedirs(path)

				# get list of files
				files = folders[f]['Files']
				for fi in xrange(len(files)):
					fileid = files[fi]['ID']
					print fileid
					url = config.downloadurl
					payload = {'APIKey' : config.APIKey, 'AuthToken' : token, 'ID' : fileid, 'target' : 'workbin'}
					response = requests.get(url, params = payload, stream = True)

					print response.headers
					fpath = os.path.join(path, files[fi]['FileName'])
					fhandler = open(fpath, 'wb')
					fhandler.write(response.content)