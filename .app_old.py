import streamlit as st
from streamlit_navigation_bar import st_navbar
import json
import os
import base64

#######################################################################################################
# Loading functions


# Function to load an image and return it as base64
def load_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

@st.cache_data(ttl=600)  # Cache the app content loading function
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

@st.cache_data(ttl=600)  # Cache the news items loading function
def load_news_items():
    try:
        with open("news/news_feed.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        st.error("The news feed file 'news_feed.json' was not found.")
        return {}
    except json.JSONDecodeError:
        st.error("Error decoding JSON. Please check the structure of 'news_feed.json'.")
        return {}

#######################################################################################################
#######################################################################################################
# Tab title and icon 
# Setting up the page config
st.set_page_config(page_title="Welcome App", page_icon=":tada:", layout="wide")

#######################################################################################################
#######################################################################################################
# Header
# Load the logos from the 'logos/' folder

left_logo_path = os.path.join("logos", "LOGO_INNOVACION__HORIZONTAL_FONDO_BLANCO.png")  
right_logo_path = os.path.join("logos", "ulsa-logo.png")  

# Load logos
left_logo_path = os.path.join("logos", "LOGO_INNOVACION__HORIZONTAL_FONDO_BLANCO.png")  
right_logo_path = os.path.join("logos", "ulsa-logo.png")  

# Load images as base64
left_logo_base64 = load_image(left_logo_path)
right_logo_base64 = load_image(right_logo_path)

# Header with institutional logos using st.markdown
st.markdown(
    f"""
    <style>
        .header-container {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px;
            background-color: white;
            border-bottom: 1px solid #ddd;
            position: fixed; /* Fixed position */
            top: 0; /* Align at the top */
            left: 0;
            right: 0;
            z-index: 9999; /* Ensure it's on top of other content */
        }}
        .content {{
            margin-top: 80px; /* Space for the fixed header */
        }}
        .logo {{
            height: 60px; /* Set a fixed height for logos */
            object-fit: contain; /* Ensure the image is scaled correctly */
        }}
    </style>
    <div class="header-container">
        <div class="left-logo">
            <img src="data:image/png;base64,{left_logo_base64}" alt="Left Logo" class="logo">
        </div>
        <div class="right-logo">
            <img src="data:image/png;base64,{right_logo_base64}" alt="Right Logo" class="logo">
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Add a content div to offset the header
st.markdown('<div class="content">', unsafe_allow_html=True)

#######################################################################################################
# Navigation bar
logo = os.path.join("logos", "LOGO_INNOVACION__HORIZONTAL_FONDO_BLANCO.svg")  

styles = {
    "nav": {
        "background-color": "white",
        "justify-content": "left",
         "height": "60px", 
    },
    "img": {
        "width": "180px",  # Adjust width as needed
        "height": "auto",  # Use "auto" to maintain aspect ratio, or specify a fixed height
        "padding-right": "14px",
    },
    "span": {
        "color": "royalblue",
        "padding": "14px",
    },
    "active": {
        "background-color": "royalblue",
        "color": "var(--text-color)",
        "font-weight": "normal",
        "padding": "14px",
    }
}
options = {
    "show_menu": False,
    "show_sidebar": False,
}

selected_page = st_navbar(
    pages=["Home", "Second Page"],
    logo_path=logo,
    styles=styles,
    options=options,
)

#######################################################################################################
# Body
# Load app content and news items
app_content = load_app_content()
news_items = load_news_items()

# Title for the welcome page from JSON
st.title(app_content.get("title", "Default title!"), anchor=False)

# Description and Instructions from JSON
st.write(app_content.get("description", "Default description!"), anchor=False)

st.markdown("---")

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

st.markdown("---")

#######################################################################################################
###########################################################################################################
# Footer with institutional legends
st.markdown(
    """
        <style>
        .footer-container {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            text-align: center;
            padding: 10px 0;
            font-size: 0.7em;
            color: #666;
            border-top: 1px solid #ddd;
            background-color: #E4ECFA;
            height: 60px; 
        }
    </style>
    <div class="footer-container">
        <p>Universidad De La Salle Bajío - Dirección de Investigación y Doctorado &copy; Copyright 2024. <br /> Investigación de futuros: Prospectiva de tendencias científicas y tecnológicas en Guanajuato. Con clave IDEA GTO/SG/386/2023</p>
    </div>
    """,
    unsafe_allow_html=True
)

###########################################################################################################
# Hide development elements

# Add custom CSS to hide the entire header section
hide_header = """
        <style>
        header[data-testid="stHeader"] {
            display: none !important;
        }
        </style>
        """

st.markdown(hide_header, unsafe_allow_html=True)

# Add custom CSS to hide the "Manage app" button
hide_manage_app_button = """
        <style>
        button[data-testid="manage-app-button"] {
            display: none !important;
        }
        </style>
        """

st.markdown(hide_manage_app_button, unsafe_allow_html=True)

# Add custom CSS to hide the Hosted with stremlit element
hide_div_element = """
        <style>
        div.viewerBadge_link__qRIco {
            display: none !important;
        }
        </style>
        """

st.markdown(hide_div_element, unsafe_allow_html=True)