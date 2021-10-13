import streamlit as st
import pandas as pd
from streamlit_keplergl import keplergl_static


df=pd.read_csv('western.csv')
# print('Shape=>',df.shape)
# print(df.head())

from keplergl import KeplerGl
map1=KeplerGl(height=600)
map1.add_data(data=df,name='western province')


# display streamlit map
keplergl_static(map1)

# st.header("Interactive Widgets")
# st.radio("Choose One", ["To be", "Not to be"])
# st.slider("How old are you?", min_value=1, max_value=100)
# st.date_input("Choose your favorite date")
