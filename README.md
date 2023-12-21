# Práctica final programación II
  **Descripción del Proyecto:**
  
  El proyecto se base de una plataforma interactiva desarrollada en Streamlit que permite la visualización y análisis de datos relacionados con los 2640 individuos más ricos a nivel mundial, conforme a la clasificación elaborada por la revista Forbes. Este grupo de billonarios ha sido sometido a diversas formas de investigación, proporcionando información de interés sobre su patrimonio, origen de su riqueza, y otros aspectos significativos.
  
  Para facilitar la presentación de los datos, se ha implementado un servidor backend mediante FastAPI. Este backend se encarga de suministrar la información desde el archivo CSV correspondiente al frontend de la aplicación de Streamlit, permitiendo así una experiencia de usuario fluida y dinámica.
  
  **Visualizaciones Implementadas:**
  
  *Información del Billonario más Rico:*
  
  Nombre Patrimonio Ciudad de residencia País de residencia Empresa asociada Origen de la riqueza (adquirida por méritos propios o heredada)
  
  *Riqueza Total por Sector:*
  
  Se presenta una visión general del total de riqueza acumulada, clasificada por diferentes sectores.
  
  *Comparación de Self-Made vs. Inherited por Sexo:*
  
  Se explora la distinción entre fortunas generadas de manera autónoma y aquellas adquiridas por herencia, diferenciadas por género.
  
  *Edad Promedio por Sector:*
  
  Analizando la distribución de edades, se proporciona una visión promedio de edades en función de los distintos sectores económicos.
  
  *Top 10 de Países/Ciudades por Riqueza Total:*
  
  Ofrece una perspectiva de los diez principales países y ciudades que tienen la mayor concentración de riqueza, facilitando así la identificación de territorios económicos clave.
  
  *Mapa Interactivo:*
  
  Utilizando la librería Folium, se ha implementado un mapa interactivo que visualiza la distribución geográfica de los billonarios a nivel mundial, resaltando la riqueza total asociada a cada país.
  
  **Desarrollo Técnico:**
  
  Para la implementación técnica, se han empleado las siguientes herramientas;
  
  -Pydantic para utilizar la clase BaseModel y de esta forma encapsular en este caso la creación de un nuevo billonario (también sirve para filtrar los datos que se quieren meter)
  
  -FastAPI para crear la conexión frontend-backend
  
  -Docker para la creación de contenedores (esto nos permite especificar las versiones de los paquetes necesarios (requirements) independientemente de la versión que tengamos instalada en nuestro ordenador)
  
  -Folium una librería que permite realizar visualizaciones de mapas interactivos
  
  -Geopy (su módulo Nominatim) para obtener las coordenadas de los paises ya que no las tenía el csv.
  
  Todas estas herramientas se han usado para garantizar una eficiente manipulación y transferencia de datos, de tal forma que cada visualización tenga su propia fuente de datos (método get). Por otro lado, la interfaz de usuario ha sido diseñada y construida con Streamlit, proporcionando gráficos interactivos y fácilmente comprensibles con el fin de contrar y transmitir una historia al usuario, que le permita comprender el conjunto de datos.
  
  Uno de los objetivos de este proyecto pretende ser una valiosa y fiable fuente de información para aquellos interesados en explorar y entender la dinámica de la riqueza a nivel mundial, facilitando la identificación de patrones y tendencias significativas entre los mercados y los individuos más ricos del mundo.
  
  **Pasos para ejecutar el Proyecto: Pasos:**
  
  Abrir la cmd y clonar el repositorio con el trabajo: git clone "url del repositorio".
  
  Dirigirse al directorio donde se ha clonado el trabajo y meterse dentro de la carpeta (donde esta el archivo docker compose).
  
  Escribir "dir" en la terminal para ver que están todos los archivos.
  
  Abrir Docker desktop.
  
  Ejecutar docker escribiendo: docker compose up.
  
  Cuando docker se termine de ejecutar ir al navegador web y escribir: http://localhost:8501/
  
  Ya puedes navegar por la página de streamlit.
