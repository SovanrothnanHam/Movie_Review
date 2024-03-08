import streamlit as st
import pandas as pd
import plotly.express as px  # Plotly library for interactive charts
from textblob import TextBlob  # Sentiment Analysis Library

def app():
    # Streamlit App Header
    st.title("Movie Reviews Intelligent Analysis System")
    st.subheader('Welcome to the movie review page of our Movie Review app!')

    st.write("Explore the sentiment analysis of movie reviews using our intelligent system.")
    # Upload Dataset Option
    uploaded_file = st.file_uploader("Upload Movie Reviews Dataset (CSV)", type=["csv"])
   
    # Analyze Option
    if uploaded_file is not None:
        # Load dataset
        df = pd.read_csv(uploaded_file)

        # Display a sample of the dataset
        st.subheader("Sample of the Uploaded Dataset:")
        st.dataframe(df.head())

        # Perform Sentiment Analysis
        df['Sentiment'] = df['text'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

        # Display Overall Sentiment Distribution as Pie Chart
        display_sentiment_distribution(df)

       
        

# Function to display Overall Sentiment Distribution as Pie Chart using Plotly

def display_sentiment_distribution(df):
    st.subheader("Overall Sentiment Distribution:")
    # Define a custom color sequence with blue for positive sentiment
    custom_colors = ['#66B2FF', '#FF9999', '#99FF99']  # Replace with your desired colors

    # Create a pie chart using Plotly
    fig = px.pie(df, names=df['Sentiment'].apply(get_sentiment_category).value_counts().index,
                 values=df['Sentiment'].apply(get_sentiment_category).value_counts().values,
                 labels={'labels': 'Sentiment', 'values': 'Count'},
                 hole=0.3,
                 color_discrete_sequence=custom_colors)
    
    # Display the pie chart
    st.plotly_chart(fig)


# Function to categorize sentiment into positive, negative, or neutral
def get_sentiment_category(sentiment):
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

if __name__ == "__main__":
    # Run the app: streamlit run script_name.py
    app()

