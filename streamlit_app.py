import streamlit

streamlit.title("My Mom's new healthy diner")

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega3 & Blueberry Oat meal')
streamlit.text('🥗 Kale,Spinach & Rocket smoothie')
streamlit.text('🐔 Hard-Boiled Free-range egg')
streamlit.text('🥑🍞 Avocado Tost')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
