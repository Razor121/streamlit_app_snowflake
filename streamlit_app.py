import streamlit as st

st.header("This is my first streamlit application")
st.text("This is a sample text")


import pandas as pd

fruit_data= pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
fruit_data= fruit_data.set_index('Fruit')




selected_fruits=st.multiselect("Please select your fruits: ", list(fruit_data.index))

fruits_to_show= fruit_data.loc[selected_fruits]

st.dataframe(fruit_to_show)



