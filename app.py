import streamlit as st 
import numpy as np
from sklearn.linear_model import LinearRegression

st.title("Thias App Running At Streamlit Framework")


# Data Dummy 
dataset = {
    'luas' : [2, 3, 4, 5, 6],
    'harga' : [1, 2, 3, 3.5, 5]
}

x_train = np.reshape(dataset['luas'], (-1,1))
y_train = dataset['harga']

model = LinearRegression()
model.fit(x_train, y_train)

luas = st.number_input("Masukkan Luas Tanah (m2) : ", min_value=0.0)

if luas: 
    predict = model.predict([[luas]])
    st.success(f"Etimasi Harga Rumah : Rp. {predict[0]:,.2f} juta")