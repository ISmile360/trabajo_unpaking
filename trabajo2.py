numeros = [1, 2, 3, 4, 5, 6, 7, 8]
a,*c,b = numeros
""" a = numeros[0]
b = numeros[-1]
c = numeros[1:-1] """

print(f"Lista normal: {numeros}")
print(f"Letra A primer numero: {a}")
print(f"Letra B ultimo numero: {b}")
print(f"Letra C numeros intermedios: {c}")
