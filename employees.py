import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


st.title('Employees app')
st.header('App de employees. Reto módulo 5.')
st.write('En esta aplicación se trabajará con el archivo employees.csv')
DATE_COLUMN = 'released'
DATA_URL = ('Employees.csv')

import codecs
#Functions to be called
@st.cache
def load_data(nrows):
    doc = codecs.open(DATA_URL,'rU','latin1')
    employeeData = pd.read_csv(doc, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return employeeData

@st.cache
def filter_data_by_id(id):
    filtered_data_id = employeeData[employeeData['Employee_ID'].str.upper().str.contains(id)]
    return filtered_data_id

@st.cache
def filter_data_by_hometown(hometown):
    filtered_data_hometown = employeeData[employeeData['Hometown'].str.upper().str.contains(hometown)]
    return filtered_data_hometown

@st.cache
def filter_data_by_unit(unit):
    filtered_data_unit = employeeData[employeeData['Unit'].str.upper().str.contains(unit)]
    return filtered_data_unit

@st.cache
def filter_data_by_educationLevel(educationLevel):
    filtered_data_educationLevel = employeeData[employeeData['Education_Level'] == educationLevel]
    return filtered_data_educationLevel

@st.cache
def filter_data_by_SelectedHometown(selectedHometown):
    filtered_data_by_SelectedHometown = employeeData[employeeData['Hometown'] == selectedHometown]
    return filtered_data_by_SelectedHometown

# Load all registers
data_load_state = st.text('Loading cicle nyc data...')
employeeData = load_data(1000)
data_load_state.text("Done! (using st.cache)")

if st.sidebar.checkbox('Mostrar todos los registros'):
    st.subheader('Todos los registros')
    st.write(employeeData)

# Filter by ID
idEmpleado = st.sidebar.text_input('ID del empleado :')
btnBuscar_id = st.sidebar.button('Buscar empleado por ID')

if (btnBuscar_id):
   data_id = filter_data_by_id(idEmpleado.upper())
   count_row = data_id.shape[0]  # Gives number of rows
   st.write(f"Total empleados mostrados tras busqueda de id : {count_row}")
   st.write(data_id)

# Filter by Hometown
hometownEmpleado = st.sidebar.text_input('Hometown del empleado :')
btnBuscar_hometown = st.sidebar.button('Buscar empleado por Hometown')

if (btnBuscar_hometown):
   data_hometown = filter_data_by_hometown(hometownEmpleado.upper())
   count_row = data_hometown.shape[0]  # Gives number of rows
   st.write(f"Total empleados correspondientes a la busqueda de hometown : {count_row}")
   st.write(data_hometown)

# Filter by Unit
unitEmpleado = st.sidebar.text_input('Unit del empleado :')
btnBuscar_unit = st.sidebar.button('Buscar empleado por Unit')

if (btnBuscar_unit):
   data_unit = filter_data_by_unit(unitEmpleado.upper())
   count_row = data_unit.shape[0]  # Gives number of rows
   st.write(f"Total empleados correspondientes a la busqueda de unidad : {count_row}")
   st.write(data_unit)

# Filter by selected education level
selected_educationLevel = st.sidebar.selectbox("Seleccionar nivel educativo", employeeData['Education_Level'].unique())
btnFilterbyeducationLevel = st.sidebar.button('Filtrar nivel educativo ')

if (btnFilterbyeducationLevel):
   filterbyeducationLevel = filter_data_by_educationLevel(selected_educationLevel)
   count_row = filterbyeducationLevel.shape[0]  # Gives number of rows
   st.write(f"Total empleados con este nivel educativo : {count_row}")
   st.dataframe(filterbyeducationLevel)

# Filter by selected hometown
selected_hometown = st.sidebar.selectbox("Seleccionar hometown", employeeData['Hometown'].unique())
btnFilterbySelectedHometown = st.sidebar.button('Filtrar hometown seleccionado ')

if (btnFilterbySelectedHometown):
   filterbySelectedHometown = filter_data_by_SelectedHometown(selected_hometown)
   count_row = filterbySelectedHometown.shape[0]  # Gives number of rows
   st.write(f"Total empleados de la ciudad seleccionada : {count_row}")
   st.dataframe(filterbySelectedHometown)

# Histogram by age
fig, ax = plt.subplots()
ax.hist(employeeData["Age"])
st.header("Histograma de los empleados por edad")
st.pyplot(fig)

#Countplot de empleados x unidad
fig3, axs3 = plt.subplots()
axs3 = sns.countplot(x=employeeData["Unit"], orient="h")
axs3.tick_params(axis='x', rotation=90)
st.header("Countplot de empleados x unidad")
st.pyplot(fig3)

employees_by_hometown = employeeData.dropna().groupby("Hometown").mean()

# Graficas de attrition por hometown
fig4, axs4 = plt.subplots()
axs4 = sns.lineplot(data = employees_by_hometown, x="Hometown", y="Attrition_rate")
st.header("Attrition rate by hometown")
st.pyplot(fig4)

#Scatterplot de empleados edad x taza de decersión
fig2, axs2 = plt.subplots()
axs2 = plt.scatter(employeeData['Age'],employeeData['Attrition_rate'])
st.header("Scatterplot de empleados edad x taza de decersión")
st.pyplot(fig2)

#Scatterplot de empleados edad x taza de decersión
fig5, axs5 = plt.subplots()
axs5 = plt.scatter(employeeData['Time_of_service'],employeeData['Attrition_rate'])
st.header("Scatterplot de empleados tiempo de servicio x taza de decersión")
st.pyplot(fig5)