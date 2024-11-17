import streamlit as st
import pickle 
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline


# Load model
def load_model():
    with open('pipe_chnmod_.pkl', 'rb') as file:
        df = pickle.load(file)
    return df

df = load_model()
pipe = df['model']





def show_predict_pag():
    st.write("""### Customer Churn prediction""")
    st.write("""###### Kindly enter details""")

    DeviceProtection_options = ('No', 'No internet service', 'Yes')
    TechSupport_options = ('No', 'No internet service', 'Yes')
    Contract_options = ('Month-to-month', 'One year', 'Two year')
    PaymentMethod_options = ('Bank transfer (automatic)', 'Credit card (automatic)', 'Electronic check', 'Mailed check')
    

   
    DeviceProtection = st.selectbox('Device Protection', DeviceProtection_options)
    TechSupport = st.selectbox('Tech Support', TechSupport_options)
    Contract = st.selectbox('Contract type', Contract_options)
    PaymentMethod = st.selectbox('Payment Method', PaymentMethod_options)

    
    tenure = st.slider ('Number of Tenure', 0, 100, 1)
  

   

    ok = st.button("Predict Customer Churn")
    if ok:
        
        expected_columns = ['tenure', 'DeviceProtection', 'TechSupport', 'Contract',
       'PaymentMethod']
        
        user_data = pd.DataFrame([[tenure, DeviceProtection, TechSupport, Contract, PaymentMethod]],
                       columns=expected_columns)

        # Make sure categorical columns have the correct data type
        user_data['DeviceProtection'] = user_data['DeviceProtection'].astype('category')
        user_data['TechSupport'] = user_data['TechSupport'].astype('category')
        user_data['Contract'] = user_data['Contract'].astype('category')
        user_data['PaymentMethod'] = user_data['PaymentMethod'].astype('category')
       

        #user_input = ([[DeviceProtection, TechSupport, Contract, PaymentMethod,
              
                      #tenure]])

        #user_data = pd.DataFrame([user_input])

        

# Make predictions and obtain probabilities
        churn_proba = pipe.predict_proba(user_data)[:, 1]  # Assuming you want the probability of the positive class

# ... ( Make a decision based on a threshold (adjust the threshold as needed)
        threshold = 0.5
        churn = 1 if churn_proba > threshold else 0

    # Output results
        if churn == 1:
            st.subheader(f'This customer will churn with a probability of {churn_proba[0]*100:.2f}%')
        else:
            st.subheader(f'This customer will not churn with a probability of {(1 - churn_proba[0])*100:.2f}%')
        

       