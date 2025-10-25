
def burbuja_numeros(lista):
    numeros = lista.copy()
    n = len(numeros)

    print(f"Lista inicial: {lista}")

    for i in range(n):
        for j in range(n - i - 1):
            if numeros[j] > numeros[j + 1]:
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
                print(f"intercambio: {numeros}")
    
    return numeros

# Programa principal  
lista = [5, 3, 8, 4, 2]
resultado = burbuja_numeros(lista)
print(f"Resultado: {resultado}")
