
# Radar del futuro

Esta plataforma tiene como objetivo mostrar los grafos del conocimiento de los 10 sectores principales de Guanajuato. De igual manera, se muestran las noticias más releventes de cada uno de ellos. 

## Archivo principal

La plataforma se carga desde el archivo app.py el cual tiene paths relativos a las carpetas que lo alimentan: 
* .stremlit : Se definen estilos del sitio y la barra de navegación
* app_info: Se define el texto a mostrar en la pagina de inicio: Titulo y descripción
* graphs: Se definen los archivos de los grafos de conocimiento
* news: Se definen los archivos de las noticias
* logos: Se define el logo a mostrar (en formato svg)

```
logo = os.path.join("logos", "LOGO_INNOVACION__HORIZONTAL_FONDO_BLANCO.svg")  
```

## Instalación de dependencias & ejecución de la aplicación
Dentro de la carpeta del proyecto, se encuentra el archivo de requirements.txt el cual contiene la paquetería a instalar. Se recomienda usar un ambiente virtual con Python >=3.8.

* Configuración del ambiente virtual

```
sudo apt-get update
sudo apt-get upgrade
sudo apt install python3-pip
sudo apt install python3-virtualenv
mkdir directory_env
virtualenv directory_env/futuros2024
```

* Activación (y desactivación) del ambiente
```
source directory_env/futuros2024/bin/activate
deactivate
```

* La carpeta de la aplicación se encuentra en radar_2024, por lo que es importante cambiar de directorio de trabajo y activar el ambiente virtual para instalar las dependencias.
```
source directory_env/futuros2024/bin/activate
cd radar_2024/
pip install -r requirements.txt 
```

* Para ejecutar (en segundo plano) la aplicación y especificar el número de puerto:
```
nohup streamlit run app.py --server.port 8502 &
```

* Notas:

    * Por default usa el puerto 8080, no es necesario el --server.port. 
    * Se requiere el & al final de la linea.
    * Si no se desea en segundo plano, ejecutar sin nohup. 
    * Para cargar actualizaciones a los archivos, detener el proceso y volver a lanzar.
    * Buscar el proceso con: ps -e | grep streamlit, y matar el proceso con el ID mostrado con kill ID.
    * Recuerda desactivar tu ambiente virtual con deactivate


## Estilo del sitio
* El tema del sitio se edita desde: .stremlit/config.toml, por default esta como:
```
    [theme]
    primaryColor = "#1a73e8"               # Primary color (links, buttons)
    backgroundColor = "#f0f0f0"             # Background color for the app
    secondaryBackgroundColor = "#f5f5f5"    # Background color for containers
    textColor = "#000000"                    # Color of the text
    font = "sans serif"                      # Font family

```
Puedes ver: https://docs.streamlit.io/develop/api-reference/configuration/config.toml para más opciones

* La barra de navegación se configura desde .streamlit/navbar_styles.json y tiene por default las opciones:
```
{
    "nav": {
        "background_color": "white",
        "height": "60px",
        "justify-content": "left"
    },
    "img": {
        "width": "180px",
        "height": "auto",
        "padding_right": "14px"
    },
    "span": {
        "color": "var(--text-color)",
        "padding": "14px"
    },
    "active": {
        "background_color": "#E4ECFA",
        "color": "var(--text-color)",
        "font_weight": "normal",
        "padding": "14px"
    }
}
```

## Organización del sitio
El sitio se divide en dos pestañas, Inicio e Información y se *alimenta* de la siguiente manera:

* Inicio: Es la pestaña de *Home*, donde se muestra:
    * El titulo y la descripción del sitio: app_info/app_content.json
    
```
    {
        "title": "Radar del Futuro",
        "description": "Este sitio ..."
    }
```

* Las noticias principales, las cuales requieren una url para la nota y una url para la foto en miniatura a mostar: news/news_feed.json

```
    {
        "Breaking News 1": {
            "url": "https://example.com/news1",
            "image": "https://picsum.photos/200"
        },
        "Breaking News 2": {
            "url": "https://example.com/news2",
            "image": "https://picsum.photos/200"
        }
    }
```

* Información: Es la pestaña donde se cargan los grafos de conocimiento segun el sector seleccionado. Los grafos por sector se cargan (y editan) desde: graphs/SECTOR.json. Es importante señalar que los sectores validos y sus respectivos archivos de carga se especifican en graphs/config.json. 

El archivo graphs/config.json tiene la forma:

```
    {
        "Agroindustrial": "Agroindustria.json", 
        "Moda" : "Moda.json",
        "Ciencias de la vida" : "Salud.json",
        "Movilidad" : "Movilidad.json",
        "Turismo" : "Turismo.json",
        "Fabricación Automotores" : "Automotor.json",
        "Productos Químicos" : "Productos_quimicos.json",
        "Servicios basados en conocimientos" : "SBS.json",
        "Energia y Agua" : "Energia_y_agua.json",
        "Gobierno" : "Gobierno.json"
    }
```

Y el archivo de cada sector, por ejemplo Agroindustria.json tiene el formato:


```
    {
        "nodes": [
            {
                "name": "Agroindustria",
                "category": 0,
                "symbolSize": 50
            },
            {
                "name": "Agricultura impulsada por IA",
                "category": 1,
                "symbolSize": 30
            },
            {
                "name": "Vegetales sin emisiones de carbono",
                "category": 2,
                "symbolSize": 30
            },
            {
                "name": "Sistemas de producción de alimentos éticos",
                "category": 3,
                "symbolSize": 30
            },
            {
                "name": "Tractores agrícolas autónomos",
                "category": 1,
                "symbolSize": 20
            },
            {
                "name": "Gallineros móviles",
                "category": 1,
                "symbolSize": 20
            },
            {
                "name": "Agricultura vertical",
                "category": 1,
                "symbolSize": 20
            },
            {
                "name": "Robots agrícolas para el monitoreo de cultivos",
                "category": 1,
                "symbolSize": 20
            },
            {
                "name": "Robots agrícolas automatizados",
                "category": 1,
                "symbolSize": 20
            },
            {
                "name": "Herramientas de previsión de agricultura basadas en inteligencia artificial",
                "category": 1,
                "symbolSize": 20
            },
            {
                "name": "Granjas con emisiones de carbono negativas",
                "category": 2,
                "symbolSize": 20
            },
            {
                "name": "Frutas carbono neutrales",
                "category": 2,
                "symbolSize": 20
            },
            {
                "name": "Piñas certificadas como carbono neutral",
                "category": 2,
                "symbolSize": 20
            },
            {
                "name": "Zanahorias verdaderamente neutras en carbono",
                "category": 2,
                "symbolSize": 20
            },
            {
                "name": "Café regenerativo",
                "category": 3,
                "symbolSize": 20
            },
            {
                "name": "Cacao alternativo",
                "category": 3,
                "symbolSize": 20
            },
            {
                "name": "Arándanos orgánicos cultivados de forma regenerativa",
                "category": 3,
                "symbolSize": 20
            }
        ],
        "links": [
            {
                "source": "Agroindustria",
                "target": "Agricultura impulsada por IA"
            },
            {
                "source": "Agricultura impulsada por IA",
                "target": "Tractores agrícolas autónomos"
            },
            {
                "source": "Agricultura impulsada por IA",
                "target": "Gallineros móviles"
            },
            {
                "source": "Agricultura impulsada por IA",
                "target": "Agricultura vertical"
            },
            {
                "source": "Agricultura impulsada por IA",
                "target": "Robots agrícolas para el monitoreo de cultivos"
            },
            {
                "source": "Agricultura impulsada por IA",
                "target": "Robots agrícolas automatizados"
            },
            {
                "source": "Agricultura impulsada por IA",
                "target": "Herramientas de previsión de agricultura basadas en inteligencia artificial"
            },
            {
                "source": "Agroindustria",
                "target": "Vegetales sin emisiones de carbono"
            },
            {
                "source": "Vegetales sin emisiones de carbono",
                "target": "Granjas con emisiones de carbono negativas"
            },
            {
                "source": "Vegetales sin emisiones de carbono",
                "target": "Frutas carbono neutrales"
            },
            {
                "source": "Vegetales sin emisiones de carbono",
                "target": "Piñas certificadas como carbono neutral"
            },
            {
                "source": "Vegetales sin emisiones de carbono",
                "target": "Zanahorias verdaderamente neutras en carbono"
            },
            {
                "source": "Agroindustria",
                "target": "Sistemas de producción de alimentos éticos"
            },
            {
                "source": "Sistemas de producción de alimentos éticos",
                "target": "Cacao alternativo"
            },
            {
                "source": "Sistemas de producción de alimentos éticos",
                "target": "Café regenerativo"
            },
            {
                "source": "Sistemas de producción de alimentos éticos",
                "target": "Arándanos orgánicos cultivados de forma regenerativa"
            }
        ],
        "categories": [
            {
                "name": "Agroindustria"
            },
            {
                "name": "Agricultura impulsada por IA"
            },
            {
                "name": "Vegetales sin emisiones de carbono"
            },
            {
                "name": "Sistemas de producción de alimentos éticos"
            }
        ]
    }
 ```

* Al seleccionar un sector, se cargan sus respectivas noticias principales, las cuales se editan desde: news/SECTOR.json, las cuales siguen el mismo formato que als noticias generales:

```
{
    "Agroindustria News 1": {
        "url": "https://example.com/news1",
        "image": "https://picsum.photos/200"    },
    "Agroindustria News 2": {
        "url": "https://example.com/news2",
        "image": "https://picsum.photos/200"    },
    "Agroindustria News 3": {
        "url": "https://example.com/news3",
        "image": "https://picsum.photos/200"    },
    "Agroindustria News 4": {
        "url": "https://example.com/news4",
        "image": "https://picsum.photos/200"    }
}
```

* Para mayor información, contactar a: 

