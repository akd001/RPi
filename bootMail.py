import subprocess, re, urllib, time, rpiutil

def connect_type (word_list):
    if 'wlan0' in word_list or 'wlan1' in word_list:
        con_type = 'wifi'
    elif 'eth0' in word_list:
        con_type = 'ethernet'
    else:
        con_type = 'current'
    return con_type

def getPrivateIp () :
	arg='ip route list'
	p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
	data = p.communicate()
	ip_lines = data[0].splitlines()
	split_line_b = ip_lines[2].split()
	ip_type_b = connect_type(split_line_b)
	ipaddr_b = split_line_b[split_line_b.index('src')+1]
	privateIpString = 'Your %s private ip: [%s]' % (ip_type_b, ipaddr_b)
	return privateIpString

def getPublicIp ():
	data = re.search('"([0-9.]*)"', urllib.urlopen("http://ip.jsontest.com/").read()).group(1)
	publicIpString = ' and public ip: [%s]' %data
	return publicIpString

today = datetime.date.today()
mailSubject = 'Re: IP for rpium01 on %s' % today.strftime('%b %d %Y')
mailBody = getPrivateIp() + getPublicIp()
print mailSubject
print mailBody
rpiutil.sendMail(mailSubject, mailBody)
