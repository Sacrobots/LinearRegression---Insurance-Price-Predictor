import streamlit as st
import pandas as pd


def presentData():
    
    dataSet = pd.read_csv('insurance.csv', index_col= 0)


    st.dataframe(dataSet, width=800, height=400)