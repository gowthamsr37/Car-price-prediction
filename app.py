import streamlit as st
import pickle
import numpy as np
import pandas as pd


st.set_page_config(page_title="Car Price Prediction", page_icon="🚗")
st.title('Car price prediction')
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
car = pd.read_csv('cleaned_car.csv')

companies=sorted(car['company'].unique())
car_models=sorted(car['name'].unique())
year=sorted(car['year'].unique(),reverse=True)
fuel_type=car['fuel_type'].unique()

company = st.selectbox('Select the company', companies)
car_model=st.selectbox('Select the model', car[car['company']==company]['name'].unique())
year=st.selectbox('Select the year of purchase', year)
fuel_type=st.selectbox('Select the fuel type', car[car['company']==company]['fuel_type'].unique())
driven=st.selectbox('Select the KMs driven', sorted(car['kms_driven'].unique()))


if st.button('Predict the Price'):
    prediction=model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                              data=np.array([car_model,company,year,driven,fuel_type]).reshape(1, 5)))
    prediction = int(prediction[0])
    st.header('The price would be around {}'.format(prediction))




# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    </style>
                    """
st.markdown(hide_st_style, unsafe_allow_html=True)