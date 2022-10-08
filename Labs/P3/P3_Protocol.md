# Lab 3 - Connecting to the Raspberry Pi

## Pre Lab requirements
* For this lab you will need to install a [SSH](https://en.wikipedia.org/wiki/Secure_Shell_Protocol) and an [SFTP](https://en.wikipedia.org/wiki/SSH_File_Transfer_Protocol) client to connect to the Raspberry Pi (RPi). To help interact with the RPi in the headless mode, you will also install a remote access software with a GUI.

    * Windows:
        * Install the [**Bitvise SSH Client**](https://www.bitvise.com/ssh-client-download)
            * https://www.bitvise.com/ssh-client-download 
        * Install the [**VNC Viewer**](https://www.realvnc.com/pt/connect/download/viewer)
            * https://www.realvnc.com/en/connect/download/viewer/ 

    * macOS:
        * Install [**Cyberduck**](https://cyberduck.io)
        * Install the [**VNC Viewer**](https://www.realvnc.com/pt/connect/download/viewer)

* You also need a raspberry PI computer and a SD card with its operating system. A unique SD card was prepared for each group and you must use only this card during the course. The SD card has the following contents:
    * The latest release of the raspberry operating system 
        * https://www.raspberrypi.com/software/
    * Miniconda
        * https://conda.io/projects/conda/en/latest/user-guide/install/linux.html
    * Jupyter notebook 
        * https://jupyter.org/install 
    * Configured to access to the lab wifi network
        * unique ip adress (192.168.1.###)
        * login: pi
        * password: 1234 

## Starting steps
* Connect your laptop to the local lab network
    * SSID: **pi**
    * Pass: **raspberry**
* Insert the SD card in the appropriated  slot of the raspberry PI computer (RPI) 
* Connect the RPI to the power supply trough the usb cable provided. This usb cable is only for the purpose of powering the RPI, so even if you connect it to your computer, no data will flow through this cable.
* Wait one minute or so, to RPI to boot.
* Test connection between your pc and RPI
    * In the PC open a command line or command shell
    * Execute the following command **ping 192.168.1.###** (### is specific to your group)  
    * If connection successful  you should see a reply like this:
        * *Reply from 192.168.1.10: bytes=32 time<1ms TTL=64*
    * Do Ctrl^C if you need to stop the ping command

## Lab Goals

## Goal 1 - Connect to the RPi via SSH
Before proceeding, it is recommended that you fully understand the concepts of user and hostname. Take a look at the following [content](https://searchnetworking.techtarget.com/definition/host).
The user is `pi`. The host ID is written on your SD card. You must use it to find the complete `hostname`.

Windows:

Use Bitvise and establish an SSH connection using the GUI with the `user` and `hostname` you found.


macOS:

Use the ssh command on the macOS terminal replacing `user` and `hostname` you found.

`
ssh user@hostname
`

you have access to the command line of linux. Try a few simple commands. Try this link if you are not familiar with them:
* https://maker.pro/linux/tutorial/basic-linux-commands-for-beginners

## Goal 2 - Create a group work folder in the RPi 
Establish an SFTP connection and create a new folder in the RPi. Copy some files from your laptop to the RPi.

## Goal 3 - Jupyter Notebook
To start the jupyter notebook in your RPI, from the RPI ssh shell, execute:

`
jupyter notebook --ip 192.168.1.####
`

The jupyter session will begin and will give you a link to use, like this:

`
http://192.168.1.10:8888/?token=285d53bf433ec1040e6cb81c14df8f67049fe04b6b8faf05
`

Copy the link for a browser in you pc and you are ready to go.

Try to run some of scripts that you develop in P1 & P2.

Remember to copy first, the scripts to the RPI.

**Note:** 
If you intend to run Notebook scripts with plots, you will notice that all the matplotlib functions will give an error.
The reason for that is the matplotlib is not yet installed in the RPI. To install it, open a shell and run the following commands:
* `sudo apt-get install libatlas-base-dev`
* `sudo pip3 install matplotlib`


## Goal 4 - Remote connect to the RPi

Use the VNC Viewer in your laptop and use the following connection details:

**Address:** 192.168.1.### (Replace ### with the Host ID)
**Pass:** 1234

Launch an IPython shell with

`
ipython --pylab
`

Do a simple plot :

```python
plot(randn(100))
```


Save a pdf and download to the local computer:  

```python
savefig('plot.pdf')
```


## Going deeper
* Config guide of the memory card [Raspberry Pi Setup](oldlabs/lab5.1-setting-up-raspberry-pi.md)

* Learn to use byobu http://byobu.co/

* Linux/Unix Command Line [Cheat Sheet](https://sites.tufts.edu/cbi/files/2013/01/linux_cheat_sheet.pdf)

* 101 Most important Linux/Unix [commands](https://dev.to/awwsmm/101-bash-commands-and-tips-for-beginners-to-experts-30je)
