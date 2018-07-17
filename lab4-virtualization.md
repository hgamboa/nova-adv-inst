# Lab 3 - Virtual Raspberry pi 

## Pre Lab requirments

* Install virtual box application (https://www.virtualbox.org/wiki/Downloads)
* Download Lubuntu distribution(https://help.ubuntu.com/community/Lubuntu/GetLubuntu  ~600MB)
* SSH-client
 * Windows - Download and install bitvise (https://www.bitvise.com/ssh-client)
 * Mac - included
* FTP-client
 * Windows - Bitwise
 * Mac - cyberduck (https://cyberduck.io/)


## Starting steps
* Create and setup a new virtual machine with the lubuntu linux distribution.

## Lab Goals

## Goal 1 - Use the console
* Start a new console and learn some commands
* Create a directory
* edit a file with vi
* copy the file to the directory 

 * learn the following commands
```
> cd mkdir cp 
> vi sudo
```
## Goal 2 - Connect over ssh and tranfer files
 * Install openssh-server 
```
> sudo apt-get install openssh-server
> reboot
```
 * delete and create a new newtwork device in virtual box and set to host-only
 * edit a file with vi remotely
 * copy a file over ssh


## Goal 3 - Install python  packages

 * Install python packages 
 * Teste ipython 
```
 > sudo apt-get install ipython python-scipy python-matplotlib ipython-notebook
```

## Going deeper 
* Check the shell tutotial http://www.ee.surrey.ac.uk/Teaching/Unix/
* Vi list of commands: http://www.lagmonster.org/docs/vi2.html
* The Linux Command Line Book: http://linuxcommand.org/tlcl.php
* Using amazon cloud computing infrastructure - AWS: https://github.com/hgamboa/novaelphy/blob/master/CloudComputing/Cloud%20Computing.ipynb


