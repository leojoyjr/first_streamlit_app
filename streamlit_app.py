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
streamlit.dataframe(my_fruit_list)
