import sys, datetime, time, smtplib, init
from email.mime.text import MIMEText

def getHome ():
	return init.constants['home']

sys.path.insert(0, getHome() + 'data')
import data

def logOutput (fileName, logString):
	with open(getHome() + "data/outputLog.txt", "a") as outputFile:
		ts = time.time()
		dt = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
		outputFile.write(dt + ": " + fileName + " - " + logString)

def getMailData (dataKey):
	return data.mailData[dataKey]

def getSmtpServer ():
	smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo()
	smtpserver.login(getMailData('mailUser'), getMailData('mailPass'))
	return smtpserver

def sendMail (mailSubject, mailBody):
	msg = MIMEText(mailBody)
	msg['Subject'] = mailSubject
	msg['From'] = getMailData('mailUserName')
	msg['To'] = getMailData('mailTo')
	smtpServer = getSmtpServer()
	smtpServer.sendmail(getMailData('mailUser'), [getMailData('mailTo')], msg.as_string())
	smtpServer.quit()
