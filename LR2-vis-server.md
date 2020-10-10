# Remote Lab 2 - Setting up a vizualization server in a VM

## Requirements
In your VM created in LR1: 
* Install nova instrumentation
```
--> sudo pip install novainstrumentation
```

## Lab Goals


## Goal 1 - setup local Jupyter notebook server 
In your VM created in LR1: 

* Verify if python 3 is installed:
```
--> python3 --version
```
* If not install it
```
--> sudo apt install python3
```
* Installing Jupyter Notebook
  * Option 1 (light)
  ```
  --> sudo apt install jupyter-core
  --> sudo pip3 install notebook
  ```
  * Option 2 (miniconda)
  ```
  https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html
  ```
  * Option 3 (full anaconda)
  ```
  https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html
  ```
* test Jupyter notebook locally
  ```
  --> jupyter notebook
  ```


## Goal 2 - setup Bokeh

* install bokeh
  ```
	--> sudo pip3 install bokeh
  ```
  
* Try Bokeh
  ```
  https://nbviewer.jupyter.org/github/bokeh/bokeh-notebooks/blob/master/quickstart/quickstart.ipynb
  ```



## Goal 3 - setup remote Jupyter notebook server

* Follow the insrtuctions: http://jupyter-notebook.readthedocs.io/en/latest/public_server.html

* copy next file to ~/.jupyter/jupyter_notebook_config.py

```
# Configuration file for jupyter notebook.
c = get_config()
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
# This pass is: raspberry
c.NotebookApp.password = u'sha1:ceaf7b8b148f:92bcc3411cf43275a324e8a8b6755601b5419610'
c.NotebookApp.port = 80
c.IPKernelApp.pylab = 'inline'
```

* Start the notebook server in the shell of raspberry pi

```
sudo jupyter notebook --config=.jupyter/jupyter_notebook_config.py --allow-root
```

Then open a browser in your computer and write the IP address of your VM.

## Goal 4 - Create in VM a shared folder with the host
* In VM choose a shared folder in host by configuring: Devices - Shared Folderes - Shared Folder Settings
* Install in ubunto
	```
	--> sudo apt-get install virtualbox-guest-dkms
	--> sudo apt-get install virtualbox-guest-utils
	```
* Add user to virtualbox share
	```
	--> whoami (to confirm user name)
	--> sudo adduser <user name> vboxsf
	```
* reboot VM
* The new shared folder should become available in ububto desktop

## Goal 5 - Launch the bokeh-server

Perform some examples using Bokeh ploting commands.


## Report - :red_circle: Until Friday 20:00 of your remote lecture

* Submit a pdf in moodle with a screenshot of a bokeh plot produced in your jupiter notebook


## Going deeper
* See the 5 minute intro to bokeh: http://nbviewer.jupyter.org/github/bokeh/bokeh-notebooks/blob/master/quickstart/quickstart.ipynb
* See more advanced examples on the workshop from Cristine Doig: http://chdoig.github.io/scipy2015-blaze-bokeh/#/
* The examples are in: http://chdoig.github.io/scipy2015-blaze-bokeh/#/
