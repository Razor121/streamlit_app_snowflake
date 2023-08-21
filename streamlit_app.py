import streamlit as st

streamlit.header("This is my first streamlit application")
streamlit.text("This is a sample text")


import pandas as pd

fruit_data= pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
fruit_data= fruit_data.set_index('Fruit')




selected_fruits=st.multiselect("", list(fruit_data.index), None, special_internal_function, None, None, None, None, None, 10, "Please select fruits of your choice: ", False, "visible")

fruits_to_show= fruit_data.loc[selected_fruits]

streamlit.dataframe(fruit_to_show)



