import streamlit as st
from multiapp import MultiApp
from pages import Home, MovieReview # import your app modules here

app = MultiApp()

st.markdown("""
# Movie Review App

""")

# Add all your application here
app.add_app("Home", Home.app)
app.add_app("MovieReview", MovieReview.app)

# The main app
app.run()

