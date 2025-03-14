"""  lista = [1,2,3,4,5]
#impresion de una lista de manera normal
print(lista)
#impresion de una lista mediante el uso desempaquetado
print(*lista)
print(*lista,sep="-")


lista2 = [6,7,8]
lista3 = [*lista,*lista2,9,10]
print(lista3) """

diccionario = {"dato1":1,"dato2":10}
print(diccionario)
diccionario2 = {"dato3":30,"dato4":50}
print(diccionario2)
diccionario3 = {**diccionario, **diccionario2}
print(diccionario3)
diccionario4 = diccionario2 * 2
print(diccionario4) 

lista4=[10,12,100,20]
lista5 = [*lista4]
lista5.append(200)
print(f"Lista4: {id(lista4)} contenido:{lista4}")
print(f"Lista5: {id(lista5)} contenido:{lista5}")


def multiples(**datos):
    print(datos)
    
multiples(**diccionario) 

#