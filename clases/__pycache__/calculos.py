from math import * #Este módulo proporciona acceso a las funciones matemáticas
import pandas as pd # Libreria para trabajar con dataframes (tablas)
import mathplotlib.pyplot as plt #Para graficar (no se importa bien la librería)

datos= pd.read_csv('/Users/hectorbernaltrujillo/Documents/informática/Programación python/critica_pelicula2.0/critica_peliculas.csv') #Leer el archivo csv

class Calculo:
    def __init__(self, n, lista_producto, media, lista_opiniones, lista_producto2,varianza, intervalo, limite_inferior, limite_superior,desviacion_tipica,amplitud):
        
        self.n=n
        self.lista_producto=lista_producto
        self.media=media
        self.lista_opiniones=lista_opiniones
        self.lista_producto2=lista_producto2
        self.varianza=varianza
        self.intervalo=intervalo
        self.limite_inferior=limite_inferior
        self.limite_superior=limite_superior
        self.desviacion_tipica=desviacion_tipica
        self.amplitud=amplitud

    def grafica_datos_excell():
        #grafica de criticas_peliculas.csv
        lista_votantes=list(datos['Cantidad_votantes(ni)'])
        eje_x = [5,4,3,2,1]
        eje_y = lista_votantes
        plt.bar(eje_x,eje_y, color= 'blue')
        plt.xlabel('Cantidad votantes')
        plt.ylabel('Opiniones(5-0 estrellas)')
        plt.title('Grafica de opiniones de peliculas')
        plt.show()

 
    def Operaciones_estadística(self):
        lista_producto = list(datos['Producto(xi*ni)']) #Seleccionar la columna del producto
        n= list(datos['Cantidad_votantes(ni)']) #Seleccionar la columna de la cantidad de votos
        lista_opiniones = list(datos['Opiniones(xi)']) #Seleccionar la columna de la opinion
        suma_lista_producto=0
        suma_n=0
        for i in range (len(lista_producto)):
            suma_lista_producto += lista_producto[i]* lista_opiniones[i]
        for j in n:
            suma_n += j
        media = suma_lista_producto/suma_n
        #A continuación se calcula la varianza
        lista_producto2 = list(datos['Producto_2(xi^2*ni)']) #Seleccionar la columna del producto_2
        suma_lista_producto2=0
        varianza = 0
        for i in range (len(lista_producto2)):
            suma_lista_producto2 += lista_producto2[i]
        varianza = (suma_lista_producto2 - (media)**2)/(suma_n-1)
        #Calculo de la desviación típica
        desviacion_tipica = sqrt(varianza) #Utilizamos la función sqrt de la librería math para calcular la raíz cuadrada de la varianza
        print(f"\n La media es {media}, la varianza {varianza} y la desviación típica {desviacion_tipica} \n ")
        #SI QUISIESEMOS RESONDEAR LOS VALORES TAN SOLO AÑADIMO ''ROUND'' DELANTE DE LOS VALORES
        #print(f"\n La media es {round(media,2)}, la varianza {round(varianza,2)} y la desviación típica {round(desviacion_tipica,2)} \n ")
    def percentil_68(self):
        #En primer lugar calculamos en que intervalo se encuentra para luego sustituir en la fórmula
        n = list(datos['Cantidad_votantes(ni)']) #Seleccionar la columna de la cantidad de votos
        total = 0
        for i in n:
            total += i
        k = 68
        intervalo = (total*k)/100
        #Ahora calculamos el limite inferior y superior
        limite_inferior = 1 #Datos de la tabla
        limite_superior = 2 #Datos de la tabla
        frecuencia_absoluta_acumulada_anterior = 136 #Datos de la tabla
        frecuencia_relativa_intervalo = 133 #Datos de la tabla
        #Calculamos la amplitud
        amplitud = limite_superior - limite_inferior
        percentil_68 = (limite_inferior + (intervalo-frecuencia_absoluta_acumulada_anterior/ frecuencia_relativa_intervalo))*amplitud
        print(f"\n El percentil 68 es {percentil_68} \n ")
    def percentil_95(self):
        #En primer lugar calculamos en que intervalo se encuentra para luego sustituir en la fórmula
        n = list(datos['Cantidad_votantes(ni)']) 
        total = 0
        for i in n:
            total += i
        k = 95
        intervalo = (total*k)/100
        #Ahora calculamos el limite inferior y superior
        limite_inferior = 3 #Datos de la tabla
        limite_superior = 4 #Datos de la tabla
        frecuencia_absoluta_acumulada_anterior = 414 #Datos de la tabla 
        frecuencia_relativa_intervalo = 99 #Datos de la tabla
        #Calculamos la amplitud
        amplitud = limite_superior - limite_inferior
        percentil_95 = (limite_inferior + (intervalo-frecuencia_absoluta_acumulada_anterior/ frecuencia_relativa_intervalo))*amplitud
        print(f"\n El percentil 95 es {percentil_95} \n ")
    def percentil_97(self):
        #En primer lugar calculamos en que intervalo se encuentra para luego sustituir en la fórmula
        n = list(datos['Cantidad_votantes(ni)']) 
        total = 0
        for i in n:
            total += i
        k = 97
        intervalo = (total*k)/100
        #Ahora calculamos el limite inferior y superior
        limite_inferior = 4 #Datos de la tabla
        limite_superior = 5 #Datos de la tabla
        frecuencia_absoluta_acumulada_anterior = 513
        frecuencia_relativa_intervalo = 40
        #Calculamos la amplitud
        amplitud = limite_superior - limite_inferior
        percentil_97 = (limite_inferior + (intervalo-frecuencia_absoluta_acumulada_anterior/ frecuencia_relativa_intervalo))*amplitud
        print(f"\n El percentil 97 es {percentil_97} \n ")











    
    




        

    
    


