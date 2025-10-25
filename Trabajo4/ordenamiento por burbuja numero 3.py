def burbuja(lista):
    total = len(lista)
    intercambios = 0
    for i in range(total - 1):
        for j in range(total - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambios += 1
    return lista

numeros = []

activo = True

while activo:
    print("\nSeleccione una opción:")
    print("1. Agregar número a la lista")
    print("2. Ordenar la lista")
    print("0. Salir del programa")

    try:
        opcion = int(input("Ingrese su elección: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    if opcion == 1:
        try:
            nuevo_numero = int(input("Ingrese un número: "))
            numeros.append(nuevo_numero)
            print("Lista actual:", numeros)
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")
    elif opcion == 2:
        if numeros:
            print("Lista original:", numeros)
            lista_ordenada = burbuja(numeros.copy())  
            print("Lista ordenada:", lista_ordenada)
        else:
            print("La lista está vacía. No hay nada que ordenar.")
    elif opcion == 0:
        activo = False
        print("Programa finalizado.")
    else:
        print("Opción no válida. Intente con 0, 1 o 2.")
