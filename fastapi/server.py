from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from typing import Any , List
import pandas as pd
import streamlit as st
from pydantic import BaseModel as PydanticBaseModel

class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True


class Billionaire(BaseModel):
    rank : int
    finalWorth : float
    category : str
    personName :str
    age : int
    country : str
    city : str
    source : str
    industries : str
    countryOfCitizenship : str
    organization : str
    selfMade : bool
    status : str
    gender : str
    birthDate : str
    lastName : str
    firstName : str
    title : str
    date : str
    state : str
    residenceStateRegion : str
    birthYear : int
    birthMonth : int
    birthDay : int
    cpi_country : float
    cpi_change_country : float
    gdp_country : float
    gross_tertiary_education_enrollment : float
    gross_primary_education_enrollment_country : float
    life_expectancy_country : float
    tax_revenue_country_country : float
    total_tax_rate_country : float
    population_country : float
    latitude_country : float
    longitude_country : float


class ListadoBillonaire(BaseModel):
    billonario = List[Billionaire]

app = FastAPI(
    title="Servidor de datos (top billonarios)",
    description="""Este servidor da acceso a una base de datos que contiene una tabla con el ranking
      de billonarios, además información adicional de cada uno de ellos""", version="0.1.0",)

# Load CSV data into a DataFrame
csv_file = "Dataset/Billionaires_Statistics_Dataset.csv"
data = pd.read_csv(csv_file)



# CODIGO QUE FUNCIONA
@app.get("/gettop1/")
def get_top1_info():
    '''Método get que selecciona los datos de la información general del billonario top 1'''
    # Select relevant columns from the DataFrame
    selected_columns = ["personName", "finalWorth","city","country","source","selfMade"]
    df = data[selected_columns]
    top1 = df.iloc[0]
    # # Convertir el DataFrame a una lista de diccionarios
    top1 = top1.fillna(0)
    todosmisdatosdict = top1.to_dict()
    # Create a list containing the dictionary
    # list_of_billionaires = [todosmisdatosdict]
    listado = ListadoBillonaire()
    listado.billonario = todosmisdatosdict
    lista_top1=[listado.billonario]
    return lista_top1

@app.get("/get1/")
def get_vis1_info():
    '''Método get que recoge la información para realizar la visualización 1'''
    # Select relevant columns from the DataFrame
    selected_columns = ["finalWorth", "category"]
    df = data[selected_columns]
    # Convertir el DataFrame a una lista de diccionarios
    df = df.fillna(0)
    todosmisdatosdict = df.to_dict(orient="records")
    listado = ListadoBillonaire()
    listado.billonario = todosmisdatosdict
    return listado.billonario

@app.get("/get2/")
def get_vis2_info():
    '''Método get que recoge la información para realizar la visualización 2'''
    # Select relevant columns from the DataFrame
    selected_columns = ["selfMade", "gender"]
    df = data[selected_columns]
    df["selfMade"] = df["selfMade"].astype(int)
    # Convertir el DataFrame a una lista de diccionarios
    df = df.fillna(0)
    todosmisdatosdict = df.to_dict(orient="records")
    listado = ListadoBillonaire()
    listado.billonario = todosmisdatosdict
    return listado.billonario

@app.get("/get3/")
def get_vis3_info():
    '''Método get que recoge la información para realizar la visualización 3'''
    # Select relevant columns from the DataFrame
    selected_columns = ["category", "age"]
    df = data[selected_columns]
    # Convertir el DataFrame a una lista de diccionarios
    df = df.fillna(0)
    todosmisdatosdict = df.to_dict(orient="records")
    listado = ListadoBillonaire()
    listado.billonario = todosmisdatosdict
    return listado.billonario

@app.get("/get4/")
def get_vis4_info():
    '''Método get que recoge la información para realizar la visualización 4'''
    # Select relevant columns from the DataFrame
    selected_columns = ["country","city", "finalWorth"]
    df = data[selected_columns]
    # Convertir el DataFrame a una lista de diccionarios
    df = df.fillna(0)
    df = df[(df["city"] != 0) & (df["country"] != 0)] # Para eliminar los paises y ciudades NULL
    todosmisdatosdict = df.to_dict(orient='records')
    listado = ListadoBillonaire()
    listado.billonario = todosmisdatosdict
    return listado.billonario

@app.get("/get5/")
def get_vis5_info():
    '''Método get que recoge la información para realizar el mapa interactivo'''
    # Select relevant columns from the DataFrame
    selected_columns = ["country", "finalWorth"]
    df = data[selected_columns]
    # Convertir el DataFrame a una lista de diccionarios
    df = df.fillna(0)
    todosmisdatosdict = df.to_dict(orient="records")
    listado = ListadoBillonaire()
    listado.billonario = todosmisdatosdict
    return listado.billonario


#----------------------------------------------------------------------------------------(POST)
# Variable para almacenar los datos
data_cambio = pd.DataFrame()

@app.post("/Subir_nuevo_billonario/")
def add_billionaire(billionaire: Billionaire):
    
    try:
        # Leer el JSON desde el archivo
        billionaire = billionaire.dict()
        
        # Convertir el diccionario a un dataframe
        new_data = pd.DataFrame([billionaire])

        # Concatenar el nuevo DataFrame con el existente
        global data
        nuevo_df = pd.concat([new_data,data], ignore_index=True)
        nuevo_df = nuevo_df.fillna('')
        nuevo_df.to_csv("Dataset/nuevo_df", index=False)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar el archivo: {str(e)}")
    
@app.get("/obtener_nuevo_df")
def get_nuevo_df():
    if "Dataset/nuevo_df":
        new_df=pd.read_csv("Dataset/nuevo_df")
        new_df = new_df.fillna('')
        todosmisdatosdict = new_df.to_dict()
        return todosmisdatosdict
    else:
        print("Error: No se ha encontrado el archivo 'nuevo_df'")