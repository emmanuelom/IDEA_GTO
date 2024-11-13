import streamlit as st
from streamlit_echarts import st_echarts
import json
import os
from utils.news import show_news


####################################################################################################
# load data functions
@st.cache_data
def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Render functions
def render_graph(data, width="100%", height="600px", label_font_size=12):
    option = {
        "tooltip": {},
        "legend": [
            {
                "data": [category["name"] for category in data["categories"]]
            }
        ],
        "series": [
            {
                "type": "graph",
                "layout": "force",
                "data": data["nodes"],
                "links": data["links"],
                "categories": data["categories"],
                "roam": True,
                "label": {
                    "show": True,
                    "position": "right",
                    "fontSize": label_font_size  
                },
                "draggable": True,
                "force": {
                    "repulsion": 400
                },
            }
        ]
    }

    # Use st_echarts with events
    events = {
        "click": "function(params) { return params.data; }"
    }
    
    selected_node = st_echarts(options=option, width=width, height=height, events=events)
    
    return selected_node

####################################################################################################

def show_graph():
    graph_parent_path = "graphs"
    # Load sectors config file
    sectors_config = load_data(os.path.join(graph_parent_path, "config.json"))
    sectors = list(sectors_config.keys())
    api_options = tuple(["---"] + sectors)

    # Create containers 
    sidebar_container = st.container(border=True)
    
    with sidebar_container:
        # Sector selector
        st.header("Sector", anchor=False)
        selected_api = st.selectbox(
            label="Selecciona una opción",
            options=api_options,
        )
        
    # Add Sector subheader 
    st.markdown("---")
    is_selected = True if selected_api != '---' else False
    st.subheader(f"Sector: {selected_api if is_selected else ' Seleccione un sector'}", anchor=False)

    # Add the graph container
    plot_container = st.container(border=True)
    info_container = st.expander("Ver noticias")

    # get graph data only if a sector is selected
    if is_selected:
        try: 
            graph_data = load_data(os.path.join(graph_parent_path, sectors_config[selected_api]))

            # Plot graph
            with plot_container:
                render_graph(graph_data, width="100%", height="700px", label_font_size=12)
        except: 
            st.write(f"Sin información disponible en el eje {selected_api}")

        
        with info_container:
            st.subheader(f"Noticias relevantes del sector {selected_api}")
            show_news("news", sectors_config[selected_api])

        st.markdown("---")

###################################################################################################