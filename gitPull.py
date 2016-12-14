import os
import rpiutil

def pull():
	outString = os.system("cd /home/pi/Desktop/git/Rpi/ && git pull")
	rpiutil.logOutput("gitPull", outString)
