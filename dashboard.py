# Importing necessary libraries
import streamlit as st
import numpy as np

# Title of the web app
st.title('Random Number Generator')

# Generating a random number
random_number = np.random.randint(1, 101)

# Displaying the random number
st.write('The random number is:', random_number)
