# Funcion para convertir un numero de DNI a lista

def convertir_dni_a_lista(numero):                          # Crea la funcion para convertir un número de DNI en una lista de dígitos
    lista_de_digitos = [int(digito) for digito in cadena]   # Convierte cada carácter de la cadena a un entero 
    return lista_de_digitos                                 # Devuelve la lista de dígitos del DNI



# Funcion para obtener los dígitos únicos de una lista

def obtener_unicos(lista):                                  # Crea la funcion obtener los dígitos únicos de una lista
    unicos = []                                             # Lista para almacenar los dígitos únicos del DNI
    for item in lista:                                      # Itera cada elemento de la lista
        if item not in unicos:                              # Si el elemento no está en la lista de únicos, lo agrega
            unicos.append(item)                             # Añade el elemento que no esta en la lista de unicos a la lista de únicos
    return unicos                                           # Devuelve la lista de dígitos únicos del DNI



# Funcion para obtener los dígitos únicos de una lista

def union_listas(lista_de_listas):                          # Crea la funcion para unir varias listas y obtener los elementos únicos
    resultado = []                                          # Lista para almacenar el resultado de la unión de listas
    for lista in lista_de_listas:                           # Itera cada "lista" en "lista de listas"
        for item in lista:                                  # Itera cada "item" en la "lista"
            if item not in resultado:                       # Si el "item" no está en el resultado, lo agrega
                resultado.append(item)                      # Añade el elemento que no esta en la lista de resultado a la lista de resultado
    return resultado                                        # Devuelve la lista de elementos únicos de todas las listas unidas



# Funciones para realizar operaciones con listas de números de DNI

def interseccion_listas(lista_de_listas):                   # Crea la funcion para encontrar la intersección de varias listas
    if not lista_de_listas:                                 # Si la lista de listas está vacía, retorna una lista vacía
        return []                                           # Retorna una lista vacía si no hay listas para intersectar
    resultado = []                                          # Lista para almacenar el resultado de la intersección
    for item in lista_de_listas[0]:                         # Toma el primer elemento de la primera lista como base para la intersección
        en_todas = True                                     # Variable para verificar si el "item" está en todas las listas
        for lista in lista_de_listas[1:]:                   # Itera sobre las listas restantes
            if item not in lista:                           # Verifica si el "item" está en la lista actual
                en_todas = False                            # Si no está en alguna lista, cambia la variable a False
        if en_todas and item not in resultado:              # Si el "item" está en todas las listas y no está en el resultado, lo agrega
            resultado.append(item)                          # Añade el elemento que esta en todas las listas a la lista de resultado
    return resultado                                        # Devuelve la lista de elementos que están en todas las listas



#Funcion para identificar la diferencia entre listas

def diferencia(lista1, listas_restantes):                   # Crea la funcio para calcular la diferencia entre una lista y varias listas restantes
    resultado = []                                          # Lista para almacenar el resultado de la diferencia
    for item in lista1:                                     # Itera cada "item" en la primera lista
        esta = False                                        # Variable para verificar si el "item" está en alguna de las listas restantes
        for lista in listas_restantes:                      # Itera "lista" in "listas restantes"
            if item in lista:                               # Si el "item" está en alguna de las listas restantes, cambia la variable a True
                esta = True
        if not esta:                                        # Si el "item" no está en ninguna de las listas restantes, lo agrega al resultado
            resultado.append(item)
    return resultado                                        # Devuelve la lista de elementos que están en la primera lista pero no en las listas restantes



#Funcion para indentificar la diferencia simétrica entre listas

def diferencia_simetrica_dos_listas(lista1, lista2):        # Crea la funcio para calcular la diferencia simétrica entre listas
    resultado = []                                          # Lista para almacenar el resultado de la diferencia simétrica
    for item in lista1:                                     # Itera cada "item" en la primera lista
        if item not in lista2 and item not in resultado:    # Si El "item" no esta en la lista2 y tampoco en resultado, lo agrega
            resultado.append(item)                          # Añade el elemento evaluado anteriormente a la lista "resultado"
    for item in lista2:                                     # Itera cada "item" en la segunda lista
        if item not in lista1 and item not in resultado:    # Evalua si el item no esta en lista1 y tampoco en resultado, y lo agrega a la lista "resultado"
            resultado.append(item)
    return resultado                                        # Devuelve la lista de elementos que están en una lista o en otra, pero no en ambas



# Funcion para Contar la frecuencia de cada digito de un DNI

def contar_frecuencia_digitos(dnis):                        # Crea la funcion para contar la frecuencia de cada dígito en una lista de DNIs
    frecuencia = {}                                         # Diccionario para almacenar la frecuencia de cada dígito del 0 al 9
    for i in (dnis):                                        # Itera cada "i" en la lista de DNIs
        frecuencia[i] = frecuencia.get(i, 0) + 1            # Actualiza la frecuencia del dígito "i" en el diccionario, si no existe lo inicializa en 0 y le suma 1
    return frecuencia                                       # Devuelve el diccionario con la frecuencia de cada dígito en el DNI



# Funcion para sumar los digitos de un DNI

def sumar_digitos_dni(dni):                                 # Crea la funcion para sumar los dígitos de un DNI
    return sum(int(digito) for digito in str(dni))          # Convierte el DNI a cadena, itera sobre cada dígito, lo convierte a entero y suma todos los dígitos  


def diversidad_numerica (conjunto):  
    for i in range (5):
        if len(conjunto[i])>=5:
                print(f"En el conjunto {unicos_list[i]}, hay diversidad numérica")
        else:
                print(f"En el conjunto {unicos_list[i]}, no hay diversidad numérica")
    return conjunto

def elemento_comun(lista):
    if not lista:
        return set()

    # Convertir la primera sublista en un conjunto inicial
    comunes = set(lista[0])

    # Intersectar con cada sublista restante
    for sublista in lista[1:]:
        comunes &= set(sublista)

    return comunes

def grupo_par(lista):
    pares = 0
    impares = 0
    for i in range(5):
        for i in range(len(lista[i])):
            if i % 2 == 0:
                pares += 1
            else:
                impares += 1
    if pares > impares:
        return ("Grupo par")
    elif pares < impares:
        return ("Grupo impar")
    else:
        return("Misma cantidad de pares e impares")

def procesar_fechas():
    años_lista = []
    edad_lista = []
    contador_par = 0
    grup_z = 0
    for n in range(5):                                                                                                            # La operación se desarrolla con una iteración de 5 ya que somos 5 integrantes.
        años = int(input("Ingrese un año de nacimiento: "))                                                                                                                            # Se ingresan los años de nacimiento de los integrantes una vez por ciclo.
        print(f"Año: {años}")
        años_lista.append(años)
        edad = 2025 - años
        edad_lista.append(edad)                                                                                                   # Se calcula una edad aproximada con la fecha de nacimiento ingresada (no toma en concideración los meses)
        if (años % 2) == 0: contador_par += 1                                                                                     # Se calcula la suma de los años que son pares, y en base a eso tambén podemos conseguir los años impares.
        if (años >= 2000): grup_z += 1                                                                                            # Se suman los años que cumplan la condicion si son mayores o iguales al año 2000, y se guarda en la variable grupo_z.
        if ((años % 4 == 0 and años % 100 != 0) or (años % 400 == 0)): print("Tenemos un año especial.")                          # Distingue si algun año ingresado es Bisiesto. De haber uno se imprime un mensaje indicándolo.
    
    print(f"Los años ingresados son: {años_lista}")                                                                               # Se imprimen los años que están guardados en la lista "años".
    if grup_z == 5: print("Grupo Z.")                                                                                             # Se comprueba si el contador grup_z cumple la condición de tener valor 5. Indicando que todos los integrantes nacieron en el año 2000, o posteriormente.
    
    print(f"Las edades en orden son: {edad_lista}")                                                                               # Se imprimen las edades.
    print(f"Hubo {contador_par} miembros que nacieron en año par, y {5 - contador_par} que nacieron en año impar.")               # Se imprime la cantidad de miembros que nacieron en un año par e impar respectivamente.
    
    print("Producto Cartesiano entre años y edades")                                                                              # Se imprimen un mensaje para dar seguimiento a la operación de cartesianos.
    print([(x, y) for x in años_lista for y in edad_lista])                                                                       # Se define y se imprime el producto cartesiano entre las edades y las fechas de nacimiento.



################################################################################################################################################################


# Cuerpo del programa para manejar operaciones con números de DNI 

dnis = []                                                   # Lista para almacenar los números de DNI ingresados
unicos_list = []                                            # Lista para almacenar los dígitos únicos de cada DNI
nombres = ['A', 'B', 'C', 'D', 'E']                         # Lista de nombres para identificar cada DNI
dnis_cadena = []                                            # Lista para almacenar los números de DNI como cadenas


for i in range(5):                                          # Itera 5 veces para solicitar 5 números de DNI
    cadena = input("Ingrese su número de DNI: ")            # Solicita al usuario que ingrese un número de DNI
    dnis_cadena.append(cadena)                              # Añade el número de DNI ingresado a la lista de DNIs como cadena
    dni = convertir_dni_a_lista("")                         # Convierte el número de DNI ingresado a una lista de dígitos
    unicos = obtener_unicos(dni)                            # Obtiene los dígitos únicos de la lista de dígitos del DNI
    print(f"DNI {nombres[i]}: {dni}")                       # Imprime el número de DNI convertido a lista
    print(f"Dígitos únicos ({nombres[i]}): {unicos}")       # Imprime los dígitos únicos del DNI
    dnis.append(dni)                                        # Añade el número de DNI convertido a lista a la lista de DNIs 
    unicos_list.append(unicos)                              # Añade los dígitos únicos del DNI a la lista de dígitos únicos




print("\nOperaciones de conjuntos:")                                                       # Imprime el encabezado para las operaciones de conjuntos
union_total = union_listas(unicos_list)                                                    # Lista para almacenar la unión de todas las listas de dígitos únicos           
print(f"Unión: A ∪ B ∪ C ∪ D ∪ E = {union_total}")                                        #Imprime la Union total de lso digitos unicos de los DNIs

interseccion_total = interseccion_listas(unicos_list)                                      # Lista para almacenar la intersección de todas las listas de dígitos únicos
print(f"Intersección: A ∩ B ∩ C ∩ D ∩ E = {interseccion_total}")                           # Imprime la Intersección total de los digitos unicos de los DNIs

diferencia_a = diferencia(unicos_list[0], unicos_list[1:])                                 # Calcula la diferencia entre el primer DNI y los demás                               
print(f"Diferencia: A - B - C - D - E = {diferencia_a}")                                   # Imprime la diferencia entre el primer DNI y los demás

print(f"A - B = {diferencia(unicos_list[0], [unicos_list[1]])}")                           # Imprime la diferencia de ls dígitos únicos entre el primer y segundo DNI
print(f"B - C = {diferencia(unicos_list[1], [unicos_list[2]])}")                           # Imprime la diferencia de ls dígitos únicos entre el segundo y tercer DNI
print(f"C - D = {diferencia(unicos_list[2], [unicos_list[3]])}")                           # Imprime la diferencia de ls dígitos únicos entre el tercer y cuarto DNI
print(f"D - E = {diferencia(unicos_list[3], [unicos_list[4]])}")


print("\nDiferencia Simétrica entre pares:")
for i in range(len(unicos_list) - 1):
    resultado_par = diferencia_simetrica_dos_listas(unicos_list[i], unicos_list[i+1])
    print(f"{nombres[i]} Δ {nombres[i+1]} = {resultado_par}")

resultado_total = unicos_list[0]
for i in range(1, len(unicos_list)):
    resultado_total = diferencia_simetrica_dos_listas(resultado_total, unicos_list[i])

print(f"\nDiferencia Simétrica Total: A Δ B Δ C Δ D Δ E = {resultado_total}")




resultado1 = contar_frecuencia_digitos(dnis_cadena[0])  
resultado2 = contar_frecuencia_digitos(dnis_cadena[1])  
resultado3 = contar_frecuencia_digitos(dnis_cadena[2])  
resultado4 = contar_frecuencia_digitos(dnis_cadena[3])  
resultado5 = contar_frecuencia_digitos(dnis_cadena[4])  


print(f"Frecuencia de cada dígito en el DNI: {dnis_cadena[0]}")
for i, cantidad in resultado1.items():
    print(f"{i}: {cantidad}")
print(f"Frecuencia de cada dígito en el DNI: {dnis_cadena[1]}")
for i, cantidad in resultado2.items():
    print(f"{i}: {cantidad}")
print(f"Frecuencia de cada dígito en el DNI: {dnis_cadena[2]}")
for i, cantidad in resultado3.items():
    print(f"{i}: {cantidad}")
print(f"Frecuencia de cada dígito en el DNI: {dnis_cadena[3]}")
for i, cantidad in resultado4.items():
    print(f"{i}: {cantidad}")
print(f"Frecuencia de cada dígito en el DNI: {dnis_cadena[4]}")
for i, cantidad in resultado5.items():
    print(f"{i}: {cantidad}")


for i in range(5):
    suma_digitos = sumar_digitos_dni(dnis_cadena[i])

    print(f"DNI {nombres[i]}: {dnis_cadena[i]}")
    print(f"Suma de los dígitos: {suma_digitos}")


diversidad_numerica(unicos_list)

print(f"Dentro de los dni ingresados de los ingresantes, encontramos un Dígito en Común: {elemento_comun(unicos_list)}")
print (f"De acuerdo a la cantidad de elementos pares e impares podemos decir que se trata de un {grupo_par(unicos_list)}")

print("A continuación le pediremos a los integrantes que ingresen sus años de nacimiento.")    
procesar_fechas()