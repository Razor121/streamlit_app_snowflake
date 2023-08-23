import streamlit 
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.header("This is my first streamlit application")
streamlit.text("This is a sample text")




fruit_data= pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
fruit_data= fruit_data.set_index('Fruit')

selected_fruits=streamlit.multiselect("Please select fruits: ",list(fruit_data.index),["Avocado","Strawberries"])
fruits_to_show=fruit_data.loc[selected_fruits]
streamlit.dataframe(fruits_to_show)


# FRUITYVICE

streamlit.header("Fruity vice fruit advice")
try:
  fruit_choice= streamlit.text_input('what fruit do you want to know about')  #,'Kiwi'
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    fruit_normalize= pd.json_normalize(fruityvice_response.json())
    #fruit_normalize= fruit_normalize.set_index('id')
    streamlit.dataframe(fruit_normalize)
except URLError as e:
    streamlit.error("noty hora bhen ke lode)
    




# the streamlit code above will not be affected after the below line is executed
streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select fruit_name from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("The fuirt load list contains:")
streamlit.dataframe(my_data_row)

add_my_fruit= streamlit.text_input("What fruits would like to add?")
streamlit.write("Thanks for adding",add_my_fruit)

my_cur.execute("insert into fruit_load_list values('"+add_my_fruit+"')")
                                   








