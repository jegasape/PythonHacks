#!/usr/bin/env python
from subprocess import Popen, PIPE

for ip in range(1,40):
	ipAddress = '10.0.0.'+str(ip)
	print("Scanning %s " %(ipAddress))
	subprocess = Popen(['/bin/ping', '-c 1 ', ipAddress], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	stdout, stderr= subprocess.communicate(input=None)
	if "bytes from " in str(stdout):
		print("The Ip Address %s has responded with a ECHO_REPLY!" %(stdout.split()[1]))
