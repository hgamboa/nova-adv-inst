# Lab 3 - Visualization with MatPlotLib

## Starting steps

- Develop this Lab using the Jupyter Notebook of the RPI
  
  - In the Command Console do:
    
    - jupyter notebook --ip 192.168.1.###  (### is specific to your group)
    
    - copy generated link to the browser in your computer

- if you have not done any application with matplotlib before, try the Getting Started example found in:
* https://matplotlib.org/stable/users/getting_started/

Take a moment a see some of the examples available in:

* https://matplotlib.org/stable/gallery/index.html

## Lab Goals

## Goal 1 - XY Graph

* Draw a xy graph of a sin(t) and sin(4*(t+pi/2))
* Adjust the axis to be a square figure
* Place 9 lissajous figures in subplots, with diferent combination of frequencies 

## Goal 2 - Transfer function of a low pass filter

* Choose an cutoff frequency (f_c) and a frequency range to be analysed 
* Plot the amplitude of the transfer function of the gain in a frequency log scale (DB scale).
  * |H| = 1/sqrt(1 + (f/f_c)^2)
* Plot the phase of the transfer function in degrees in a frequency log scale.
  * phase(H) = -2 arctan(f/f_c)
* Plot frequency and phase in the same figure

## Goal 3 - Random walk

* Plot a 1D random walk (1000 samples)
  * search 'python randam walk' for inspiration
* Plot the moving average filtering with a window size of 50.
* Plot the variance of the original and filtered.

## Goal 4 - Matrix images

* Create an 100x100 matrix of zeros and change same values of the matrix to 0.5 and 1
  * Display the image with different color pallets
* Read the image the "baboon.bmp" and display it (https://matplotlib.org/stable/tutorials/images.html))
  * convert it to a luminance (grey scale image)
  * build its histogram
* Smooth the image using a 2D gaussian filter (from scipy.ndimage.filters)
  * try different values of sigma
