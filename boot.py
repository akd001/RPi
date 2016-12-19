import subprocess

def reboot():
	subprocess.call(['sudo', 'reboot', 'now'])
