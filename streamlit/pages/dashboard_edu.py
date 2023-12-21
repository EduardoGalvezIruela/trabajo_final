import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import requests
import plotly.express as px
import folium
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim

#--------------------------------------------------------------------------------------------------------------(Información general top 1)

st.set_page_config(page_title='Visualizaciones', layout='wide',     page_icon="📊")

# Meter rectangulos con información
def cargar_datostop1(url:str):
    '''Con esta función importamos los datos necesarios del backend para la realizar la visualización 1.'''
    r = requests.get(url)
    if r.status_code != 200:
        print(f'Error en la solicitud: {r.status_code}')
    else:
        print('Requests realizada correctamente')
        data = r.json()
        dataf=pd.DataFrame.from_records(data)
        return dataf
df_top1 = cargar_datostop1('http://fastapi:8000/gettop1')

# Muestra la información en cajas (boxes) individuales

sns.set_palette("pastel")

st.header("Información general de Billonario Top 1")

col1, col2, col3 = st.columns(3)

col4, col5, col6 = st.columns(3)
with col1:
    st.subheader('Nombre')
    st.info(df_top1.iloc[0, 0])
with col2:
    st.subheader('Patrimonio')
    st.info(df_top1.iloc[0, 1])
with col3:
    st.subheader('Ciudad')
    st.info(df_top1.iloc[0, 2])

with col4:
    st.subheader('País')
    st.info(df_top1.iloc[0, 3])

with col5:
    st.subheader('Empresa')
    st.info(df_top1.iloc[0, 4])
with col6:
    st.subheader('Origen')
    st.info(df_top1.iloc[0, 5])

#--------------------------------------------------------------------------------------------------------------(Visualización 1)
#   ORDENAR FINALWORTH DE MAYOR A MENOR PARA QUE QUEDE MÁS VISUAL
def cargar_datos1(url:str):
    '''Con esta función importamos los datos necesarios del backend para la realizar la visualización 1.'''
    r = requests.get(url)
    if r.status_code != 200:
        print(f'Error en la solicitud: {r.status_code}')
    else:
        print('Requests realizada correctamente')
        data = r.json()
        dataf=pd.DataFrame.from_records(data)
        return dataf

df = cargar_datos1('http://fastapi:8000/get1')

# Calcular el total de 'finalWorth' por cada 'category'
df = df.groupby('category')['finalWorth'].sum().reset_index()

st.title('Visualización 1: Riqueza por Sector')

categoriasunicas=df["category"].unique() # FALTA VARIABLE 'Sports'
# Opcional: Puedes agregar controles interactivos, por ejemplo, un filtro por categoría
categorias_unicas = ["Todas"] + list(df["category"].unique())
categoria_seleccionada = st.selectbox('Selecciona una categoría:', categorias_unicas)

# Filtrar el DataFrame según la categoría seleccionada
if categoria_seleccionada == 'Todas':
    df_filtrado = df
else:
    df_filtrado = df[df['category'] == categoria_seleccionada]
# st.dataframe(df_filtrado)

# Botones para ordenar el gráfico
col1, col2 = st.columns(2)
with col1:
    ordenar_ascendente = st.button('Ordenar ascendente')

with col2:
    ordenar_descendente = st.button('Ordenar descendente')

# Verificar el estado de los botones y ordenar el DataFrame
if ordenar_ascendente:
    df_filtrado = df_filtrado.sort_values(by='finalWorth', ascending=True)
elif ordenar_descendente:
    df_filtrado = df_filtrado.sort_values(by='finalWorth', ascending=False)

# Visualización: Distribución de la riqueza por sector
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='finalWorth', y='category', data=df_filtrado, errorbar=None, ax=ax)
plt.title(f'Distribución de la Riqueza para la categoría {categoria_seleccionada}')
st.pyplot(fig)

#--------------------------------------------------------------------------------------------------------------(Visualización 2)

def cargar_datos2(url:str):
    '''Con esta función importamos los datos necesarios del backend para la realizar la visualización 2.'''
    r = requests.get(url)
    if r.status_code != 200:
        print(f'Error en la solicitud: {r.status_code}')
    else:
        print('Requests realizada correctamente')
        data = r.json()
        dataf=pd.DataFrame.from_records(data)
        return dataf

df_selfmade_inherited = cargar_datos2('http://fastapi:8000/get2')

st.title('Visualización 2: Comparación de Self-Made vs. Inherited por Sexo')

# Filtro interactivo por sexo
sexo_seleccionado = st.selectbox('Selecciona un sexo:', ['Todos', 'Male', 'Female'])

# Filtrar el DataFrame según el sexo seleccionado
if sexo_seleccionado == 'Todos':
    df_filtrado = df_selfmade_inherited
else:
    df_filtrado = df_selfmade_inherited[df_selfmade_inherited['gender'].apply(lambda x: 'Male' if x == 'M' else 'Female') == sexo_seleccionado]

# Agrupar por 'selfMade', 'gender' y contar el número de ocurrencias
df_agrupado = df_filtrado.groupby(['selfMade', 'gender']).size().reset_index(name='count')

# Verificar si hay datos en el DataFrame antes de continuar
if not df_agrupado.empty:
    # Visualización: Comparación de Self-Made vs. Inherited por Sexo
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x='selfMade', y='count', hue='gender', data=df_agrupado, errorbar=None, ax=ax)

    # Configurar etiquetas y leyenda
    plt.title('Comparación de Self-Made vs. Inherited por Sexo')
    plt.xlabel('Origen de la Riqueza')
    plt.ylabel('Cantidad')
    plt.xticks([0, 1], ['Inherited', 'Self-Made'])

    # Configurar información al pasar el cursor
    for p in ax.patches:
        total = p.get_height()
        ax.annotate(f'{total}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center')

    # Mostrar la visualización en Streamlit
    st.pyplot(fig)
else:
    st.warning('No hay datos disponibles para la visualización.')

#--------------------------------------------------------------------------------------------------------------(Visualización 3)

def cargar_datos3(url:str):
    '''Con esta función importamos los datos necesarios del backend para la realizar la visualización 3.'''
    r = requests.get(url)
    if r.status_code != 200:
        print(f'Error en la solicitud: {r.status_code}')
    else:
        print('Requests realizada correctamente')
        data = r.json()
        dataf=pd.DataFrame.from_records(data)
        return dataf

df_edad_sector = cargar_datos3('http://fastapi:8000/get3')

# Calcular la edad promedio por sector
edad_promedio_sector = df_edad_sector.groupby('category')['age'].mean().reset_index()

# Ordenar el DataFrame por edad promedio de manera ascendente
edad_promedio_sector = edad_promedio_sector.sort_values(by='age')

# Título de la aplicación
st.title('Visualización 3: Edad Promedio por Sector')

# Filtro interactivo para establecer edades mínima y máxima
edad_minima = st.slider('Edad Promedio Mínima', int(df_edad_sector['age'].min()), int(df_edad_sector['age'].max()), int(df_edad_sector['age'].min()))
edad_maxima = st.slider('Edad Promedio Máxima', int(df_edad_sector['age'].min()), int(df_edad_sector['age'].max()), int(df_edad_sector['age'].max()))

# Filtrar el DataFrame según las edades seleccionadas
edad_promedio_sector_filtrado = edad_promedio_sector[(edad_promedio_sector['age'] >= edad_minima) & (edad_promedio_sector['age'] <= edad_maxima)]

# Crear el gráfico de barras interactivo con Plotly Express
fig = px.bar(edad_promedio_sector_filtrado, 
             x='category', 
             y='age',
             title=f'Edad Promedio por Sector ({edad_minima} - {edad_maxima} años)',
             labels={'age': 'Edad Promedio', 'category': 'Sector'},
             color='age')

# Configurar el diseño del gráfico
fig.update_layout(xaxis_title='Sector', yaxis_title='Edad Promedio', coloraxis_colorbar=dict(title='Edad Promedio'))

# Mostrar la visualización en Streamlit
st.plotly_chart(fig)
#--------------------------------------------------------------------------------------------------------------(Visualización 4)

def cargar_datos4(url:str):
    '''Con esta función importamos los datos necesarios del backend para la realizar la visualización 3.'''
    r = requests.get(url)
    if r.status_code != 200:
        print(f'Error en la solicitud: {r.status_code}')
    else:
        print('Requests realizada correctamente')
        data = r.json()
        dataf=pd.DataFrame.from_records(data)
        return dataf

df_country_city = cargar_datos4('http://fastapi:8000/get4')

st.title('Visualización 4: Top 10 de Países/Ciudades por Riqueza Total')

# Crear un filtro para seleccionar entre 'Top 10 ciudades' y 'Top 10 paises'
tipo_filtro = st.selectbox('Selecciona el tipo de filtro', ['Top 10 ciudades', 'Top 10 paises'])

# Definir las columnas a mostrar en la tabla según el tipo de filtro
columnas_mostrar = ['city', 'finalWorth'] if tipo_filtro == 'Top 10 ciudades' else ['country', 'finalWorth']

# Obtener el top 10 según la columna seleccionada
top_10 = df_country_city.groupby(columnas_mostrar[0])['finalWorth'].sum().reset_index().nlargest(10, 'finalWorth')

# Mostrar la tabla
st.table(top_10)

#--------------------------------------------------------------------------------------------------------------(Visualización 5)

# Meter mapa con folium probar a coger pocos datos para uqe funcione. Coger solo los paises más top

def cargar_datos5(url:str):
    '''Con esta función importamos los datos necesarios del backend para la realizar la visualización 3.'''
    r = requests.get(url)
    if r.status_code != 200:
        print(f'Error en la solicitud: {r.status_code}')
    else:
        print('Requests realizada correctamente')
        data = r.json()
        dataf=pd.DataFrame.from_records(data)
        return dataf

df_map = cargar_datos5('http://fastapi:8000/get5')

st.title('Visualización 5: Mapa Interactivo')
st.write("⚠️ Por favor, espere a que cargue el mapa, esto puede tardar varios segundos.")
st.write("⚠️ En caso de error, por favor recargue al página (es posible que lo tengas que realizar varias veces por problemas de la librería).")
st.write("Haz click en los puntos del mapa para obtener más información acerca del pais seleccionado.")

# Sumar finalWorth por pais
df_grouped = df_map.groupby('country', as_index=False)['finalWorth'].sum()
df_grouped = df_grouped.drop(0)# Quitamos paises NULL

# Crear un mapa centrado en una ubicación inicial
m = folium.Map(location=[25, 0], zoom_start=2)

# Diccionario para corregir coordenadas de algunos paises
coordinates = {
    'Russia': [61.5240, 105.3188],
    'China': [35.8617, 104.1954],
    'Egypt': [26.8206, 30.8025],
    'Israel': [31.0461, 34.8516],
    'Hungary': [47.1625, 19.5033],
    'Lebanon': [33.8547, 35.8623],
    'Sweden': [60.1282, 18.6435],
    'Greece': [39.0742, 21.8243],
    'Germany' : [51.1657, 10.4515],
    'Georgia' : [42.3154, 43.3569]
}

# Función para obtener las coordenadas de un país
def get_country_location(country_name):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.geocode(country_name)
    
    # Verificar si se encontró la ubicación
    if country_name not in coordinates:
        return [location.latitude, location.longitude]
    elif country_name in coordinates:
        return coordinates[country_name]
    else:
        print(f"No se encontraron coordenadas para {country_name}")
        return None

# Agregar marcadores al mapa
for index, row in df_grouped.iterrows():
    country_name = row['country']
    final_worth = row['finalWorth']

    # Obtener las coordenadas del país
    location = get_country_location(country_name)
    
    # Verificar si se encontraron las coordenadas
    if location:
        # Crear un marcador para cada país
        folium.Marker(
            location=location,
            popup=f'{country_name}<br>Final Worth: {final_worth} M',
            tooltip=country_name
        ).add_to(m)
    else:
        print(f"No se agregó el marcador para {country_name} porque no se encontró su ubicación")

# Mostrar el mapa en Streamlit
folium_static(m)