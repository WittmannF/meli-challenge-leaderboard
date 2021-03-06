import streamlit as st
import pandas as pd

DF_URL = 'https://raw.githubusercontent.com/WittmannF/meli-challenge-leaderboard/main/leaderboard/leaderboard.csv'

st.title('Meli Kaggle-like Leaderboard')
st.write('This web app is going to keep track of the Meli Leaderboard in order to always display the top scores here')
df = pd.read_csv(DF_URL)
cols_display = ['Username', 'Top Score', 'Submits']
df = df[cols_display]
df.columns = ['Username', 'Best Score', 'Submits']
df.index = df.index+1
st.table(df)
