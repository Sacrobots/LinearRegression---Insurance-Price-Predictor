import streamlit as st
import pandas as pd


def presentData():
    
    dataSet = pd.read_csv('insurance.csv', index_col= 0)


    st.dataframe(dataSet, width=800, height=400)
    total_records = len(dataSet)
    print(f"**The total number of records: {total_records}**")
