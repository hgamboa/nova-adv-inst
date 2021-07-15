# Lab 3 - Presential - Connecting to the Raspberry Pi

## Pre Lab requirements
For this lab you will need to install a [SSH](https://en.wikipedia.org/wiki/Secure_Shell_Protocol) and an [SFTP](https://en.wikipedia.org/wiki/SSH_File_Transfer_Protocol) client to connect to the Raspberry Pi (RPi). To help interact with the RPi in the headless mode, you will also install a remote access software with a GUI.

Windows:

1. Install the [**Bitvise SSH Client**](https://www.bitvise.com/ssh-client-download)
2. Install the [**VNC Viewer**](https://www.realvnc.com/pt/connect/download/viewer)

macOS:

1. Install [**Cyberduck**](https://cyberduck.io)
2. Install the [**VNC Viewer**](https://www.realvnc.com/pt/connect/download/viewer)

## Starting steps
* Connect your laptop to the local lab network
  * SSID: **pi**
  * Pass: **raspberry**

## Lab Goals

## Goal 1 - Connect to the RPi via SSH
Before proceeding, it is recommended that you fully understand the concepts of user and hostname. Take a look at the following [content](https://searchnetworking.techtarget.com/definition/host).
The user is `pi`. The host ID is written on your RPi cover. You must use it to find the complete `hostname`.

Windows:

Use Bitvise and establish an SSH connection using the GUI with the `user` and `hostnanme` you found.


macOS:

Use the ssh command on the macOS terminal replacing `user` and `hostname` by the ones you found.

`
ssh user@hostname
`

## Goal 2 - Create a group work folder in the RPi 
Establish an SFTP connection and create a new folder in the RPi. Copy some files from your laptop to the RPi.

## Goal 3 - Remote connect to the RPi

To establish a remote connection, you will need to instantiate the VNC Server on the RPi. Only after the vncserver process started on the device is it possible to use the VNC Client to connect to the RPi.

1. Launch the VNC Server in the RPi

`
vncserver
`

2. Use the VNC Viewer in your laptop and use the following connection details:

**Address:** 192.168.0.XXX:1 (Replace XXX with the Host ID)
**Pass:** raspberry

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