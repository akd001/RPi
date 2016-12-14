import subprocess
import rpiutil

def pull():
	outString = subprocess.check_output("git pull", shell=True)
	rpiutil.logOutput("gitPull", outString)
