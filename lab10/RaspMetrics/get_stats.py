import time
from datetime import timedelta, datetime

# This function opens the '/proc/meminfo' file and
# parses it. The results are then dumped to a dictonary
# and returned it.
# These include the total memory installed (MemTotal),
# unused memory (MemFree), and we calculate the used memory
# (MemUsed)
def get_ram():
	file = open('/proc/meminfo')
	lines = file.readlines()
	file.close()
	
	output = {'MemTotal': int(lines[0].strip().split()[1]), 'MemFree': int(lines[2].strip().split()[1])}
	output['MemUsed'] = output['MemTotal']-output['MemFree']
	for i in output:
		output[i] = output[i]*1E-6
	return output
	
# This function reads the CPU temperature, parses it, converts the results
# to celcius and returns them
def get_temperature():
	return float(open('/sys/class/thermal/thermal_zone0/temp','r').read().strip())/1000.0


# This function gets the CPU load. In UNIX systems, the cpu load is measured
# in time used, and therefore you have to make two sucessive reads of the 'proc/stat'
# file to get an estimate for this load.

def get_cpu(interval=0.1):
	def stats():
		cpu = open('/proc/stat','r').readlines()[0]
		return list(map(float,cpu.split()[1:5]))

	t1 = stats()
	time.sleep(interval)
	t2 = stats()
	delta = [t2[i] - t1[i] for i in range(len(t1))]
	try:
		return (1.0 - (delta[-1:].pop()/(sum(delta)*1.0)))*100
	except:
		return 0.0

# This function gets the total amount of seconds the system has been up
# and returns a string with days, hours, minutes, and seconds.
def get_uptime():
	seconds = open('/proc/uptime', 'r').readline().split()[0]
	sec = timedelta(seconds=int(float(seconds)))
	d = datetime(1,1,1) + sec 
	return "%d:%d:%d:%d" % (d.day-1, d.hour, d.minute, d.second)


# This function calls the previous four functions and joins all the outputs
# in a dictionary, returning it.
def get_stats(interval=0.1):
	return {'Ram': get_ram(), 'CPU': get_cpu(interval), 'Temperature': get_temperature(), 'Uptime': get_uptime()}

