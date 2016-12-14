import datetime
import time

def logOutput (fileName, logString):
	with open("../data/outputLog.txt", "w") as outputFile:
		ts = time.time()
		dt = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
		outputFile.write(dt + ": " + fileName + " - " + logString)
