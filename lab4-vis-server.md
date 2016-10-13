# Lab 4 - Seting up a vizualization server


## Pre Lab requirments

* Install bokeh via pip or via the full anaconda distribuition
* Install nova instrumentation


## Lab Goals


## Goal 1 - setup Jupyter notebook server

* Follow the insrtuctions: http://jupyter-notebook.readthedocs.io/en/latest/public_server.html

* copy next file to ~/.jupyter/jupyter_notebook_config.py

```
# Configuration file for jupyter notebook.
c = get_config()
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.password = u'sha1:ceaf7b8b148f:92bcc3411cf43275a324e8a8b6755601b5419610'
c.NotebookApp.port = 80
c.IPKernelApp.pylab = 'inline'
```

* Start the notebook server in the shell of raspberry pi

```
sudo jupyter notebook --config=~/.jupyter/jupyter_notebook_config.py
```

Then open a browser in your computer and write the IP address of your raspberry pi.


## Goal 2 - Launch the bokeh-server

Perform some examples using Bokeh plotiing commands.


## Going deeper 
* See the workshop from Cristine Doig: http://chdoig.github.io/scipy2015-blaze-bokeh/#/
* The examples are in: http://chdoig.github.io/scipy2015-blaze-bokeh/#/
