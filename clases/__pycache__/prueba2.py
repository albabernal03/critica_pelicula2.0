
class Calculo:
    def __init__(self, n, lista_producto,media):
        self.n=n
        self.lista_producto=lista_producto
        self.media=media
    def MediaAritmetica (self):
        suma=0
        n= [1,2,3]
        total=0
        lista_producto = [100,200,300]
        for i in range (len(lista_producto)):
            suma += lista_producto[i]
        for j in n:
            total += j
        media = suma/total
        print(media)
print(Calculo.MediaAritmetica('media'))