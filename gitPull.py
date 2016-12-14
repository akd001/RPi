import os
import rpiutil

def pull():
	outString = os.system("git pull")
	rpiutil.logOutput("gitPull", outString)
