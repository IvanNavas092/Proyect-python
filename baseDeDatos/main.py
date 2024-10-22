# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 21:26:38 2024

@author: navas
"""
from conectar_BD import connect_BD, read_BD

if __name__ == "__main__":
    # Parametros de conexion
    host = "mysql-rfam-public.ebi.ac.uk"
    database = "Rfam"
    user = "rfamro"
    password = " "
    port = 4497
    # Parametros de consulta
    tabla = "family"
    # Columnas que quieres extraer
    columnas = ["rfam_acc", "rfam_id", "description"]
    limite_filas = 5 #numero de filas que quieres extraer
    # Conectar a la BD
    conexion = connect_BD(host, database, user, password, port)
    if conexion:
        # Leer
        df_BD = read_BD(conexion, tabla, columnas, limite_filas)
        if df_BD is not None:
            print(df_BD)
        conexion.close()