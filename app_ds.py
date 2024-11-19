import streamlit as st
from EDA import show_EDA
import distutils.core
import sklearn

from predict_pag import show_predict_pag



#Add the custom bar
st.title ('Smart Churn Pro')

#Rest of your streamlit app
page = st.selectbox('Predict or Explore', ('Predict', 'EDA'))




if page == 'Predict':
    show_predict_pag()
else:
    show_EDA()
