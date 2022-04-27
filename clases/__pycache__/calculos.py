from math import * #Este módulo proporciona acceso a las funciones matemáticas
import pandas as pd # Libreria para trabajar con dataframes (tablas)
import mathplotlib.pyplot as plt #Para graficar

datos= pd.read_csv('/Users/hectorbernaltrujillo/Documents/informática/Programación python/critica_pelicula2.0/critica_peliculas.csv') #Leer el archivo csv

class Calculo:
    def __init__(self, n, lista_producto):
        self.n=n
        self.lista_producto=lista_producto
    def MediaAritmetica (self):
        suma=0
        for i in range(self.n):
            suma=suma+self.lista_producto[i]
        return suma/self.n