from ML_Model import *
from ReadClean import *
import streamlit as st




first = readData()

dataSetDescription(first)
    

def main_page():
    st.title("**Insurance Price Predicator**")
    st.sidebar.markdown("**Enter Person's Details 😄**")
    
    # conversionToNumerical(first)
    interface()



def page2():
    st.title("**Graphical Representation Chart**")
    st.sidebar.markdown("**Original CSV Charts Representation 📊**")
    Graphs(first)

    

page_names_to_funcs = {
    "Insurance Price Predicator 🔰": main_page,
    "Graphical Representation": page2
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())

page_names_to_funcs[selected_page]()