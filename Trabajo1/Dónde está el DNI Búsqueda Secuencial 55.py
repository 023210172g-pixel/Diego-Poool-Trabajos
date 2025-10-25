import random

def buscar_dni(lista_dnis, dni_buscado):
    intentos = 0
    for indice, valor in enumerate(lista_dnis):
        intentos += 1
        if valor == dni_buscado:
            return indice, intentos
    return -1, intentos

dnis = [random.randint(10_000_000, 99_999_999) for _ in range(60)]
print("Lista aleatoria de DNIs generada:")
print(dnis)

dni_inexistente = -1
dni_primero = dnis[0]
dni_ultimo = dnis[-1]
dni_medio = dnis[len(dnis) // 2]

print("\n--- Resultados de la búsqueda secuencial ---")
casos_prueba = [dni_inexistente, dni_primero, dni_ultimo, dni_medio]
for dni in casos_prueba:
    posicion, total_intentos = buscar_dni(dnis, dni)
    print(f" Buscando {dni} → Posición encontrada: {posicion}, Comparaciones: {total_intentos}")

print("\n📌 Conclusión:")
print("La búsqueda secuencial es útil para listas pequeñas o desordenadas,")
print("ya que no necesita orden previo y es muy fácil de programar.")