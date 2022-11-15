#example for LanMic Interface. PV 13/12/21

import time
import socket
import numpy as np
import struct
from scipy.io.wavfile import write 


print ('The begin (lanmic)...')

wavFile = input('Wav filename: ')
wavFile = wavFile +'.wav'
AqTime = int(input('Aquisition time (s): '))

#settings 
host = "192.168.1.155" #ip address of the mobile
samplerate = 22050 #(LANmic sample rate)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #host = "192.168.1.155"
    port = 8080
    
    print('Opening socket')
    s.connect((host, port))


    chunk_size = 1024 # 512
    #audio_format = pyaudio.paInt16
    channels = 1
    #samplerate = 22050 #(LANmic sample rate /2)
    samplerate = int(samplerate/2)    #(LANmic sample rate /2)

    print('connected to server\n')
    
    print('Sound being aquired ...')
    
    #wait for data to be aquired before start
    time.sleep(chunk_size/samplerate)
    data=s.recv(chunk_size)
    t0=time.time()
    #aquire for a period of time
    while time.time()-t0 < AqTime:
        time.sleep(chunk_size/samplerate/4)
        data+=s.recv(chunk_size)
    # to flush the buffer
    time.sleep(0.2)
    data+=s.recv(chunk_size)
   
    print('... finished')
    
    l=len(data)
    print('Length of data (3)= ', l)
   
    #Convert to numpy array
    npdata=np.frombuffer(data, dtype=np.int32)
  
    #save data   
    write(wavFile, samplerate, npdata);     
    print('wav file writeen\n')
    
    #close socket
    s.close()   
    print('socket closed') 


print ('... end')
