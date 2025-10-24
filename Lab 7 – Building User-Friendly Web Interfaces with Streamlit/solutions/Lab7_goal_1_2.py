# -*- coding: utf-8 -*-
# Lab 7 - Goal 1.2
# Pedro Vieira 25/26

import streamlit as st

#goal 1.1
st.title("My First Page")
st.text("Hello world")

#goal 1.2
#inputs the two numbers
a=st.number_input('Value 1:', value=1.0)
b=st.number_input('Value 2:', value=1.0)

#when button pressed multplies the 2 numbers and prints result
if st.button('Multiply'):
    c=a*b
    st.text('--> ' + str(a) + 'x' + str(b) + '=' + str(c))