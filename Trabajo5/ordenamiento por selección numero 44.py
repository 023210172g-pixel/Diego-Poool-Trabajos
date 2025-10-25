import random

obj = [random.randint(1, 50) for _ in range(10)]
print("obj original:", obj)

def seleccion(obj):
    n = len(obj)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if obj[j] < obj[min_idx]:
                min_idx = j
        obj[i], obj[min_idx] = obj[min_idx], obj[i]
    return obj

def busqueda_binaria(obj, val):
    ini = 0
    fin = len(obj) - 1
    while ini <= fin:
        mid = (ini + fin) // 2
        if obj[mid] == val:
            return mid     
        elif obj[mid] < val:
            ini = mid + 1
        else:
            fin = mid - 1
    return -1  

seleccion(obj)  
print("obj ordenado:", obj)

val = random.choice(obj)
pos = busqueda_binaria(obj, val)
print("Buscando", val, "-> posición:", pos)

val2 = 999
pos2 = busqueda_binaria(obj, val2)
print("Buscando", val2, "-> posición:", pos2)  

 
