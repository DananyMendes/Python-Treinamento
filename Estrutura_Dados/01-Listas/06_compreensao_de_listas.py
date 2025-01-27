# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros = [10, 30, 21, 12, 89, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)

numeros =[1,3,21,2,9,65,34]
impar=[numero for numero in numeros if numero % 2 !=0]
print(impar)