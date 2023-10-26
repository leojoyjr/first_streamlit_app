import streamlit
streamlit.title('My parents Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omlete')
streamlit.text('🐔Hard boiled eggs')
streamlit.text('🥗Spinach Curry')
streamlit.text('🥑🍞avocado')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas 
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#making Fruit name as the index
my_fruit_list=my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruit_selected=streamlit.multiselect("Pick some fruits :",list(my_fruit_list.index),['Avocado','Strawberries'])
#taking a variable to push the fruits selected
fruit_to_show=my_fruit_list.loc[fruit_selected]
# Display the table on the page.
streamlit.dataframe(fruit_to_show)

#new section to display api response
streamlit.header("Fruityvice Fruit Advice!")

#taking the input from the user
fruit_choice = streamlit.text_input('What fruit would you like information about?','jackFruit')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


# take the response from api and using the python functions get it in nice form
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# making the output to a data frame
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

#taking the input from the user
fruit_choice = streamlit.text_input('What fruit would you like add?','Kiwi')
streamlit.write('Thanks for adding', fruit_choice)




