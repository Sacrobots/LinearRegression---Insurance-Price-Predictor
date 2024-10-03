import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def readData():
    
    dataSet = pd.read_csv('insurance.csv')
    return dataSet


def dataSetDescription(dataSet):

    print("The columns present: \n", dataSet.head(5), "\n")
    print("The columns present: \n", dataSet.columns, "\n")
    print(f"The information regarding the dataset: \n{dataSet.info}\n")
    print(f"The information regarding the dataset: \n", dataSet.describe())

    print(f"The number of males vs females are: \n", dataSet['sex'].value_counts(), "\n")
    print(f"The count of each region: \n", dataSet['region'].value_counts(), "\n")
    print(f"The total number of columns: \n", dataSet.columns, "\n")


def Graphs(dataSet):
    
    # Graph to determine the distribution of Age
    st.subheader("Age Vs Charges: -")
    st.bar_chart(x = 'age', y ='charges', data=dataSet, color='#7F00FF')
    st.markdown("\n")
    st.markdown("\n")
    

    fig1 = plt.figure(figsize=(3, 3))
    fig1 = sns.displot(dataSet['age'], color='red')
    st.subheader("Age Distribution: -")
    st.pyplot(fig1)
    st.markdown("\n")
    st.markdown("\n")
    fig = sns.displot(dataSet['sex'], color='blue')
    st.subheader("Gender Distributions: -")
    st.pyplot(fig)
    st.markdown("\n")
    st.markdown("\n")
    fig = sns.displot(dataSet['smoker'], color='green')
    st.subheader("Smoker Distributions: -")
    st.pyplot(fig)
    st.markdown("\n")
    st.markdown("\n")
    fig = sns.displot(dataSet['region'], color='yellow')
    st.subheader("Region Distributions: -")
    st.pyplot(fig)
    st.markdown("\n")
    st.markdown("\n")


    

