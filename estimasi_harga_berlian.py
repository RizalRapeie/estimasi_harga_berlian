import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

model = pickle.load(open('estimasi_harga_berlian.sav', 'rb'))

st.title('Estimasi Harga Berlian')
st.write('Berikut ini adalah aplikasi untuk memprediksi harga berlian')

carat = st.number_input('Karat', min_value=0.2, max_value=5.01, step=0.01)
x = st.number_input('Panjang dalam mm', min_value=3.73, max_value=10.74, step=0.01)
y = st.number_input('Lebar dalam mm', min_value=3.71, max_value=10.54, step=0.01)
z = st.number_input('Tinggi dalam mm', min_value=2.33, max_value=6.98, step=0.01)

cut = st.selectbox('Cut', ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
if cut == 'Fair':
    cut = 0
elif cut == 'Good':
    cut = 1
elif cut == 'Very Good':
    cut = 2
elif cut == 'Premium':
    cut = 3
else:
    cut = 4

color = st.selectbox('Color', ['J', 'I', 'H', 'G', 'F', 'E', 'D'])
if color == 'J':
    color = 0
elif color == 'I':
    color = 1
elif color == 'H':
    color = 2
elif color == 'G':
    color = 3
elif color == 'F':
    color = 4
elif color == 'E':
    color = 5
else:
    color = 6

clarity = st.selectbox('Clarity', ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])
# turn clarity into numerical 
if clarity == 'I1':
    clarity = 0
elif clarity == 'SI2':
    clarity = 1
elif clarity == 'SI1':
    clarity = 2
elif clarity == 'VS2':
    clarity = 3
elif clarity == 'VS1':
    clarity = 4
elif clarity == 'VVS2':
    clarity = 5
elif clarity == 'VVS1':
    clarity = 6
else:
    clarity = 7

if st.button('Estimasi'):
    # calculate its price using the model
    y_pred = model.predict([[carat, cut, color, clarity, x, y, z]])
    st.write(f'Estimasi harga berlian dalam USD : ', y_pred[0])
