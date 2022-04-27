from math import *
import mathplotlib.pyplot as plt #Para graficar
class Calculo:
    def __init__(self, n, lista_producto,media,varianza):
        self.n=n
        self.lista_producto=lista_producto
        self.media=media
        self.varianza=varianza
    def Calculos (self):
        suma=0
        lista_opinion= [1,2,3]
        total=0
        lista_producto = [100,200,300]
        for i in range (len(lista_opinion)):
            suma += lista_producto[i]*lista_opinion[i]
        for j in lista_producto:
            total += j
        media = suma/total
        print(media)
        lista_producto2= [100,800,2700]
        suma2=0
        varianza = 0
        for i in range (len(lista_producto2)):
            suma2 += lista_producto2[i]
        varianza = (suma2 - (media)**2)/(total-1)
        print(varianza)
        desviacion_tipica = sqrt(varianza)
        print(desviacion_tipica)
        print(f"\n La media es {media}, la varianza {varianza} y la desviación típica {desviacion_tipica} \n ")

print(Calculo.Calculos('media'))


