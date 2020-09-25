# Remote Lab 2 - Setting up a vizualization server

## Requirements

* Install bokeh via pip or via the full anaconda distribution  
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
sudo jupyter notebook --config=.jupyter/jupyter_notebook_config.py --allow-root
```

Then open a browser in your computer and write the IP address of your raspberry pi.


## Goal 2 - Launch the bokeh-server

Perform some examples using Bokeh ploting commands.


## Report - :red_circle: Until Friday 20:00 of your remote lecture

* Submit a pdf in moodle with a screenshot of a bokeh plot produced in your jupiter notebook


## Going deeper
* See the 5 minute intro to bokeh: http://nbviewer.jupyter.org/github/bokeh/bokeh-notebooks/blob/master/quickstart/quickstart.ipynb
* See more advanced examples on the workshop from Cristine Doig: http://chdoig.github.io/scipy2015-blaze-bokeh/#/
* The examples are in: http://chdoig.github.io/scipy2015-blaze-bokeh/#/
