# Lab 3 - Presential - Connecting to the Raspberry Pi


## Pre Lab requirements

* Install **bitvise** client (macos:command line **ssh** plus **cyberduck**)
* Install **tightvnc** viewer (macos: **chicken of the VNC**)

## Starting steps
* Connect your laptop to the local lab network
  * ssid: **pi**
  * pass: **raspberry**

## Lab Goals

## Goal 1 - Connect to the raspberry pi via ssh to the raspberry

* Find the number written on the raspberry pi cover a and use it as XXX

* Connext via ssh to the raspberry pi

`
ssh pi@192.168.0.XXX
`

(XXX substitute with the computed local ip)

## Goal 2 - Folder for group work

* Use sftp to create a new folder and copy some files

## Goal 3 - Remote connect

* Launch the vnc server (execute the following command in the shell)

`
vncserver
`

* Then use the tightvnc client in your computer and insert the address

192.168.0.XXX:1

The password is: raspberry

Launch an ipython shell with

`
ipython --pylab
`

Do a simple plot :

`
plot(randn(100))
`

save a pdf and downlod to the local computer:  

`
savefig('plot.pdf')
`


## Going deeper
* Config guide of the memory card [Raspberry pi Setup](lab5.1-setting-up-raspberry-pi.md)

* Learn to use byobu http://byobu.co/

* Linux commands - 101 most importants: https://dev.to/awwsmm/101-bash-commands-and-tips-for-beginners-to-experts-30je
