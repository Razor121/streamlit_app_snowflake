import streamlit

streamlit.header("This is my first streamlit application")
streamlit.text("This is a sample text")


import pandas as pd

fruit_data= pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')


streamlit.dataframe(fruit_data)



