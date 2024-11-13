import streamlit as st
import json
import os
from utils.news import show_news


###################################################################################################
# Loaading function
parent_dir = os.path.dirname(os.path.abspath(__file__))

@st.cache_data # Cache the app content loading function can add((ttl=600))
def load_app_content():
    try:
        with open("app_info/app_content.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        st.error("The app content file 'app_content.json' was not found.")
        return {"title": "Welcome to the News App!", "description": "Stay updated with the latest news. Click on the links below to read more!"}
    except json.JSONDecodeError:
        st.error("Error decoding JSON. Please check the structure of 'app_content.json'.")
        return {"title": "Welcome to the News App!", "description": "Stay updated with the latest news. Click on the links below to read more!"}

###################################################################################################
    
###################################################################################################
# body
def show_home():
    # Body
    # Load app content and news items
    app_content = load_app_content()
    #news_items = load_news_items()

    # Title for the welcome page from JSON
    st.title(app_content.get("title", "Default title!"), anchor=False)

    # Description and Instructions from JSON
    st.write(app_content.get("description", "Default description!"))

    st.markdown("---")
    show_news("news", "news_feed.json")

###################################################################################################