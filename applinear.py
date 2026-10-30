import pickle
import streamlit as st
import pandas as pd
import joblib
from sklearn.metrics import r2_score

model=joblib.load("thirteenjuly.pkl")

st.title("RESTAURANT REVENUE")
n=st.number_input("enter no of customers",min_value=10,max_value=99,value=10)
menu=st.number_input("enter menu price",min_value=10.01,max_value=49.97,value=10.01)
marketing=st.number_input("enter marketing spend",min_value=0.00,max_value=10.99,value=0.00)
average=st.number_input("enter average customer spending",min_value=10.20,max_value=49.90,value=10.20)
revenue=st.button("Predict revenue")
if revenue:
    data=pd.DataFrame({"Number_of_Customers":[n],"Menu_Price":[menu],"Marketing_Spend":[marketing],"Average_Customer_Spending":[average]})
    prediction=model.predict(data)
    
    st.success(f"predicted monthly revenue:{prediction[0]}")
    