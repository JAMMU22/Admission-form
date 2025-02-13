import streamlit as st
import pandas as pd
import os

# Custom CSS to set background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: gray;
    }
    input[type="text"] {
        transition: background-color 0.3s ease;
    }
    input[type="text"]:hover {
        background-color: lightblue;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.header("Admission form for registration")

# Define the filename for the Excel file
filename = 'Book2.xlsx'

def create_admission_form():
    # Check if file exists; if so, read existing data
    if os.path.exists(filename):
        df = pd.read_excel(filename)
    else:
        # Create an empty DataFrame with the required columns
        columns = ['Name', 'Age', 'Email', 'Course']
        df = pd.DataFrame(columns=columns)

    # Get user input using Streamlit
    name = st.text_input('Enter your Name:')
    age = st.text_input('Enter your Age:')
    email = st.text_input('Enter your Email:')
    course = st.text_input('Enter the Course you wish to apply for:')

    if st.button('Submit'):
        # Create a new record
        new_record = pd.DataFrame({
            'Name': [name],
            'Age': [age],
            'Email': [email],
            'Course': [course]
        })

        # Append the new record to the existing DataFrame
        df = pd.concat([df, new_record], ignore_index=True)

        # Save the updated DataFrame to Excel
        df.to_excel(filename, index=False)

        st.success('Your data has been saved to ' + filename)

if __name__ == "__main__":
    create_admission_form()