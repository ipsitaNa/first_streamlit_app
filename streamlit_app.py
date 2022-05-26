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
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)

#lets put a pick list for users to select their own fruits to include in their smoothie
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)
