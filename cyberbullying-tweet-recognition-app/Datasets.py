import streamlit as st
import pandas as pd

# Load the dataset
df_cyberbullying_classification = pd.read_csv(r"C:\Users\sripr\cyberbullying-tweet-recognition-app\cyberbullying_tweets.csv")

# Page title
st.title("Dataset Information")

# Print the shape of the dataset
st.write("Shape of the Dataset:", df_cyberbullying_classification.shape)

# Print the columns of the dataset
st.write("Columns:", df_cyberbullying_classification.columns.tolist())

# Print the first few rows of the dataset
st.write("First 5 Rows:")
st.write(df_cyberbullying_classification.head())

# Display the complete dataset
st.write("Complete Dataset:")
st.write(df_cyberbullying_classification)
