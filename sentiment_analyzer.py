import streamlit as st
from textblob import TextBlob

# Title of the app
st.title("Sentiment Analyzer")

# Subtitle
st.subheader("Analyze the Sentiment of Your Movie Review")

# Input text box for movie review
user_input = st.text_area("Enter a movie review:", "")

# Check if the user has entered a review
if st.button("Analyze Sentiment"):
    if user_input:
        # Perform sentiment analysis
        analysis = TextBlob(user_input)
        sentiment = analysis.sentiment.polarity
        
        # Display the result
        if sentiment > 0:
            st.write("The sentiment of this review is **Positive**.")
        elif sentiment < 0:
            st.write("The sentiment of this review is **Negative**.")
        else:
            st.write("The sentiment of this review is **Neutral**.")
    else:
        st.write("Please enter a movie review to analyze.")
