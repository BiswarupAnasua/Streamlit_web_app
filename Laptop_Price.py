import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title='Laptop Price',page_icon='https://i.pinimg.com/originals/85/7e/19/857e1977ee87256455b9b597a1529522.jpg',layout='wide')

url = 'https://raw.githubusercontent.com/BiswarupAnasua/Streamlit_web_app/main/laptopPrice.csv'
data = pd.read_csv(url)
data.info()



# data = pd.read_csv('E:\Data_Analysis\Data\laptopPrice.csv')
# data.info()
st.write('This is our Data',data)
st.write('Descriptive Statistics',data.describe())

st.write('Null Values',data.isnull().sum())


st.header(':blue[Visualization]')


for i in data.columns:
    if data[i].dtype == 'object':
        fig = px.bar(data,x='Price',y=i,width=650,height=450)
        st.plotly_chart(fig)

heatmap = px.imshow(data.corr(), text_auto=True,width=850, height=600,title='Correlation')

st.plotly_chart(heatmap)

# for i in data.columns:
#     if data[i].dtype != 'object':
#         fig = data[i].hist()
#         st.plotly_chart(fig)

selection = st.multiselect('Summarized Table',data.columns, default='brand')

# clms = data.columns

st.write(data.groupby(selection).agg({'Price':'mean'}))

# data.groupby(['processor_brand', 'processor_name', 'processor_gnrtn']).agg({'Price':'mean'})


# type(selection)

