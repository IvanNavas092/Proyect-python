# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 21:20:02 2024

@author: navas
"""

# %% Conexion a base de datos
"""Relacionales --> mysql/ PostgreSQL"""
import mysql.connector
from mysql.connector import Error
import pandas as pd
# Host, database, user, password, port
def connect_BD(host, database, user, password, port):
    try:
        connection = mysql.connector.connect(
            host = host,
            database = database,
            user = user,
            password = password,
            port = port)
        if connection.is_connected():
            print(f"La conexion ha sido existosa!")
            return connection
    except Error as e:
        print(f"Error al conectarse: {e}")
        return None

# Funcion para leer la BD
def read_BD(connection, tabla, columnas, limite_filas):
    try:
        cursor = connection.cursor()
        # Peticion
        columnas_str = ",".join(columnas)
        query = f"SELECT {columnas_str} FROM {tabla} LIMIT {limite_filas};"
        # Ejecutamos la peticion
        cursor.execute(query)
        # Resultados
        resultado = cursor.fetchall()
        # Obtener
        columnas_resultado = [i[0] for i in cursor.description]
        # Nos creamos el DataFrame
        df = pd.DataFrame(resultado, columns = columnas_resultado)
        return df
    except Error as e:
        print(f"Error al leer la BD: {e}")