import commands, re
import os.path

def getIp(iface='wlan0'):
	try:
    		str = open('/sys/class/net/%s/address' %iface).read()
		last = str.split(':')[-1]
		return int(last, 16)

	except:
		pass
local_ip = getIp()

filein = '/setup/dhcpcd.conf'
fileout = '/etc/dhcpcd.conf'

f = open(filein,'r')
filedata = f.read()
f.close()

g = open(fileout, 'r')
filedataout = g.read()
g.close()

if("192.168.0."+str(local_ip)+"/24" not in filedataout):
	newdata = filedata.replace("192.168.0.201",'192.168.0.'+str(local_ip)+'/24')
	f = open(fileout,'w')
	f.write(newdata)
	f.close()
	os.system('reboot')
else:
	pass
