# -*- coding: utf-8 -*-
# Lab 7 - Goal 1.3
# Pedro Vieira 25/26

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

#title
st.title("Plotting Data")

#input parameters data 
sr = st.number_input('Sample rate:', value=2000)
freq_1 = st.number_input('Frequency 1:', value=1)
freq_2 = st.number_input('Frequency 2:', value=4)
freq_3 = st.number_input('Frequency 3:', value=7)

#generate data and plot when button pressed
if st.button('Generate Data & Plot'):
    # sampling interval
    ts = 1.0/sr
    t = np.arange(0,1,ts)
    
    #generate data
    x = 3*np.sin(2*np.pi*freq_1*t)
    x += np.sin(2*np.pi*freq_2*t)
    x += 0.5* np.sin(2*np.pi*freq_3*t)

    #plot x
    fig, ax = plt.subplots()
    ax.plot(t,x)
    st.pyplot(fig)