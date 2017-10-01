import json
import config
import os

def prepareFolder(pseudo, pathOutPut):
	pathCurrent = pathOutPut

	for i in range(0, 2):
		pathCurrent += pseudo[i] + "/"
		if os.path.isdir(pathCurrent) == False:
			os.mkdir(pathCurrent)

	return pathCurrent



def saveProfil(data):
	pseudo = data["pseudo"].lower()
	pathOutPut = config.env["ROOT_DIR"] + config.env["output"]["path"]
	pathFolderFile = prepareFolder(pseudo, pathOutPut)
	
	fileName = pseudo + ".json"
	pathFile = pathFolderFile + fileName
	
	with open(pathFile, 'w') as outfile:
		json.dump(data, outfile)





