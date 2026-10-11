import streamlit as st

#import functions from feature_files
from feature_even_odd import return_even
from feature_even_odd import return_odd

#define functions
original_list= [i for i in range(100)]

even_list = return_even(original_list)
odd_list = return_odd(original_list)

#code being written in streamlit
st.write("Hello team, ready to start the project?")

st.write(even_list)
st.write(odd_list)