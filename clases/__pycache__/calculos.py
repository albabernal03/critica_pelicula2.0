from math import * #Este módulo proporciona acceso a las funciones matemáticas
import pandas as pd # Libreria para trabajar con dataframes (tablas)
import mathplotlib.pyplot as plt #Para graficar

datos= pd.read_csv('/Users/hectorbernaltrujillo/Documents/informática/Programación python/critica_pelicula2.0/critica_peliculas.csv') #Leer el archivo csv

class Calculo:
    def __init__(self, n, lista_producto, media):
        self.n=n
        self.lista_producto=lista_producto
        self.media=media
    def MediaAritmetica (self):
        lista_producto = list(datos['Producto(xi*ni)']) #Seleccionar la columna del producto
        n= list(datos['Cantidad_votos(ni)']) #Seleccionar la columna de la cantidad de votos
        suma_lista_producto=0
        suma_n=0
        for i in range (len(lista_producto)):
            suma_lista_producto += lista_producto[i]
        for j in n:
            suma_n += j
        media = suma_lista_producto/suma_n
        print(media)
print(Calculo.MediaAritmetica('media'))
