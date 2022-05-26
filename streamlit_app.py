import streamlit
streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 and Blueberry oatmeal')
streamlit.text('🥗 Kale spinach and rocket smoothie')
streamlit.text('🐔 Hard boiled free range egg')
streamlit.text('🥑🍞 Hard boiled free range egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list =pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

#lets put a pick list for users to select their own fruits to include in their smoothie
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
#display the table on the page
streamlit.dataframe(my_fruit_list)
