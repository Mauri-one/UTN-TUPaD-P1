

"""Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal."""

#Funcion para imprimir "Hola Mundo!"
def imprimir_hola_mundo():
    print("Hola Mundo!")


#########################################################################################################




"""Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), 
deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario."""

#Funcion para saludar al usuario
def saludar_usuario(nombre):
    return f"Hola {nombre}!"


#########################################################################################################




""" Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
Pedir los datos al usuario y llamar a esta función con los valores ingresados."""

#funfion para imprimir la información personal

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


#########################################################################################################




"""Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro
 y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio 
 como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y 
 llamar ambas funciones para mostrar los resultados."""


# Función para calcular el área de un círculo
import math
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio


#########################################################################################################




"""Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y 
mostrar el resultado usando esta función."""

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas


#########################################################################################################




"""Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función."""

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


#########################################################################################################




"""Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos, 
restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara."""

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinido"  # Evita división por cero
    return suma, resta, multiplicacion, division


##########################################################################################################




"""Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
 para mostrar el resultado con dos decimales."""    

#FUncvion calcular imc
def calcular_imc(peso, altura):
    return round(peso / (altura ** 2), 2)


#########################################################################################################



"""Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función."""

#Funcion para convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32


#########################################################################################################




""".Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
"""
# Funcion para calcular el promedio de tres números
def calcular_promedio(a, b, c):
    return (a + b + c) / 3


##########################################################################################################


### Programa principal ###

if __name__ == "__main__":
    imprimir_hola_mundo()

    nombre = input("Ingrese su nombre: ")
    print(saludar_usuario(nombre))

    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    residencia = input("Ingrese su lugar de residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)

    radio = float(input("Ingrese el radio del círculo: "))
    print(f"Área: {calcular_area_circulo(radio)}, Perímetro: {calcular_perimetro_circulo(radio)}")

    segundos = int(input("Ingrese la cantidad de segundos: "))
    print(f"Equivalente en horas: {segundos_a_horas(segundos)}")

    numero = int(input("Ingrese un número para la tabla de multiplicar: "))
    tabla_multiplicar(numero)



    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))

    resultados = operaciones_basicas(a, b)
    print(f"Suma: {resultados[0]}")
    print(f"Resta: {resultados[1]}")
    print(f"Multiplicación: {resultados[2]}")
    print(f"División: {resultados[3]}")




    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    print(f"IMC: {calcular_imc(peso, altura)}")

    celsius = float(input("Ingrese la temperatura en Celsius: "))
    print(f"Equivalente en Fahrenheit: {celsius_a_fahrenheit(celsius)}")

    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
    print(f"Promedio: {calcular_promedio(a, b, c)}")


