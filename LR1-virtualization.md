# Optional Lab (4.1) - Virtual Raspberry pi 

## Pre Lab requirments

* Install virtual box application (Windows - ver 6.1.14; Mac -ver 5.2.30)  (https://www.virtualbox.org/wiki/Downloads)
* Download Lubuntu distribution (ver. 18.04.5 Alternate 64 bits) (https://lubuntu.me/downloads/  ~600MB)

## Starting steps
* Create and setup a new virtual machine with the lubuntu linux distribution.

### Tips for Windows users
* If you need help for the installation:
* VirtualBox: https://www.youtube.com/watch?v=WD1vMhJGPn8 
* Lubuntu: https://www.youtube.com/watch?v=9f2l3j0rF-E (note: this tutorial shows the instalation of an older version of VirtualBox

### Tips for Mac users
* The most recent version of virtual box do not work in all macs.
* An alternative is using VMware fusion (also free for personal usage). (https://www.vmware.com/products/fusion.html) 

* Warning:Warning: It is possible that you will get an error when you try to start a virtual machine. The details of the error box should have VT-x is disable in the BIOS. If that happens it is necessary to go to the BIOS of your system and activate the virtualization mode of the processor. Depending of the manufacturer there is different ways to do it and you must look specifically for your computer model. An tutorial can be found in: https://support.bluestacks.com/hc/en-us/articles/115003174386-How-can-I-enable-virtualization-VT-on-my-PC-for-BlueStacks-4-

## Lab Goals

## Goal 1 - Use the console
* Start a new console and learn some commands
* Create a directory with the first part of your email
* edit a file with vi or nano
* copy the file to the directory 

 * learn the following commands
```
> cd mkdir cp 
> vi sudo
```


## Goal 2 - Install python  packages

 * Install python packages 
 * Teste ipython 
```
 > sudo apt-get install ipython python-scipy python-matplotlib ipython-notebook
```


## Report - :red_circle: Until Friday 20:00 of your remote lecture

* Submit a pdf in moodle with a screenshot of your virtual machine with a terminal inside the created directory.



## Going deeper 
* Check the shell tutotial http://www.ee.surrey.ac.uk/Teaching/Unix/
* Vi list of commands: http://www.lagmonster.org/docs/vi2.html
* The Linux Command Line Book: http://linuxcommand.org/tlcl.php
* Using amazon cloud computing infrastructure - AWS: https://github.com/hgamboa/novaelphy/blob/master/CloudComputing/Cloud%20Computing.ipynb


