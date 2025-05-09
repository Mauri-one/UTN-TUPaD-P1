terminar = True                                                     #Se inicializa la variable con el valor Boolean "True" para poder comenzar el ciclo hasta que su valor cambie a "False" 
while terminar:                                                     #Se inicia la estructura repetitiva "while"
    print("Conversor de Números entre bases numericas!")
    print("1. Decimal a Binario")                                   #Se dan opciones para ejecutar codigo de conversion numerica
    print("2. Binario a Decimal")                                   #Se dan opciones para ejecutar codigo de conversion numerica
    print("3. Terminar")                                            #Se da la opcion para terminar el programa
    opcion = input("Elige una opción: ")                            #Se solicita ingresar un valor y se guarda en la variable "opción"

    if opcion == "1":                                               #Si la variable "opcion" guarda un valor valido se ejecuta el codigo correspondiente al valor elegido
        num = int(input("Ingrese un numero decimal entero: "))      #Se solicita que se ingrese un número decimal y se guarda en la variable "num" como int
        original_num = num                                          #Se guarda el valor original de num en la variable "original_num"
        result = ""                                                 #Se inicializa la variable "result" como un string

        if num == 0:                                                #Usando el operador relacional ==, se compara el valor de la variable "num" con el caracter 0"
           result = 0                                               #Se guarda el valor "0" en la variable "result", dando lugar al ciclo while nuevamente

        else:
            while num > 0:                                          #Se inicia el ciclo while si la variable "num" es mayor a "0"
                resto = num % 2                                     #Se guarda el resultado de la operación num módulo 2 en la variable "resto" 
                num = num // 2                                      #Se realiza la división entera por 2 de la variable "num" y se actualiza en la misma variable
                result = str(resto) + result                        #Se se actualiza la variable "result", con la suma de la variable "resto" como string y de la variable "result"

        result = int(result)                                        #Se cambia el tipo de dato (string) de la variable "result" al tipo de dato int y se guarda en la misma variable
        print(f"El número {original_num} en binario es: {result}")


    elif opcion == "2":                                             #Si la variable "opcion" guarda un valor valido se ejecuta el codigo correspondiente al valor elegido
        binario = input("Ingrese un número binario: ")              #Se solicita que se ingrese un número binario y se guarda en la variable "binario"
        binarioInvertido = binario[::-1]                            #Se utiliza un slicing para invertir el orden de los digitos del numero binario y se guarda en la variable "binarioInvertido"
        suma = 0                                                    #Se inicializa la variable "suma" con el calor  "0"

        if binario == 0:
            suma = 0

        else:
            for i in range(len(binarioInvertido)):                  #Itera sobre cada digito del string "binarioInvertido"
                digito = int(binarioInvertido[i])                   #Convierte cada caracter en la posición de "i" al tipo de dato "entero"
                suma += digito * 2 ** i                             #Calcula el valor decimal del digito actual, realizando; digito multiplicado por 2, elevado a la posición numerica del digito y lo guarda en el acumulador "suma"

        print(f"El número binario {binario} en decimal es: {suma}")


     
    
    #Hola mi nombre es Mauricio Lopez 
    En esta parte del codigo nos encontramos con la sentencia Elif, la cual es antecedida por la condicional if que es el comienzo de la estructura condicional
    como ya se mencionó anteriormente, pertenece a una estructura condicional.
    esta nos permite condicionar el bloque de codigo a ejecutar, aplicando una condicion con la sentencia elif que traducuida significa SI nó sí, esto viene de se cumple tal condicion se ejecuta el 
    codigo siguiente, en este caso 

