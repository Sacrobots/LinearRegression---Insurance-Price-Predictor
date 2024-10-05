from ML_Model import *
from ReadClean import *
import streamlit as st
from Original_CSV_File import presentData


first = readData()

dataSetDescription(first)
    

def main_page():
    st.title("**Insurance Price Predicator**")
    st.sidebar.markdown("**Enter Person's Details 😄**")
    
    # conversionToNumerical(first)
    interface()



def page2():
    st.title("**Graphical Representation Chart 📊**")
    st.sidebar.markdown("**Original CSV Charts Representation 📊**")
    Graphs(first)


def page3():
    st.title("**Dataset Presented Below**")
    st.sidebar.markdown("**Contents Of CSV 📋**")
    presentData()
    

page_names_to_funcs = {
    "Insurance Price Predicator 🔰": main_page,
    "Graphical Representation": page2,
    "Contents Of Original CSV File": page3
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())

page_names_to_funcs[selected_page]()
