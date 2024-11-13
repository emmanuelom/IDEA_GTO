import streamlit as st
import json
import os

@st.cache_data # Cache the news items loading function
def load_news_items(parent_folder, news_file):
    try:
        with open(os.path.join(parent_folder, news_file), "r") as file:
            return json.load(file)
    except FileNotFoundError:
        st.error(f"The news feed file '{news_file}' was not found.")
        return {}
    except json.JSONDecodeError:
        st.error(f"Error decoding JSON. Please check the structure of '{news_file}'.")
        return {}
    

def show_news(parent_folder, news_file):
    news_items = load_news_items(parent_folder, news_file)
    if news_items:
        # Display news items in a 4x4 grid layout
        cols = st.columns(4)  # Creating a 4-column layout for the grid
        for i, (title, content) in enumerate(news_items.items()):
            url = content["url"]
            image_url = content["image"]
            col = cols[i % 4]  # Select the column based on the index for 4x4 layout
            with col:
                # Display each news item in a bordered box with an image
                st.markdown(
                    f"""
                    <div style="border:1px solid #ddd; padding: 15px; margin: 5px; border-radius: 5px; text-align:center;">
                        <a href="{url}" target="_blank">
                            <img src="{image_url}" alt="{title}" style="width:50%; height:auto; max-height:150px; border-radius:5px; margin-bottom:10px;">
                        </a>
                        <h4 style="margin-bottom: 10px;">{title}</h4>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
    else:
        st.write("No news items available.")
