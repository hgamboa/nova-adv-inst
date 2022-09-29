# Lab 4 - Visualization with MatPlotLib


## Requirements

* Install MatPlotLib via pip in your RPI
  *  sudo pip install matplotlib
* Documentation about MatPlotLib in:
  *  https://matplotlib.org/stable/index.html


## Starting steps

* Use jupyter notebook or spyder
* Implelement and test the Getting Started example found in:
  * https://matplotlib.org/stable/users/getting_started/

## Lab Goals

## Goal 1 - XY Graph

* Draw a xy graph of a sin(w) and cos(2w)
* Adjust the axis to be a square figure
* Place 9 lissajous figures in subplots

## Goal 2 - Transfer function of a low pass filter

* Choose an cutoff frequency (f_c) and a frequency range to be analysed 
* Plot the amplitude of the transfer function of the gain in a frequency log scale (DB scale).
  * |H| = 1/sqrt(1 + (f/f_c)^2)
* Plot the phase of the transfer function in degrees in a frequency log scale.
  * phase(H) = -2 arctan(f/f_c)


## Goal 2 - Random walk

* Plot a random walk (1000 samples)
  * search 'python randam walk' for inspiration
* Plot the mean sliding window (using ni.smooth, with 50 samples window).
* Plot the variance band.
* Draw multiples superimposed random walks.


## Goal 4 - Matrix images

* Create a matrix of zeros and draw a circle 
by turning some points to 1
* Smooth the image with a vertical smooth by passing in each column.
* Smooth the image with a vertical smooth and horizontal pass.


## Report - :red_circle: Until Friday 20:00 of your remote lecture

* Submit a pdf in moodle with a screenshot of all 4 plots


## Going deeper 
* See the workshop from Cristine Doig: http://chdoig.github.io/scipy2015-blaze-bokeh/#/
* The examples are in: http://chdoig.github.io/scipy2015-blaze-bokeh/#/
