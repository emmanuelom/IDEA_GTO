import streamlit as st
from streamlit_navigation_bar import st_navbar
import json
import os
import pages as pg


#######################################################################################################
# Tab title and icon 
# Setting up the page config
st.set_page_config(page_title="Radar del futuro", page_icon=":robot_face:", layout="wide", initial_sidebar_state="collapsed")

#######################################################################################################
#######################################################################################################
# Navigation bar
logo = os.path.join("logos", "LOGO_INNOVACION__HORIZONTAL_FONDO_BLANCO.svg")  
functions = {
    "Home": pg.show_home, # by default
    "Inicio": pg.show_home,
    "Información": pg.show_graph,
}
pages = list(functions.keys())[1:] # remove default 'Home'

# Load styles from the JSON file
with open('.streamlit/navbar_styles.json') as f:
    styles = json.load(f)



options = {
    "show_menu": False,
    "show_sidebar": False,
}

selected_page = st_navbar(
    pages=pages,
    logo_path=logo,
    styles=styles,
    options=options,
)

#######################################################################################################
# Body
# Load app content 
# Add a content div to offset the header
st.markdown('<div class="content">', unsafe_allow_html=True)

go_to = functions.get(selected_page)
if go_to:
    go_to()

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