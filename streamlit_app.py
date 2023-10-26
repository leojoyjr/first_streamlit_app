import streamlit
import pandas 
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My parents Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omlete')
streamlit.text('🐔Hard boiled eggs')
streamlit.text('🥗Spinach Curry')
streamlit.text('🥑🍞avocado')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#making Fruit name as the index
my_fruit_list=my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruit_selected=streamlit.multiselect("Pick some fruits :",list(my_fruit_list.index),['Avocado','Strawberries'])
#taking a variable to push the fruits selected
fruit_to_show=my_fruit_list.loc[fruit_selected]
# Display the table on the page.
streamlit.dataframe(fruit_to_show)


# function 
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    # take the response from api and using the python functions get it in nice form
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    # making the output to a data frame
  streamlit.dataframe(fruityvice_normalized)
#new section to display api response
streamlit.header("Fruityvice Fruit Advice!")
try:
  #taking the input from the user
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function=get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()
# streamlit.write('The user entered ', fruit_choice)

streamlit.header("The fruit load list contains:")
# snowflake related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()

#  add a button to load the fruit
if streamlit.button('Get fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows=get_fruit_load_list()
  streamlit.dataframe(my_data_rows)


# streamlit.stop()

# allow the end user to add a fruit to the list
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('" + new_fruit + "')")
    return "Thanks For adding "+ new_fruit

add_my_fruit=streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add aFruit to the List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function= insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)

#taking the input from the user
# fruit_choice = streamlit.text_input('What fruit would you like add?','Kiwi')
# streamlit.write('Thanks for adding', fruit_choice)





