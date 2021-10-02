import subprocess, re
import os.path

def getmac(iface):

    ifconfig = subprocess.getoutput("ifconfig " + iface)

    mac = re.search('\w\w:\w\w:.+\n', ifconfig)

    if mac is None:

        parsedMac = 'Mac not found'

    else:

        parsedMac = mac.group()

    return parsedMac #Or use return here.



local_ip = int(getmac("wlan0").strip().split(":")[5].split()[0],16)



# Show the local ip

print(local_ip)







filein = '/setup/interfaces'

fileout = '/etc/network/interfaces'



f = open(filein,'r')

filedata = f.read()

f.close()



newdata = filedata.replace(".111",'.'+str(local_ip))



f = open(fileout,'w')

f.write(newdata)

f.close()



print ('Instalation of wlan0 completed')



os.system('cp /setup/wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf')

os.system('/etc/init.d/networking stop')

os.system('/etc/init.d/networking start')
