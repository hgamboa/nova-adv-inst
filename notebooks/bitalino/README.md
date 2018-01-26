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

Open opensignals

Test all sensors 

How to EMG
How to ACC
Hwo to EDA
How to ECG
How to EEG
How to light

Record a signal 

## 2 Open a signal in python <a name="opensignal"></a>

SLIDE 4
Proceed to opening a signal data file sample [SampleEMG.txt](http://bitalino.com/datasheets/REVOLUTION_BITalino_Board_Kit_Datasheet.pdf).
You can use python script [LoadFile.py](http://bitalino.com/datasheets/REVOLUTION_BITalino_Board_Kit_Datasheet.pdf).
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

## 6 Template of project <a name="template"></a>

templateproject.py

## 7 Webbrowser <a name="browser"></a>
Demo of serverbit + webrowser

## 8 External link <a name="external"></a>
Bitalino Forum
Bitalino API documentation 
...

## PENDING TASKS

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
