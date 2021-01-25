#!/usr/bin/python

from socket import *
import optparse
from threading import *


def connScan(thost, tport):

	if tport > 1 and tport < 100:
		try:
			sock = socket(AF_INET, SOCK_STREAM)
			sock.connect((thost,tport))
			print '%d/tcp        open' %tport
		except:
			print '%d/tcp        closed' %tport
		finally:
			sock.close()

	if tport > 99 and tport < 999:
		try:
			sock = socket(AF_INET, SOCK_STREAM)
			sock.connect((thost,tport))
			print '%d/tcp       open' %tport
		except:
			print '%d/tcp       closed' %tport
		finally:
			sock.close()
	if tport > 1000:
		try:
			sock = socket(AF_INET, SOCK_STREAM)
			sock.connect((thost,tport))
			print '%d/tcp      open' %tport
		except:
			print '%d/tcp      closed' %tport
		finally:
			sock.close()


def portScan(thost,tports):

	try:
		hostIP = gethostbyname(thost)
		print ('Started advanced port scan for target [%s]' %hostIP)
	except:
		print ('Cant resolve host name %s' %thost)
	try:
		hostName = gethostbyaddr(hostIP)
		print '[+] Scan results for: ' + hostName[0]
		print 'PORT          STATE'
	except:
		print '[+] Scan results for: ' + hostIP
		print 'PORT          STATE'
		setdefaulttimeout(1)
	for tport in tports:
		t = Thread(target=connScan, args=(thost, int(tport)))
		t.start()

def main():
	parser = optparse.OptionParser('Usage of Program: ' + '-H <target host> -p <target port>')
	parser.add_option('-H', dest='thost', type='string', help='specify target host')
	parser.add_option('-p', dest='tport', type='string', help='specify target port (if > 1 ports should be seperated by ",")')
	(options, args) = parser.parse_args()
	thost = options.thost
	tports = str(options.tport).split(',')
	if (thost == None) | (tports[0] == None):
		print parser.usage
		exit(0)
	portScan(thost,tports)
if __name__ == '__main__':
	main()
