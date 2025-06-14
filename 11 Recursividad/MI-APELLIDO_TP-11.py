"""Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario"""



def factorial(n):                                                                       # se define la función recursiva para calcular el factorial
    if n == 0 or n == 1:                                                                # caso base: si n es 0 o 1, el factorial es 1
        return 1                                                                        # Return cumple la función de devolver el valor 1, es una variable que se usa para el caso base
    return n * factorial(n - 1)                                                         # caso contrario a la condicion anterior, recursivamente se multiplica n por el factorial de n-1

# Solicitar al usuario un número entero
num = int(input("Ingresa un número entero positivo: "))                                 # se solicita al usuario un número entero positivo

# Validación para asegurarse de que el número sea positivo
if num < 1:
    print("Por favor, ingresa un número entero positivo mayor o igual a 1.")
else:
    # Calcular y mostrar los factoriales desde 1 hasta num
    for i in range(1, num + 1):                                                         # se itera desde 1 hasta el número ingresado por el usuario
        print(f"Factorial de {i}: {factorial(i)}")                                      # se imprime el factorial de cada número en el rango

