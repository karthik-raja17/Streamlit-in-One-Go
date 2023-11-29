import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import plotly.express as px
import plotly.figure_factory as ff

#altair scatter plot

st.header('1. Altair Scatter plot')

chart_data = pd.DataFrame(np.random.randn(500,5), columns = ['a','b','c','d','e'])
chart = alt.Chart(chart_data).mark_circle().encode(x= 'a',y = 'b',size = 'c', tooltip = ['a','b','c','d','e'])
st.altair_chart(chart)

#Interactive Line Charts

st.header('2. Interactive Line charts')
df = pd.read_csv('lang_data.csv')
lang_list = df.columns.tolist()
lang_choices = st.multiselect('Select the language(s)', lang_list)
new_df = df[lang_choices]
st.subheader('2.1 Line Chart')
st.line_chart(new_df)

st.subheader('2.1 Area Chart')
st.area_chart(new_df)

st.header('3. Data visualization with plotly')
st.subheader('3.1 Displaying the dataset')

df = pd.read_csv('tips.csv')
st.dataframe(df.head())

st.subheader('3.2 Pie chart')
fig = px.pie(df, values = 'total_bill', names = 'day')
st.plotly_chart(fig)

st.subheader('3.3 Pie chart with multiple parameters')
fig = px.pie(df, values = 'total_bill', names = 'day', opacity = .2, color_discrete_sequence = px.colors.sequential.RdBu)
st.plotly_chart(fig)

st.subheader('3.4 Histogram')
x1 = np.random.randn(200)
x2 = np.random.randn(200)
x3 = np.random.randn(200)

hist_data = [x1,x2,x3]
group_label = ['Group - 1','Group - 2','Group - 3']
fig = ff.create_distplot(hist_data,group_label,bin_size = [.1,.25,.5])
st.plotly_chart(fig)
