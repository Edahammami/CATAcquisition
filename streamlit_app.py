# Create the Streamlit app file
with open('app.py', 'w') as f:
    f.write("""
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Streamlit app
st.title("My Streamlit App")
st.write("This is a simple interactive graph.")

# Create a plot
fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)
""")
# Create the requirements file
with open('requirements.txt', 'w') as f:
    f.write("""
streamlit
matplotlib
numpy
""")
from google.colab import files
files.download('app.py')
files.download('requirements.txt')
