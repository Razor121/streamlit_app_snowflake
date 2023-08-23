

import streamlit 


streamlit.header("This is my first streamlit application")
streamlit.text("This is a sample text")


import pandas as pd

fruit_data= pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
fruit_data= fruit_data.set_index('Fruit')

selected_fruits=streamlit.multiselect("Please select fruits: ",list(fruit_data.index),["Avocado","Strawberries"])
fruits_to_show=fruit_data.loc[selected_fruits]
streamlit.dataframe(fruits_to_show)

import requests

streamlit.header("Fruity vice fruit advice")
fruit_choice= streamlit.text_input('what fruit do you want to know about','Kiwi')
streamlit.write('User entered ',fruit_choice)



fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#streamlit.text(fruityvice_response.json())


fruit_normalize= pd.json_normalize(fruityvice_response.json())
fruit_normalize= fruit_normalize.set_index('id')
streamlit.dataframe(fruit_normalize)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)








