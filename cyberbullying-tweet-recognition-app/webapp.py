# importing libraries
import pandas as pd
import streamlit as st
from PIL import Image
from functions import custom_input_prediction  # Ensure this function is optimized
from io import BytesIO

# Page title
image = Image.open('images/logo.png')

st.image(image, use_column_width=True)

st.write('''
# Cyberbullying Tweet Recognition App

This app predicts the nature of the tweet into 6 Categories.
* Age
* Ethnicity
* Gender
* Religion
* Other Cyberbullying
* Not Cyberbullying

***
''')

# Text Box for direct input
st.header('Enter Tweet')
tweet_input = st.text_area("Tweet Input", height=150)

st.write('''
***
''')

# Print input on the webpage
st.header("Entered Tweet text")
if tweet_input:
    st.write(tweet_input)
else:
    st.write('''
    ***No Tweet Text Entered!***
    ''')
st.write('''
***
''')

# Output on the page
st.header("Prediction")
if tweet_input:
    prediction = custom_input_prediction(tweet_input)
    if prediction == "Age":
        st.image("images/age_cyberbullying.png", use_column_width=True)
    elif prediction == "Ethnicity":
        st.image("images/ethnicity_cyberbullying.png", use_column_width=True)
    elif prediction == "Gender":
        st.image("images/gender_cyberbullying.png", use_column_width=True)
    elif prediction == "Not Cyberbullying":
        st.image("images/not_cyberbullying.png", use_column_width=True)
    elif prediction == "Other Cyberbullying":
        st.image("images/other_cyberbullying.png", use_column_width=True)
    elif prediction == "Religion":
        st.image("images/religion_cyberbullying.png", use_column_width=True)
else:
    st.write('''
    ***No Tweet Text Entered!***
    ''')

st.write('''***''')

# File uploader
st.header("Or Upload a CSV File with Tweets")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Check if the uploaded file has the correct name
    if uploaded_file.name == "sample1.csv":
        # Read the CSV file
        df = pd.read_csv(uploaded_file)
        
        # Check if the uploaded file contains a 'tweet_text' column
        if 'tweet_text' in df.columns:
            # Process each tweet in the file and predict
            df['Prediction'] = df['tweet_text'].apply(custom_input_prediction)
            
            # Calculate counts and percentages
            counts = df['Prediction'].value_counts()
            percentages = df['Prediction'].value_counts(normalize=True) * 100
            
            # Create a DataFrame for displaying counts and percentages
            result_df = pd.DataFrame({
                'Category': counts.index,
                'Count': counts.values,
                'Percentage (%)': percentages.values
            })
            
            # Display the DataFrame as a table
            st.write("### Table of Counts and Percentages")
            st.dataframe(result_df, use_container_width=True)
            st.write("PLEASE TAKE NECESSARY ACTION")
            
            # Create DataFrame for export
            export_df = df[['tweet_text', 'Prediction']].copy()
            export_df.rename(columns={'tweet_text': 'Cyber_Bully_Tweet', 'Prediction': 'Classification'}, inplace=True)
            
            # Convert the DataFrame to Excel format
            excel_buffer = BytesIO()
            with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
                export_df.to_excel(writer, sheet_name='Results', index=False)
                writer.close()
            excel_buffer.seek(0)
            
            # Download button
            st.download_button(
                label="Download Results as Excel",
                data=excel_buffer,
                file_name='cyber_bullying_results.xlsx',
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
        else:
            st.error("The uploaded CSV file does not contain a 'tweet_text' column.")
    else:
        st.error("Please upload a file named 'sample1.csv'.")

# About section
expand_bar = st.expander("About")
expand_bar.markdown('''
* **Dataset:** [https://www.kaggle.com/datasets/andrewmvd/cyberbullying-classification](https://www.kaggle.com/datasets/andrewmvd/cyberbullying-classification)
''')