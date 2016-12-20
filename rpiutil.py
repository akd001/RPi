import datetime
import time

def logOutput (fileName, logString):
	with open(getHome() + "data/outputLog.txt", "a") as outputFile:
		ts = time.time()
		dt = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
		outputFile.write(dt + ": " + fileName + " - " + logString)

def getHome ():
	return '/home/akd/'
