import streamlit as st
import pandas as pd
import seaborn as ssn
import time
import plotly.express as px

data = pd.read_csv('zomato_dataset.csv')


st.set_page_config(page_title='Zomato Food Price',page_icon='chart_with_upwards_trend',layout='wide')


st.header(':red[Zomato food Price Analysis]')

st.text("This Kaggle dataset contains information about \n 850 restaurants listed on the popular online food delivery \n and restaurant discovery platform, Zomato. The dataset provides a comprehensive \n collection of restaurant details, including their names, locations, ratings, cuisines, pricing, \n and more. This data is valuable for data analysis, market research, and gaining insights \n into the restaurant landscape in various cities.")


st.write('This is our Data',data.head())
st.write('Descriptive Statistics',data.describe())
st.write('Checking NULL Values',data.isnull().sum())


# st.sidebar.header('Dashboard')

# total_votes_based_on_city = ssn.barplot(x='Votes',y='City',data=data)

# st.pyplot(total_votes_based_on_city)

# total_votes_based_on_city


print(data.columns)

group_Delivery_Rating = data.groupby('City')['Delivery_Rating'].sum().reset_index()



bar = px.bar(group_Delivery_Rating,x='City',y= 'Delivery_Rating',template='seaborn',title=' Delivery Rating of Cities Based on Votes ')

st.plotly_chart(bar)

heatmap = px.density_heatmap


with st.spinner('Loading...'):
    time.sleep(5)
st.success('Done!')








