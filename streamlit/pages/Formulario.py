import streamlit as st
import requests
import pandas as pd



def add_billionaire_form():
    st.header("Rellena al menos los campos obligatorios, señalados por '*'.")
    st.write("Aviso: El billonario que agreges se añaderá en la primera fila del csv.")

    # Definir campos del formulario con valor predeterminado None
    rank = st.number_input("Ranking", value=0)
    finalWorth = st.number_input("Patrimonio *", value=0.0)
    category = st.text_input("Categoría", value=0, key="category")
    personName = st.text_input("Nombre *", value=None, key="personName")
    age = st.number_input("Edad *", value=0)
    country = st.text_input("País", value=None, key="country")
    city = st.text_input("Ciudad", value=None, key="catecitygory")
    source = st.text_input("Fuente", value=None, key="source")
    industries = st.text_input("Industrias", value=None, key="industries")
    countryOfCitizenship = st.text_input("País de Ciudadanía", value=None, key="countryOfCitizenship")
    organization = st.text_input("Organización", value=None, key="organization")
    selfMade = st.checkbox("Autogenerado")
    status = st.text_input("Estado", value=None, key="status")
    gender = st.text_input("Género", value=None, key="gender")
    birthDate = st.text_input("Fecha de Nacimiento", value=None, key="birthDate")
    lastName = st.text_input("Apellido", value=None, key="lastName")
    firstName = st.text_input("Primer Nombre", value=None, key="firstName")
    title = st.text_input("Título", value=None, key="title")
    date = st.text_input("Fecha", value=None, key="date")
    state = st.text_input("Estado", value=None, key="state")
    residenceStateRegion = st.text_input("Región de Residencia", value=None, key="residenceStateRegion")
    birthYear = st.number_input("Año de Nacimiento", value=0)
    birthMonth = st.number_input("Mes de Nacimiento", value=0)
    birthDay = st.number_input("Día de Nacimiento", value=0)
    cpi_country = st.number_input("CPI País", value=0)
    cpi_change_country = st.number_input("Cambio CPI País", value=0)
    gdp_country = st.number_input("GDP País", value=0)
    gross_tertiary_education_enrollment = st.number_input("Matrícula Educación Terciaria", value=0)
    gross_primary_education_enrollment_country = st.number_input("Matrícula Educación Primaria", value=0)
    life_expectancy_country = st.number_input("Expectativa de Vida País", value=0)
    tax_revenue_country_country = st.number_input("Ingresos Fiscales País", value=0)
    total_tax_rate_country = st.number_input("Tasa de Impuestos País", value=0)
    population_country = st.number_input("Población País", value=0)
    latitude_country = st.number_input("Latitud País", value=0)
    longitude_country = st.number_input("Longitud País", value=0)

    # Botón para enviar el formulario
    if st.button("Agregar"):
        # Crear el diccionario con los datos del nuevo billonario
        new_billionaire = {
            'rank': rank,
            'finalWorth': finalWorth,
            'category': category,
            'personName': personName,
            'age': age,
            'country': country,
            'city': city,
            'source': source,
            'industries': industries,
            'countryOfCitizenship': countryOfCitizenship,
            'organization': organization,
            'selfMade': selfMade,
            'status': status,
            'gender': gender,
            'birthDate': birthDate,
            'lastName': lastName,
            'firstName': firstName,
            'title': title,
            'date': date,
            'state': state,
            'residenceStateRegion': residenceStateRegion,
            'birthYear': birthYear,
            'birthMonth': birthMonth,
            'birthDay': birthDay,
            'cpi_country': cpi_country,
            'cpi_change_country': cpi_change_country,
            'gdp_country': gdp_country,
            'gross_tertiary_education_enrollment': gross_tertiary_education_enrollment,
            'gross_primary_education_enrollment_country': gross_primary_education_enrollment_country,
            'life_expectancy_country': life_expectancy_country,
            'tax_revenue_country_country': tax_revenue_country_country,
            'total_tax_rate_country': total_tax_rate_country,
            'population_country': population_country,
            'latitude_country': latitude_country,
            'longitude_country': longitude_country
        }

        # Enviar la solicitud POST al backend
        response = requests.post("http://fastapi:8000/Subir_nuevo_billonario", json=new_billionaire)

        dataf= requests.get("http://fastapi:8000/obtener_nuevo_df")
        data = dataf.json()
        dataf=pd.DataFrame(data)
        st.write("Vista previa del archivo:")
        st.dataframe(dataf)
        if st.download_button(label="Dowload CSV",data=dataf.to_csv().encode('utf-8'), key="download_button", mime="text/csv"):
            st.success("Archivo descargado correctamente")
        

# Página principal de Streamlit
def main():
    st.title("Agregar Nuevo Billonario")
    # Mostrar el formulario para agregar un nuevo billonario
    add_billionaire_form()

if __name__ == "__main__":
    main()
        
