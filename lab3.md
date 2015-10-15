# Lab 3 - Seting up a vizualization server


## Pre Lab requirments

* Install bokeh via pip or via the full anaconda distribuition
* Install nova instrumentation


## Starting steps
* Launch bokeh-server
* Test simple graph on ipython notebook

## Lab Goals


## Goal 1 - setup Jupyter notebook server


* copy next file to ~/.jupyter/jupyter_notebook_config.py

'
# Configuration file for jupyter notebook.
c = get_config()
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.password = u'sha1:ceaf7b8b148f:92bcc3411cf43275a324e8a8b6755601b5419610'
c.NotebookApp.port = 80
c.IPKernelApp.pylab = 'inline'
'

## Goal 2 - Launch the bokeh-server



## Going deeper 
* See the workshop from Cristine Doig: http://chdoig.github.io/scipy2015-blaze-bokeh/#/
* The examples are in: http://chdoig.github.io/scipy2015-blaze-bokeh/#/
