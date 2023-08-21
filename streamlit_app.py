import streamlit as st

streamlit.header("This is my first streamlit application")
streamlit.text("This is a sample text")


import pandas as pd

fruit_data= pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
fruit_data= fruit_data.set_index('Fruit')




selected_fruits=st.multiselect(label="", options=list(fruit_data.index), default=None, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, max_selections=None, placeholder="Please select fruits of your choice: ", disabled=False, label_visibility="visible")

fruits_to_show= fruit_data.loc[selected_fruits]

streamlit.dataframe(fruit_to_show)



