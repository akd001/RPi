import os
import rpiutil

def pull():
	os.system("cd /home/pi/Desktop/git/Rpi/ && git pull")
	rpiutil.logOutput("gitPull", "git pull done")