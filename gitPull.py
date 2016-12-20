import subprocess
import rpiutil

def pull():
	outString = subprocess.check_output("git -C git/ pull", shell=True)
	rpiutil.logOutput("gitPull", outString)
