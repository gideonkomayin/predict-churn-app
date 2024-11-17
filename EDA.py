from altair import Axis
import streamlit as st
import pandas as pd
from  matplotlib import pyplot as plt

import seaborn as sb


@st.cache_data
def load_df():
    data = pd.read_excel("Customer-Churn.xlsx")
   
    

    return data
data =  load_df()



def show_EDA():
    #st.title ('Exploratory Data Analysis')

    st.write ("""### Customer Churn Analysis""")

    

    st.write("""##### Churn By Device Protection""")

     # Create a figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))
    data['DeviceProtection'] = data['DeviceProtection'].astype(dtype='category')
    sb.set_theme(style="whitegrid")
    plt.title('Churn by Device Protection Distribution')
    sb.countplot(x='DeviceProtection', data=data, hue='Churn')
    ax.bar_label(container=ax.containers[0], label="Count of Customers");
    ax.bar_label(container=ax.containers[1], label="Count of Customers");
    plt.grid(False)

    # Display the plot using st.pyplot()
    st.pyplot(fig)

    
    st.write("""##### Churn By Tech Support""")

    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))
    data['TechSupport'] = data['TechSupport'].astype(dtype='category')
    sb.set_theme(style="whitegrid")
    plt.title('Churn by Tech Support')
    sb.countplot(x='TechSupport', data=data, hue='Churn')
    ax.bar_label(container=ax.containers[0], label="Count of Customers");
    ax.bar_label(container=ax.containers[1], label="Count of Customers");
    plt.grid(False)

    # Display the plot using st.pyplot()
    st.pyplot(fig)



    st.write("""##### Churn by Tenure""")
    fig, ax = plt.subplots(figsize=(4, 3))


    # KDE plot for 'Tenure' with different colors for 'yes' and 'no'
    sb.kdeplot(data.loc[data['Churn'] == 'Yes', 'tenure'], color='red', fill=True, label='Yes')
    sb.kdeplot(data.loc[data['Churn'] == 'No', 'tenure'], color='blue', fill=True, label='No')

    plt.xlabel('Tenure')
    plt.ylabel('Density')
    plt.legend()
    plt.grid(False)
   
    st.pyplot(fig)



    st.write("""##### Churn By Contract Type""")

    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))
    data['Contract'] = data['Contract'].astype(dtype='category')
    sb.set_theme(style="whitegrid")
    plt.title('Churn by Contract')
    sb.countplot(x='Contract', data=data, hue='Churn')
    ax.bar_label(container=ax.containers[0], label="Count of Customers");
    ax.bar_label(container=ax.containers[1], label="Count of Customers");
    plt.grid(False)

    # Display the plot using st.pyplot()
    st.pyplot(fig)


    st.write("""##### Churn By Payment Method""")

    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))
    data['PaymentMethod'] = data['PaymentMethod'].astype(dtype='category')
    sb.set_theme(style="whitegrid")
    plt.title('Churn by Payment Method')
    sb.countplot(x='PaymentMethod', data=data, hue='Churn')
    ax.bar_label(container=ax.containers[0], label="Count of Customers");
    ax.bar_label(container=ax.containers[1], label="Count of Customers");
    plt.grid(False)

    # Display the plot using st.pyplot()
    st.pyplot(fig)