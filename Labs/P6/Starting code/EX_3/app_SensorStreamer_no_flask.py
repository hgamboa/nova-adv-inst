import time
import json
import socket
import numpy as np


print ('The begin ...')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = "192.168.1.155" #put here the ip address of your mobile
    port = 4242
    
    filename=input("Output filename: ")
    sample=int(input("How many samples: "))
    
    print('Opening socket')
    s.connect((host, port))

    f=open(filename+'.csv', 'w')
    for n in range(sample):
        #time.sleep(0.025)
        data = s.recv(256)
        if data:
            decoded_data = data.decode("utf-8").split("\n")
            for msg in decoded_data:
                try:
                    package = json.loads(msg)
                    #print(package)
                    t=package["accelerometer"]["timestamp"]
                    acc=package["accelerometer"]["value"]
                    gyro=package["gyroscope"]["value"]
                    a = str(t)+','+str(acc[0])+','+str(acc[1])+','+str(acc[2])+','+str(gyro[0])+','+str(gyro[1])+','+str(gyro[2])
                    print(a)
                    f.write(a+'\n')


                except:
                    continue


    f.close()
    s.close()   
    print('socket closed') 


print ('... end')
