import numpy as np
import pandas as pd
import streamlit as st
import datetime as dt

st.title("When's the next Birthday??")

df = pd.read_csv('Birthdays.csv')

date = dt.date.today()

def g(x):
    y = x.split('-')
    y[0] = int(y[0])
    y[1] = int(y[1])
    y[2] = int(y[2])
    z = dt.date(date.year, y[1], y[2])
    d = z - date
    if  z < date:
        p = d + dt.timedelta(365)
    else:
        p = d
    return p
 
df['days'] = df['Birthday'].apply(g)

i = df[df['days'] == df['days'].min()].index[0]

name = df['Name'][i]
date1 = df['Birthday'][i]
days = df['days'][i]

n = list(df['Name'])

st.text("The next Birthday is...")
button = st.button("Click me!")
if button:
    st.balloons()
    st.text(f'{name}\'s birthday is in {days}.days days on {date1}')

st.text("Looking for someone's Birthday?")
e = st.selectbox('Name', n)
v = df['Birthday'][e]
st.text(f'{e}\'s birthday is on {v}')

st.text('Show me everyone\'s Birthday?')
b = st.button('Yes!')
if b:
    df
