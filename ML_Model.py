from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from ReadClean import readData
import streamlit as st
import numpy as np
import pandas as pd
import joblib
import datetime
# Data Preprocessing


# Making the Smoker column and Region column into numerical values

def conversionToNumerical(dataSet):
    
    #encoding the sex columns

    dataSet.replace({'sex':{'male':0, 'female': 1}}, inplace=True)

    # smoker column
    dataSet.replace({'smoker':{'yes':0, 'no': 1}}, inplace=True)

    # for the region column

    dataSet.replace({'region':{'southeast':0,'southwest':1,'northeast':2,'northwest':3}},inplace=True)
    

    # Splitting the feature and target
    X = dataSet.drop('charges', axis = 1)
    y = dataSet['charges']

    print("\nThe first 5 entries of the X variable: \n", X.head(5))
    print("\nThe first 5 entries of the Y variable: \n", y.head(5))

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

    print(f"\nAll shapes of X_train, X_test, y_train, y_test\n{X_train.shape}, {X_test.shape}, {y_train.shape}, {y_test.shape}")

    # Linear Regression Model

    model = LinearRegression(fit_intercept= True)
    model.fit(X_train, y_train)

    joblib.dump(model,'model.pkl') # Saving the model as model.pkl
    

    # y_pred = model.predict(X_train)

    # print(f"\nPredicted score from X_train: \n{y_pred}\n")
    # print(f"Shape of the predicted X_train: \n{y_pred.shape}\n")

    # # R2 score: -

    # test_data_prediction = model.predict(X_test)
    # R2_score = metrics.r2_score(y_test, test_data_prediction)
    # print(f"The score is: {R2_score}")
    # return model
    

def  Answer(Age, Sex, BMI, NOC, Smoker, Region):
    input_data = (Age, Sex, BMI, NOC, Smoker, Region)

    #chaning it to numpy array
    input_data_as_array = np.asarray(input_data)

    #reshapping the data
    input_data_reshaped = input_data_as_array.reshape(1,-1)

    model = joblib.load("model.pkl")

    prediction = model.predict(input_data_reshaped)

    print("The person will get insurance money = ",prediction[0])
    
    st.markdown("──────────────────────── ⋆⋅☆⋅⋆ ────────────────────────\n")
    st.write(f"**--⪢ Adjust the estimated amount post-submission: ${int(prediction[0])}**")
    st.markdown("──────────────────────── ⋆⋅☆⋅⋆ ────────────────────────\n")    
    


def interface():

    with st.form(key = "form1"):
        # age,sex,bmi,children,smoker,region
        Age = st.number_input("**Enter Age: -**", min_value=5, max_value=100, label_visibility="visible")
        st.write(f"**Age of the person: {Age}**")

        Sex = st.selectbox("**Gender: -**", ("Male", "Female"))
        st.write(f"**Gender selected: {Sex}**")

        if(Sex == 'Male'):
            Sex = 0
        else:
            Sex = 1

        st.markdown("\n")
        
        BMI = st.number_input("**BMI of the person: -**", min_value=10.00, max_value=500.00, label_visibility="visible", step=1.,format="%.2f")
        st.write(f"**BMI of the person: {BMI}**")

        st.markdown("\n")
        
        NOC = st.number_input("**Enter number of children: -**", min_value=0, max_value=10, label_visibility="visible")
        st.write(f"**No. of children: {NOC}**")

        st.markdown("\n")

        smokerChecker = st.toggle("**Toggle For Smoker**", label_visibility="visible")

        if smokerChecker:
            st.write("**He is a smoker**")
            smokerChecker = 0
        else:
            st.write("**He is not a smoker**")
            smokerChecker = 1

        st.markdown("\n")

        Region = st.selectbox("**Select Region: -**", ("North East", "North West", "South East", "South West"))
        st.write(f"**Region is: {Region}**")

        if(Region == 'North East'):
            Region = 2
        elif(Region == 'North West'):
            Region = 3
        elif(Region == 'South East'):
            Region = 0
        elif(Region == 'South West'):
            Region = 1
        

        st.form_submit_button("**Submit Form**",on_click=Answer(Age, Sex, BMI, NOC, smokerChecker, Region))
        
    

    

    
