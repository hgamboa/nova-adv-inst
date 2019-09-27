# Lab 7 - Visualization


## Pre Lab requirments

* Install bokeh via pip or via the full anaconda distribuition
* Install nova instrumentation


## Starting steps

* Test simple graph on ipython notebook

## Lab Goals

## Goal 1 - Transfer function of a low pass

* Plot the DB of the transfer function of the gain in a frequency log scale.
** |H| = 1/sqrt(1 + (f/f_c)^2)

* Plot the phase of the transfer function in degrees in a frequency log scale.
** phase(H) = -2 arctan(f/f_c)$


## Goal 2 - Random walk

* Plot a random walk (1000 samples)
* Plot the mean sliding window (using ni.smooth, with 50 samples window).
* Plot the variance band.
* Draw multiples superimposed random walks.

## Goal 3 - XY Graph

* Draw a xy graph of a sin(w) and cos(2w)
* Adjust the axis to be a square figure
* Place 9 lissajous figures in subplots

## Goal 4 - Matrix images

* Create a matrix of zeros and draw a circle 
by turning some points to 1
* Smooth the image with a vertical smooth by passing in each column.
* Smooth the image with a vertical smooth and horizontal pass.

## Going deeper 
* See the workshop from Cristine Doig: http://chdoig.github.io/scipy2015-blaze-bokeh/#/
* The examples are in: http://chdoig.github.io/scipy2015-blaze-bokeh/#/
