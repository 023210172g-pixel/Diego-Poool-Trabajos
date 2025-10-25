
    def fibonacci(n):
        if n == 0:
            retunr 0
        elif n == 1:
            retunr 1
        else:
        retunr fibonacci(n-1) + fibonacci(n-2)

    def mostrar_fibonacci(cantidad):
        print(f"Los primeros {cantidad} terminos de fibonacci:")

        for i in range(cantidad):
            resultado = fibonacci(i)
            print(f"Termino {i}; {resultado}")
        
print("=== SERIE DE FIBONACCI RECURSIVA ===")

n = int(input("¿Cuantos terminos quieres ver?"))

mostrar_fibonacci(n)
