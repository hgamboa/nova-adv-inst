Bitalino python lab guide

[Project](lab-project.md)

* [0 Setting up](#settingup)
* [1 Acquisition](#acq)
* [2 Open a signal in python](#opensignal)
* [3 Process a signal](#process)
* [4 Measure and actuate with BITalino](#measure)
* [5 Online processing of signals](#online)
* [6 Template of project](#template)
* [7 Webbrowser](#browser)


# List goals

##  0 Setting up <a name="settingup"></a>
- Install the Anaconda Python distribution that best suits your platform:  
 https://www.anaconda.com/download/

- Install BITalino's serverBIT (r)evolution:    
https://github.com/BITalinoWorld/revolution-python-serverbit

- Install openSignals (r)evolution Software:  
http://bitalino.com/en/software

- Get a good code editor:  
https://pythonhosted.org/spyder/installation.html  
https://www.jetbrains.com/pycharm/  
http://www.pydev.org/  

- Enjoy executing some code:  
https://ipython.org/install.html


- Architecture of **bitalino** 
 [BITalino datasheet](http://bitalino.com/datasheets/REVOLUTION_BITalino_Board_Kit_Datasheet.pdf).

INCLUDE IMAGE from slides 

CREATE Map of the channels (analog and digital)

## 1 Acquisition <a name="acq"></a>

Once your BITalino is turned on, make sure the device is paired by the Bluetooth connection that you will use to receive the data.  You will match your device given the MAC address that is written in the back label. Default PIN is 1234.

- Open OpenSignals and proceed to configure your acquisition (sensors, channels, type of data, sampling rate). 

- Test sensor acquisition. It is important that you check sensor Datasheets to find out about the correct electrode placement, specs and formulas used for transfer functions:
    1. [How to acquire EMG](http://bitalino.com/datasheets/REVOLUTION_EMG_Sensor_Datasheet.pdf) 

    2. [How to acquire EDA](http://bitalino.com/datasheets/REVOLUTION_EDA_Sensor_Datasheet.pdf) 


    3. [How to acquire ECG](http://bitalino.com/datasheets/REVOLUTION_ECG_Sensor_Datasheet.pdf) 


    4. [How to acquire EEG](http://bitalino.com/datasheets/EEG_Sensor_Datasheet.pdf) 


    5. [How to acquire ACC](http://bitalino.com/datasheets/REVOLUTION_ACC_Sensor_Datasheet.pdf) 


    6. [How to acquire LUX](http://bitalino.com/datasheets/LUX_Sensor_Datasheet.pdf) 


    7. [How to acquire BTN](http://bitalino.com/datasheets/BTN_Sensor_Datasheet.pdf) 

- Record a signal 

## 2 Open a signal in python <a name="opensignal"></a>

SLIDE 4
Proceed to opening a signal data file sample [SampleEMG.txt](http://bitalino.com/datasheets/REVOLUTION_BITalino_Board_Kit_Datasheet.pdf).
You can use python script [LoadFile.py](http://bitalino.com/datasheets/REVOLUTION_BITalino_Board_Kit_Datasheet.pdf):
```
# -*- coding: utf-8 -*-
from pylab import *

data = loadtxt("SampleEMG.txt")

plot(data[:,5])
show()
```
## 3 Process a signal <a name="process"></a>



## 4 Measure and actuate with BITalino (assynchronous) <a name="measure"></a>

lightsBIT.py
ButtonBit.py 

[![IMAGE ALT TEXT](http://img.youtube.com/vi/LOFUTNEgrv4/0.jpg)](https://www.youtube.com/watch?v=LOFUTNEgrv4)

## 5 Online processing of signals <a name="online"></a>
MuscleBIT.py 
```
# -*- coding: utf-8 -*-
import bitalino

import numpy
import time

# Mac OS
macAddress = "/dev/tty.BITalino-01-93-DevB"

# Windows
# macAddress = "XX:XX:XX:XX:XX:XX"
   
device = bitalino.BITalino(macAddress)
time.sleep(1)

srate = 1000
nframes = 100
threshold = 5

device.start(srate, [0])
print "START"

try:
    while True:

        data = device.read(nframes)
        
        if numpy.mean(data[:, 1]) < 1: break

        EMG = data[:, -1]
        
        envelope = numpy.mean(abs(numpy.diff(EMG)))

        if envelope > threshold:
            device.trigger([0, 1])
        else:
            device.trigger([0, 0])

finally:
    print "STOP"
    device.stop()
    device.close()
```

## 6 Template of project <a name="template"></a>

templateproject.py

## 7 Webbrowser <a name="browser"></a>
Demo of serverbit + webrowser

BITalino revolution ServerBIT is a utility that helps you stream your signals in real time on a webbrowser (ClientBIT.html)
https://github.com/BITalinoWorld/revolution-python-serverbit

Once installed, run BITalino ServerBIT and open your ClientBIT.html. MAC address and channels can be configured through the config.json that is created under your home user folder. 
Open ClienBIT.html with Google Chrome and watch your signals in real time. Graphics are processed by FLOT. Feel free to source the web and inspect the codes to get the best data presentation features.
http://www.flotcharts.org/flot/examples/basic-options/index.html

## 8 External link <a name="external"></a>
Bitalino Forum
Bitalino API documentation 
...

## PENDING TASKS
BITalino pip install --> hsilva

Confirm that bitalino has api to python 3.X
Steps to follow for successful 3.5 connection:

1. Install Anaconda3-4.2.0 (most recent with Python 3.5) according to your system 
https://repo.continuum.io/archive/
2. Install dependencies
```
pip install pyserial
```

3. Download and install old PyBluez (3.5) package wheel for the user platform (e.g. WinX64), not available from PyBluez pypi resources
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pybluez
PyBluez‑0.22‑cp35‑none‑win_amd64.whl
```
pip install PyBluez-0.22-cp35-none-win_amd64.whl
```

4. Create a folder called  revolution-python-api
5. Download af12066 BITalino patch .zip and extract py files into the created folder called revolution-python-api (git clone link is broken)
$ git clone git@github.com:af12066/revolution-python-api.git (broken)
https://github.com/BITalinoWorld/revolution-python-api/archive/master.zip

6. Test bitalino.py (e.g. with a jupyter notebook test file)
