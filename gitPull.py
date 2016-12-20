import subprocess
import rpiutil

def pull():
	outString = subprocess.check_output("git -C " + rpiutil.getHome() + "git/ pull", shell=True)
	rpiutil.logOutput("gitPull", outString)
