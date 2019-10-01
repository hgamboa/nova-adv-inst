# Lab 4 - Connecting to the Raspberry Pi


## Pre Lab requirments

* Install **bitvise** client (macos:command line **ssh** plus **cyberduck**)
* Install **tightvnc** viewer (macos: **chicken of the VNC**)

## Starting steps
* Connect your laptop to the local lab network
** ssid: pi
** pass: raspberry

## Lab Goals

## Goal 1 - Connect to the raspberry pi via ssh to the raspberry

* Find the mac address of the wifi pen to copute the local ip address.
** ex: 74Da38546692
* Compute the decimal value of the two last hexadecimal digitis:
** ex: HEX - 92 -> DEC - 146
** Use a calculator to do the conversion or write in ipython with format 0x92 and view the reusult.


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
* Config guide of the memory card [Raspberry pi Setup](raspberry_pi_setup.md)

* Learn to use byobu http://byobu.co/
