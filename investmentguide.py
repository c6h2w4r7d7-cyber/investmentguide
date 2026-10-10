import streamlit as st

from feature_01 import return_even
from feature_02 import return_odd

original_list= [i for i in range(100)]

even_list = return_even(original_list)
odd_list = return_odd(original_list)


st.write("Hello team, ready to start the project?")

st.write(even_list)
st.write(odd_list)