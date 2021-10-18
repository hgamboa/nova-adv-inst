# Lab 3 - Virtual Raspberry Pi 

## Requirements

* Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) (Windows - ver 6.1.26; Mac - ver 6.1.26)
* Download the [Lubuntu distribution](https://lubuntu.me/downloads/) (ver. 20.04.3 LTS ~1.7GB)

## Starting steps
* Create and setup a new virtual machine with the Lubuntu distribution.
Hints:
* Tutorial on installing VirtualBox on Windows: https://www.youtube.com/watch?v=WD1vMhJGPn8
* Tutorial on installing Lubuntu on VirtualBox: https://www.youtube.com/watch?v=tuuQKmfTB2I&t=14s

It is suggested to reserve 2048 MB of RAM and 10 GB for the virtual hard disk.

### Tips for Windows users
* :warning: It is possible that you will get an error when you try to start a virtual machine. The details of the error box should have VT-x is disable in the BIOS. If that happens it is necessary to go to the BIOS of your system and activate the virtualization mode of the processor. Depending of the manufacturer there is different ways to do it and you must look specifically for your computer model. An tutorial can be found in: https://support.bluestacks.com/hc/en-us/articles/115003174386-How-can-I-enable-virtualization-VT-on-my-PC-for-BlueStacks-4-

### Tips for Mac users
* The most recent version of virtual box do not work in all macs.
* An alternative is using [VMware fusion](https://www.vmware.com/products/fusion.html) which is also free for personal usage 


## Lab Goals

## Goal 1 - Use the console
* Start a new console and learn some commands
* Create a directory with the first part of your email
* edit a file with vi or nano
* copy the file to the directory 

 * learn the following commands
```
> cd mkdir cp vi sudo (...)
```

## Goal 2 - Install python  packages
* Install the [Miniconda](https://docs.conda.io/en/latest/miniconda.html) distribution
* Install additional Python packages
```bash
pip install ipython scipy numpy matplotlib jupyterlab
```
* Make a plot of a vector composed of 1000 points of gaussian noise with standard distribution


## Going deeper 
* Check the shell tutorial http://www.ee.surrey.ac.uk/Teaching/Unix/
* Vi list of commands: http://www.lagmonster.org/docs/vi2.html
* The Linux Command Line Book: http://linuxcommand.org/tlcl.php
* Using amazon cloud computing infrastructure - AWS: https://github.com/hgamboa/novaelphy/blob/master/CloudComputing/Cloud%20Computing.ipynb
