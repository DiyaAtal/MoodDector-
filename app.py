import streamlit as st

# Title of the app
st.title("MoodCheck: Analyze, Improve, Thrive")

# Instructions
st.write("Welcome! This app will help you detect your mood and suggest recommendations to improve it.")
st.write("Please enter a short sentence or paragraph to analyze your mood.")

# Input text from the user
user_input = st.text_area("Your mood input:")

# Display the input text
if user_input:
    st.write("You wrote: ", user_input)
