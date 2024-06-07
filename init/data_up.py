# data_app.py
import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import test_img 
# from test_img import check
from run import check
st.title("Data Exploration App")

# Upload CSV file
uploaded_file = st.file_uploader("Choose a python", type="py")

if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    # df = pd.read_csv(uploaded_file)
    # st.write("Data Preview:")
    # st.write(df.head())
    
    # # Select columns to plot
    # columns = df.columns.tolist()
    # x_axis = st.selectbox("Select X-axis column", columns)
    # y_axis = st.selectbox("Select Y-axis column", columns)
    
    # # Plotting
    # if x_axis and y_axis:
    #     st.subheader(f"Plot of {y_axis} vs {x_axis}")
    #     plt.figure(figsize=(10, 6))
    #     plt.scatter(df[x_axis], df[y_axis])
    #     plt.xlabel(x_axis)
    #     plt.ylabel(y_axis)
    #     plt.title(f"Scatter plot of {y_axis} vs {x_axis}")
    #     st.pyplot(plt)
    # print("aaa")
    # # a = import test_img
    st.pyplot(check(True))
    print("ssss")