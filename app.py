import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open('svm.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))


st.title('Loan_Prediction')

Sex  = st.selectbox('Sex',df['Gender'].unique())
Married = st.selectbox('Married', df['Married'].unique())
Dependents = st.selectbox('Dependents',df['Dependents'].unique())
Education = st.selectbox('Education:',df['Education'].unique())
Self_Employed = st.selectbox('Self_Employed',df['Self_Employed'].unique())
ApplicantIncome = st.number_input('ApplicationIncome:')
CoapplicantIncome = st.number_input('CoapplicantIncome:')
LoanAmount= st.number_input('LoanAmount: ')
Loan_Amount_term= st.number_input('Loan_Amount_Term:')
Credit_History = st.selectbox('Credit_History', df['Credit_History'].unique())
Property_Area = st.selectbox('Property_Area', df['Property_Area'].unique())


result=''
if st.button('Predict'):
    input = pd.DataFrame([[Sex, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_term, Credit_History, Property_Area
]], columns=['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History','Property_Area'
])
    prediction = model.predict(input)
    if (prediction[0] == 0):
        result="You are not approved for loan"
    else:
        result="You are approved for loan"


st.success(result)