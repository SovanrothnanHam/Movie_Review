import streamlit as st

def app():
   
    # Home Page Content
    st.title('Movie Review Home Page')

    st.subheader('Welcome to the home page of our Movie Review app!')
    # Provide information about the app
    st.write('Explore and analyze movie reviews with our app. You can build a simple classification model to understand sentiments.')

    # Display an image related to movie reviews
    st.image('poster.jpg', use_column_width=True, output_format='JPEG')

    
app()
