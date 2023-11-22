import streamlit as st
import pandas as pd

st.title('Hello')

st.write("I enjoy to discover stremalit possibilities")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)

# Here we use "magic commands":
df_weather

st.line_chart(df_weather['MAX_TEMPERATURE_C'])

name = st.text_input("Please give me your name :")
name_length = len(name)
st.write("Your name has ",name_length,"characters")