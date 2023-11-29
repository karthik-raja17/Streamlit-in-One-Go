import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

chart_data = pd.DataFrame(np.random.randn(20,3), columns = ['Line-1','Line-2','Line-3'])

st.header('1 Charts with random numbers')
st.subheader('1.1 Line Chart')
st.line_chart(chart_data)

st.subheader('1.2 Area Chart')
st.area_chart(chart_data)

st.subheader('1.3 Bar Chart')
st.bar_chart(chart_data)

st.header('2 Data visualization with matplotlib and seaborn')
st.subheader('2.1 Loading the dataframe')
df = pd.read_csv('iris.csv')
st.dataframe(df)

st.subheader('2.1 bar graph with matplotlib')
fig = plt.figure(figsize = (15,8))
df['species'].value_counts().plot(kind = 'bar')
st.pyplot(fig)

st.subheader('2.2 Distribution plot with seaborn')
fig = plt.figure(figsize = (15,8))
sns.distplot(df['sepal_length'])
st.pyplot(fig)

st.header('3 Multiple Graph')
col1, col2 = st.columns(2)

with col1:
    col1.header = 'KDE = False'
    fig1 = plt.figure(figsize = (6,6))
    sns.distplot(df['sepal_length'], kde = False)
    st.pyplot(fig1)

with col2:
    col2.header = 'hist = False'
    fig2 = plt.figure(figsize = (6,6))
    sns.distplot(df['sepal_length'], hist = False)
    st.pyplot(fig2)

st.header('4 changing style')
col1, col2 = st.columns(2)

with col1:
    fig = plt.figure()
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.distplot(df['petal_length'], hist = False)
    st.pyplot(fig)

with col2:
    fig2 = plt.figure()
    sns.set_theme(style = 'darkgrid',context = 'poster' )
    sns.distplot(df['petal_length'], hist = False)
    st.pyplot(fig2)

st.header('5 Exploring different graphs')       #ax.scatter() is the function that creates the scatter plot.
st.subheader('5.1 Scatter plot')                 #*np.random.random() is the argument that specifies the data points for the scatter plot. The * operator unpacks the elements of the NumPy array np.random.random() into individual arguments for the ax.scatter() function.
fig,ax = plt.subplots(figsize = (15,8))          #np.random.random() is a function that generates a NumPy array of 1000 random numbers in the range.
ax.scatter(*np.random.random(size = (2,100)))
st.pyplot(fig)

st.subheader('5.2 Count plot')
fig = plt.figure(figsize = (15,8))
sns.countplot(data = df, x = 'species')
st.pyplot(fig)

st.subheader('5.3 Box plot')
fig = plt.figure(figsize = (15,8))
sns.boxplot(data = df, x = 'species', y = 'petal_length')
st.pyplot(fig)

st.subheader('5.4 violin plot')
fig = plt.figure(figsize = (15,8))
sns.violinplot(data = df, x = 'species', y = 'petal_length')
st.pyplot(fig)
