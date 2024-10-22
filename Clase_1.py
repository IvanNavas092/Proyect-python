#%% 1. Cabecera
"""
Autor: Ivan Navas
"""
#%% 2. Importar módulos
import numpy as np
#%% 3. Hola mundo
# print("Hola Mundo")

# nombre = input("Introduce tu nombre: ")
# edad = int(input("Introduce tu edad: "))
# if (edad > 25):
#     print("Hola te llamas",nombre,"y tienes",edad,"lo que significa es que eres un poco viejo")
# else:
#     print("Hola te llamas",nombre,"y tienes",edad,"lo que significa es que eres joven")



#%% 4. Chequeo de errores
# nomrbre = input("Introduce tu nombre: ")
# if nombre.isdigit():
#     print("Error, mete un string")
#     exit()
    
# #verificar numero
# try: edad= int(input("Cual es tu edad: "))
# except ValueError:
#     print("mete un numero!")
#     exit()

    
#%% 5. Tipos de datos
###############################################################################
                    # Variables Inmodificables #
###############################################################################
"""
int,str,tuplas,float,bool
"""
# 4.1 int
# a = 10
# b = 10
# print(id(a),id(b)) #Ubicacion de memoria (MISMO)

# 4.2 str

# 4.3 tuplas
"""

"""
# tupla = (1,2,3,4)
# print(tupla)
# print(tupla[0])
# tupla = tupla + (5,)
# print(tupla) 
"""Imprime la ubicacion de memoria"""
# print(id(tupla))
# #Acceder a los elementos
# E2 = tupla[1]
#Primera funcion
# def calc_suma (a,b):
#     suma = a + b
#     resta = a - b
#     return suma,resta

# resultado = calc_suma(10,5)
# a, b, c, d, e = tupla #te guarda en varibales los valores


        
        
            
    
    

###############################################################################
                    # Variables Modificables #
                    
#4.4 Creacion de listas
# lista = [1, 2, 3, 4]
# E0 = print(lista[0])
#Listas Anidadas
# lista_anidada = [1, 2, 3,  
#                  [4, 5,    
#                   [6, 7]]] 
#[]hay 3 posiciciones (0,1,2) si ponemos 3 entras en la (2 lista), ya estas dentro
#dentro de una eliges la posicion que quieres (0,1), si ponemos uno mas ingresas a la otra
#vuelves a elegir la posicion

# print(lista_anidada[3][2][0])

# lista_anidada.append(1)
# lista_anidada.append([2, 3, 4, 5])

# for elemento in lista_anidada:
#     print(elemento)
#LOS INMUTABLES SIGNIFICAN QUE NO CAMBIAN DE UBICACION DE MEMORIA
######## a pelo
# n_filas1, n_columnas1 = 4, 2
# n_filas2, n_columnas2 = 2, 2
# n_filas3, n_columnas3 = 4, 3
# M = [] #Inicializamos la matriz
# c = 1 #contador

# for i in range (n_filas1):
#     filai1 = []
#     for j in range (n_columnas1):
#         filai1.append(c)
#         c += 1
#     M.append(filai1)

# Forma Bonita
# M = [[0 for _ in range (n_columnas1)]
#      for _ in range(n_filas1)]
# for i in range (n_filas1):
#     for j in range (n_columnas1):
#         M[i][j] = [[0 for _ in range (n_columnas2)] for _ in range(n_filas2)]
#         for ii in range (n_filas2):
#             for jj in range (n_columnas2):
#                 M[i][j][ii][jj] = [[0 for _ in range (n_columnas3)] for _ in range(n_filas3)]
#                 c = 1
#                 for iii in range (n_filas3):
#                     for jjj in range (n_columnas3):
#                         M[i][j][ii][jj][iii][jjj] = c
#                         c +=1
        
# # NUMPY
# Matriz_numpy = np.arange(1, n_filas1 * n_columnas1 + 1) #para crear el vector tenemos que saber el total
# Matriz_numpy = np.reshape(Matriz_numpy, (n_filas1, n_columnas1))


# # Matriz_numpy1 = np.arange(1, n_filas1 * n_columnas1 * n_filas2 * n_columnas2 * n_filas3 * n_columnas3 + 1)
# # Matriz_numpy = np.reshape(
# #     Matriz_numpy, (n_filas1, n_columnas1, n_filas2, n_columnas2, n_filas3, n_columnas3))

# #Diccionarios
# diccionario = {"Nombre":"Sebastian", "Edad": 19, "Estudios": ["ESO", "SMR"]} #tiene un conjunto llamado "estudios"
# # print(diccionario["Edad"])
# # print(diccionario["Estudios"][1]) #SMR
# print(diccionario.get("Estudios")[1]) #SMR
# # diccionario["Gusto"] = "jugar al csgo" #AÑADIR
# # claves = diccionario.keys()
# edad_sebas = diccionario.get("Edad") #te lo saca en variable

# #bdd
# empleados = {
#     "empleado 1" : {"nombre": "Sebastian", "Nota": 2},
#     "empleado 2" : {"nombre": "Ivan", "Nota": 20}}
# print(empleados.values())

# # Conjuntos (se utiliza para cuando debes usar matematicas)
# conjunto1 = {1,2,3}
# conjunto2 = {3,4,5}
# interseccion = conjunto1.intersection(conjunto2) #te saca los numeros en comun
# union = conjunto1.union(conjunto2) #une y quita los repetidos

# booleano = 5 > 3

# """
# 1. Urgente -> Fecha_entrega < 2 y coste > 100
# 1. Prioridad_media -> Fecha_entrega < 2 y coste > 100
# 1. Urgente -> Fecha_entrega < 2 y coste > 100
# """
# fecha_entrega = int(input("Escribe la fecha de manera junta: "))
# c = int(input("costo: "))
# if (fecha_entrega < 2 and c > 100):
#     print("el pedido es urgente")
# elif (fecha_entrega >= 2 and c > 100):
#     print("prioridad media")
# else:
#     print("almacenado")


# %% 6. Condicionales
# x = 20
# if x > 10:
#     print(f" {x} es mayor que 10") #permite poner el valor de x
# elif x == 10:
#     print(f"{x} es igual que 10")
# else:
#     print (f"{x} es menor que 10")
    
# En una sola linea
# x = 4
# print(f"{x} es mayor que 5" if x > 5 else f"{x} es menor que 5")
# Condicionales y listas
# colores = ["rojo", "verde", "azul", "amarillo"]
# color = "rojo"
# if color in colores:
#     print(f"El color {color} esta dentro de la lista {colores}")
# else:
#     print(f"El color {color} no esta dentro de la lista {colores}")
    
# colores = ["rojo", "verde", "azul", "amarillo", "rojo", "rojo"]
# color = "rojo"

# if color in colores:
#     print(f"El color {color} esta dentro de la lista {colores} y se repite {colores.count(color)} veces")
    

# """ Condicionales con diccionario """
# diccionario = {"Sebastian": 11,
#                "daniel": 21,
#                "javier": 19,
#                "Manu": 26,
#                "Ana": 29}
# #  cada persona si es mayor o no
# for persona in diccionario:
#     if diccionario[persona] >= 18:
#         print(f"{persona} es mayor de edad")
#     else:
#         print(f"{persona} no es mayor de edad")
        
# all(and) y any(or)
# x, y, z = 5, 10, 15
# # if all ([x > 0, y > 0, z > 0]):
# #     print("todos son mayores de 0")
# # else: 
# #     print("no todos son mayores de 0")
    
# lista1 = ["rojo", "rojo", "rojo"]
# color = "rojo"

# if any ([x > 0, y > 0, z > 0]):
#      print("todos son mayores de 0")
     
# # %% bucles     
# """ bucles """
# frutas = ['Manzana', 'pera']
# for fruta in frutas:
#     print(f"tu fruta es {fruta}")
    
# diccionario = {'d': 1, 'a': 3, 'Sebastian': 4}
# for clave in diccionario:
#     print(f"{clave}")
    
# for valores in diccionario.values():
#     print(f"tu valor es {valores}")

# diccionario2 = {'sebastian': {'Coche': {'Marca': 'Ferrari', 'kms' : 100000}},
#                 'javier': {'Coche': {'Marca': 'mercedes', 'kms' : 100020}},
#                 'manu': {'Coche': {'Marca': 'seat', 'kms' : 10040}} 
#                 }
# for clave in diccionario2:
#     print(f"{clave} tiene un {diccionario2[clave]['Coche']}")
    
    
# for clave in diccionario2:
#     print(f"la kms del {clave} son {diccionario2[clave]['Coche']['kms']}")
    
    
# n = [1, 2, 3, 4, 5]
# for numero in n:
#     if numero == 4:
#         break
#         #continue
#     print(numero)
    

# lista = [x for x in range (1,6)]
# print(lista)

# diccionario = {x: x**2 for x in range (1, 6)}
# print(diccionario)

# nombres = ["Sebas", "Javier", "Manu"]
# edades = [19, 20, 26]
# for n, e in zip(nombres, edades):
#     print(f"la edad de {n} es {e}")

# for i in range(1, 11, 4): #valor inicial, valor fin, paso (puedes ponerlo en negativo tmb)
#     print(i)

# # %%Funciones
# def nombre():
#     """
#     Descripcion: ............
    
#     Entradas: 
#             -
#             -
#             -
#     Salidas:
#             -
#             -
#             -
#     """
    # Chequeo de errores
    
# def saludar(nombre = None):
#     if nombre is None:
#         print("Hola amigo, no has puesto parametro")
    
# saludar()

# import funciones as f

# a = 1
# b = 16
# print(f.suma(a, b))



# %% variables

# def externa():
#     x = "Externa"
    
#     def interna():
#         nonlocal x #es x de externa() 
#         x = "modificada"
#         print(x)
        
#     interna()
# externa()
    

# %% 7. Extraer y pedir informacion de ficheros, tratarla y devolverla
# 1. Extraer y tratarla
# Modulo pandas --> Leer, tratar, escribir, etc
import pandas as pd
#Leer
# archivo = pd.read_csv("empleados.csv")
# extraer informacion
# Acceder a columnas

# print("los datos de los empleados son: ", archivo)
# print("los nombres son: ", archivo["nombre"])

# Acceder a filas
# primer_empleado = archivo.loc[0] # primer empleado
# Acceder a un valor en concreto
# salario_carlos = archivo.loc[2, "salario_mensual"]

# # 2. Pedir informacion por pantalla y cargarla
# nueva_fila = {
#     "nombre" : "Javier",
#     "edad" : 21,
#     "id_empleado" : "1",
#     "horas_trabajadas" : 20,
#     "tarifa_hora" : 20,
#     "salario_mensual" : None
# }
# # Añadir --> Concat = DataFrame
# nueva_fila = pd.DataFrame([nueva_fila]) #PASAS DEL DICCIONARIO A DATAFRAME
# df = pd.concat([archivo, nueva_fila]) #pd es PANDAS


# # Cargar información
# from tkinter import Tk
# import pandas as pd
# from tkinter.filedialog import askopenfilename

# Tk().withdraw()

# # Pedimos al user que seleccione un archivo .csv
# file_path = askopenfilename(
#     title = "Selecciona un archivo .csv",
#     filetypes = [("CSV files", "*.csv"), ("All files,", "*.*")])

# if file_path:
#     # LEER
#     df = pd.read_csv(file_path) #df = dataFrame
# else:
#     print("No has seleccionado ningun archivo")
    
# 3. Crear un archivo y grabarlo
# Crear diccionario
# import pandas as pd
# import pandas as pd
# from tkinter.filedialog import askdirectory
# import os
# nombre_archivo = "empleados2.csv" #Nombre del fichero que vas a crear
# data = {
#         "nombre" : ["Sebastian", "Javier", "Manu", "Ivan"],
#         "Edad" : [19, 18, 20, 21],
#         "Salario" : [1200, 1900, 1500, 2000]}

# # Convertimos el dataframe
# df = pd.DataFrame(data)
# # Seleccionar carpeta donde quiero guardar
# carpeta_select = askdirectory(title = "Selecciona directorio") #Selecciona donde guardar
# # Verificar seleccion
# if carpeta_select:
#     file_path = os.path.join(carpeta_select, nombre_archivo)
#     # Guardamos DataFrame
#     df.to_csv(file_path, index = False)
# else:
#     print("no has seleccionado nada")

# %% parte de profesor


# %% Conexion a base de datos
# """Relacionales --> mysql/ PostgreSQL"""
# import mysql.connector
# from mysql.connector import Error
# import pandas as pd
# # Host, database, user, password, port
# def connect_BD(host, database, user, password, port):
#     try:
#         connection = mysql.connector.connect(
#             host = host,
#             database = database,
#             user = user,
#             password = password,
#             port = port)
#         if connection.is_connected():
#             print(f"La conexion ha sido existosa!")
#             return connection
#     except Error as e:
#         print(f"Error al conectarse: {e}")
#         return None

# # Funcion para leer la BD
# def read_BD(connection, tabla, columnas, limite_filas):
#     try:
#         cursor = connection.cursor()
#         # Peticion
#         columnas_str = ",".join(columnas)
#         query = f"SELECT {columnas_str} FROM {tabla} LIMIT {limite_filas};"
#         # Ejecutamos la peticion
#         cursor.execute(query)
#         # Resultados
#         resultado = cursor.fetchall()
#         # Obtener
#         columnas_resultado = [i[0] for i in cursor.description]
#         # Nos creamos el DataFrame
#         df = pd.DataFrame(resultado, columns = columnas_resultado)
#         return df
#     except Error as e:
#         print(f"Error al leer la BD: {e}")
        

# if __name__ == "__main__":
#     # Parametros de conexion
#     host = "mysql-rfam-public.ebi.ac.uk"
#     database = "Rfam"
#     user = "rfamro"
#     password = " "
#     port = 4497
#     # Parametros de consulta
#     tabla = "family"
#     # Columnas que quieres extraer
#     columnas = ["rfam_acc", "rfam_id", "description"]
#     limite_filas = 5 #numero de filas que quieres extraer
#     # Conectar a la BD
#     conexion = connect_BD(host, database, user, password, port)
#     if conexion:
#         # Leer
#         df_BD = read_BD(conexion, tabla, columnas, limite_filas)
#         if df_BD is not None:
#             print(df_BD)
#         conexion.close()
        
# if __name__ == "__main__":
#     # Parametros de conexion
#     host = "mysql-rfam-public.ebi.ac.uk"
#     database = "Rfam"
#     user = "rfamro"
#     password = " "
#     port = 4497
#     # Parametros de consulta
#     tabla = "family"
#     # Columnas que quieres extraer
#     columnas = ["rfam_acc", "rfam_id", "description"]
#     limite_filas = 5 #numero de filas que quieres extraer
#     # Conectar a la BD
#     conexion = connect_BD(host, database, user, password, port)
#     if conexion:
#         # Leer
#         df_BD = read_BD(conexion, tabla, columnas, limite_filas)
#         if df_BD is not None:
#             print(df_BD)
#         conexion.close()
        
        
# %% Consumo y creacion de APIs
# import requests
# # url
# url = "https://pokeapi.co/api/v2/pokemon2?"

# # Respuesta
# respuesta = requests.get(url)
# lista_pokemon = respuesta.json()["Results"]
# for pokemon in lista_pokemon:
#     print(pokemon["name"])
    
    
# """ NO RELACIONALES --> MONGODB"""
# # Importar módulos
# import pymongo
# import pandas as pd

# # Conexion

 
# try:
#     cliente = pymongo.MongoClient(
#         "mongodb+srv://navas:<navas>@cluster0.abnap.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#     print("conexion existosa!")
# except Exception as e:
#     print(f"algo ha fallado!, Error: {e}")
#     exit() #Importante salirse cuando falla
    
# # Extraer información (campo a campo)
# db = cliente["sample_mflix"]
# coleccion = db["movies"]    
# # Hacer la consulta
# try:    
#     resultados = coleccion.find().limit(10)
#     lista_resultados = list(resultados)
#     # Verificar si se han extraido los resultados
#     if not lista_resultados:
#         print(f"no se han encontrado datos")
#     else:
#         print(f"se han encontrado {len(lista_resultados)} documentos")
#         df = pd.DataFrame(lista_resultados)
# except Exception as e:
#     print(f"error al realizar la consulta {e}")
    


# """Creacion de APIs"""
# # PVGIS
# import requests
# import json
# # Url
# url = "https://re.jrc.ec.europa.eu/api/v5_2/PVcalc"

# # Parametros
# params = {
#     "lat": 38.6759,
#     "lon": -4.159,
#     "peakpower": 1,
#     "pvtechchoice": "crystSi",
#     "loss": 14,
#     "outputformat": "json"}

# # Realizar consulta
# respuesta = requests.get(url,params = params)

# data = json.loads(respuesta.text)

# print(f"la energia diria estimada es: {data['outputs']['totals']['fixed']}")
    



"""Creacion de APIs ahora si"""
from flask import Flask, jsonify

app = Flask(__name__)

# Lista 1
@app.route("/api/lista1", methods = ["GET"])

def obtener_lista1():
    datos = {
        "nombre": "Sebastian",
        "edad": 19,
        "Residencia": "Seseña"}
    return jsonify(datos)

# Lista 2
@app.route("/api/lista2", methods = ["GET"])

def obtener_lista2():
    lista_datos = [
        {"nombre": "Sebastian", "edad": 19, "Residencia": "Seseña"},
        {"nombre": "Javier", "edad": 12, "Residencia": "Valdemoro"},
        {"nombre": "Tymur", "edad": 9, "Residencia": "Ecuador"}]
    return jsonify(lista_datos) #Te convierte en Json

if __name__ == "__main__":
    app.run(debug = True)
    
    
       

    
        




###############################################################################
