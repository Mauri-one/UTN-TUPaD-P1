opcion=int(input("Elija un programa a ejecutar: \n1.  Numeros del 1 al 100. \n2.  Cantidad de digitos de un numero entero. \n3.  Suma de enteros con exclusion. \n4.  Suma de secuencias. \n5.  Adivina el numero. \n6.  Imprimir numeros pares comprendidos entre 2 valores. \n7.  Suma de enteros comprendidos entre 2 valores. \n8.  Discirminacion de numeros pares, impares, negativos y positivos. \n9.  Media de valores. \n10. Inversion de numeros. "))


match opcion:
    case 1:
        for i in range (1,101):                                               # Imprime los numeros del 1 al 100
            print(i)



    case 2:
        num=input(" Ingrese un numero entero: ")                              # Pide un numero entero al usuario
        digitos=(len(num))                                                    # Cuenta la cantidad de digitos del numero ingresado
        print (f"Su numero {num} tiene {digitos} digitos")                    # Imprime la cantidad de digitos del numero ingresado                               
    



    case 3:
        
        num1= int(input( "Ingrese un numero entero: ")) 
        num2= int(input( "Ingrese un numero entero mayor al anterior: "))

        suma=0                                                                # Variable para sumar los numeros
        for i in range (num1+1,num2):                                         # Se suman los numeros comprendidos entre los dos valores
            suma+=i
        print(f"La suma de los digitos es {suma}")                            # Imprime la suma de los numeros comprendidos entre los dos valores ingresados
    



    case 4:
        num= int(input("Ingrese un numero entero o 0 para terminar: "))       # Pide un numero entero al usuario
        suma=0                                                                # Variable para sumar los numeros                                               
        while num!=0:                                                         # Mientras el numero ingresado sea diferente de 0, se suman los numeros
            suma+=num
            num=int(input("Ingrese un numero entero: "))                      # Pide un numero entero al usuario   
        print(f"La suma de los digitos es {suma}")                            # Imprime la suma de los numeros ingresados cuendo el usuario ingrese 0




    case 5: 
        
        import random                                                         # Importa la libreria random para generar numeros aleatorios
        numero_aleatorio = random.randint(0, 9)                               # Genera un número aleatorio entre 0 y 9
        intentos = 0                                                          # Inicializa el contador de intentos

        while True:                                                           # Bucle infinito para permitir múltiples intentos
            intento = int(input("Adivina el número (entre 0 y 9): "))         # Pide al usuario que adivine el número
            intentos += 1                                                     # Incrementa el contador de intentos
            if intento < numero_aleatorio:                                    # Compara el intento con el número aleatorio
                print("Demasiado bajo. Intenta de nuevo.")                    # Informa al usuario si el intento es demasiado bajo
            elif intento > numero_aleatorio:                                  # Compara el intento con el número aleatorio
                print("Demasiado alto. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Adivinaste el número {numero_aleatorio} en {intentos} intentos.") # Informa al usuario si adivinó el número
                break                                                                                   # Sale del bucle si el usuario adivina el número




    case 6:

        for i in range (100, 0, -1):                                         # Imprime los numeros del 100 al 1 
            if i % 2 == 0:                                                   # Si el numero es par, lo imprime
                print(i)                                                     # Imprime el numero par
            else:                                                            # Si el numero es impar, no lo imprime    
                continue                                                     # Continua con el siguiente numero


    case 7:

        num= int(input("ingrese un numero entero positivo: "))               # Pide un numero entero al usuario
        suma=0                                                               # Variable para sumar los numeros 
        for i in range (0,num):                                              # Se suman los numeros
            suma+=i
        print(f"La suma de los digitos es {suma}")                           # Imprime la suma de los numeros ingresados                                                     

    case 8:
        num = int (input ("Ingrese un numero entero: "))                     # Pide un numero entero al usuario
        while num != 0:                                                      # Mientras el numero ingresado sea diferente de 0, se suman los numeros
            num = int (input ("Ingrese un numero entero: "))                 # Pide un numero entero al usuario
            if num % 2 ==0:                                                  # Si el numero es par, lo imprime
                pares+=1
            else:                                                            # Si el numero es impar, no lo imprime
                impares+=1
            if num>0:                                                        # Si el numero es positivo, lo imprime
                positivos+1
            else:                                                            # Si el numero es negativo, no lo imprime
                negativos+1
        pares=0
        impares=0
        positivos=0
        negativos=0
        
        cant_num= int(input("Indique la cantidad de numeros a ingresar: ")) # Pide un numero entero al usuario
        for i in range (0,cant_num):                                        # Se suman los numeros 
            num = int (input ("Ingrese un numero entero: "))                # Pide un numero entero al usuario
            if num == 0:                                                    # Si el numero es 0, se termina el programa
            if num % 2 ==0:                                                 # Si el numero es par, lo imprime
                pares+=1                                
            else:                                                           # Si el numero es impar, no lo imprime
                impares+=1

            if num>0:                                                       # Si el numero es positivo, lo imprime
                positivos+1
            else:                                                           # Si el numero es negativo, no lo imprime
                negativos+1
            print(f"Cantidad de numeros pares: {pares}")
            print(f"Cantidad de numeros impares: {impares}")
            print(f"Cantidad de numeros positivos: {positivos}")
            print(f"Cantidad de numeros negativos: {negativos}")

    case 9:
            
            suma = 0
            cantidad = 100                                                  # Cambie este valor para probar con otra cantidad de números
            
            for i in range(cantidad):                                       # Recorre la cantidad de números a ingresar
                num = int(input(f"Ingrese el número {i + 1}: "))
                suma += num
            
            media = suma / cantidad                                         # Calcula la media
            print(f"La media de los {cantidad} números ingresados es: {media}") 
        
    case 10:
        
        num = input("Ingrese un número entero: ")                     # Pide un número entero al usuario
        num_invertido = num[::-1]                                     # Invierte el string
        print(f"El número invertido es: {num_invertido}")             # Imprime el número invertido
        