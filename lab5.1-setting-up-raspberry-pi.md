# Optional Lab  5.1 - Setting up Raspberry Pi


* Full raspberry installation guide

1. Set a lab router with the ssid pi and password

2. Copy raspbian

3. Setup starting script (need and HDMI monitor)

plug a network cable
ssh log to the raspberry with the indicated ip

create a new directory

sudo mkdir /setup

copy the files in this directory a setup directory in your home directory 

And form ssh do 

sudo cp ~/setup/* /setup 

and copy the rc.local to /etc/rc.local

sudo cp ~/setup/rc.local /etc/rc.local


4. Install packages

First update your package sources:


sudo apt-get update 

sudo apt-get install python-pip
sudo pip install --upgrade pip


sudo pip install python-dev numpy --upgrade

sudo apt-get install ipython python-scipy python-matplotlib python-pandas 

sudo pip install jupyter
sudo pip install bokeh --upgrade
sudo pip install mpld3
sudo pip install seaborn

sudo pip install -U scikit-learn

sudo apt-get install byobu 

execute byobu-enable


sudo apt-get install tightvncserver 

Lunch vnc server

vncserver

then connect to your ip:1

192.168.0.xxx:1


 
5. setup network

/networks


6. Startup scrips

/etc/rc.local

python /setup/start.py

######### start.py





##########




######## /etc/networks/interfaces

auto lo
iface lo inet loopback

auto eth0
allow-hotplug eth0
iface eth0 inet manual

auto wlan0
allow-hotplug wlan0
iface wlan0 inet static
wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
address 192.168.0.111
network 192.168.0.0
netmask 255.255.255.0
broadcast 192.168.0.255
gateway 192.168.0.1
dns-nameservers 192.168.0.1



#########

########## /etc/wpa_suplicant/wpa_suplicant.conf

ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
        ssid="pi"
        psk="raspberry"
        key_mgmt=WPA-PSK
}

###########


Follow: http://jupyter-notebook.readthedocs.org/en/latest/public_server.html

jupyter notebook --generate-config



###########  copy next file to ~/.jupyter/jupyter_notebook_config.py

# Configuration file for jupyter notebook.
c = get_config()
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.password = u'sha1:ceaf7b8b148f:92bcc3411cf43275a324e8a8b6755601b5419610'
c.NotebookApp.port = 80
c.IPKernelApp.pylab = 'inline'
##########

Launch using: 

sudo jupyter notebook --config=.jupyter/jupyter_notebook_config.py

password is raspberry

