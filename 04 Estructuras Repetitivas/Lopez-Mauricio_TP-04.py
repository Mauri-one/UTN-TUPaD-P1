opcion=int(input("Elija un programa a ejecutar: \n1.  Numeros del 1 al 100. \n2.  Cantidad de digitos de un numero entero. \n3.  Suma de enteros con exclusion. \n4.  Suma de secuencias. \n5.  Adivina el numero. \n6.  Imprimir numeros pares comprendidos entre 2 valores. \n7.  Suma de enteros comprendidos entre 2 valores. \n8.  Discirminacion de numeros pares, impares, negativos y positivos. \n9.  Media de valores. \n10. Inversion de numeros. "))


match opcion:
    case 1:
        for i in range (1,101):
            print(i)

    case 2:
        num=input(" Ingrese un numero entero: ")
        digitos=(len(num))
        print (f"Su numero {num} tiene {digitos} digitos")
    
    case 3:
        num1= int(input( "Ingrese un numero entero: "))
        num2= int(input( "Ingrese un numero entero: "))

        suma=0
        for i in range (num1+1,num2):
            suma+=i
        print(f"La suma de los digitos es {suma}")
    
    case 4:
        num= int(input("Ingrese un numero entero o 0 para terminar: "))
        suma=0
        while num!=0:
            suma+=num
            num=int(input("Ingrese un numero entero: "))
        print(f"La suma de los digitos es {suma}")

    case 5: 
        """Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9."""
        import random
        numero_aleatorio = random.randint(0, 9)  # Genera un número aleatorio entre 0 y 9
        intentos = 0

        while True:
            intento = int(input("Adivina el número (entre 0 y 9): "))
            intentos += 1

            if intento < numero_aleatorio:
                print("Demasiado bajo. Intenta de nuevo.")
            elif intento > numero_aleatorio:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Adivinaste el número {numero_aleatorio} en {intentos} intentos.")
                break

    case 6:

        for i in range (100, 0, -1):
            if i % 2 == 0:
                print(i)
            else:
                continue


    case 7:

        num= int(input("ingrese un numero entero positivo: "))
        suma=0
        for i in range (0,num):
            suma+=i
        print(f"La suma de los digitos es {suma}")     

    case 8:
        num = int (input ("Ingrese un numero entero: "))
        pares=0
        impares=0
        positivos=0
        negativos=0
        
        cant_num= int(input("Indique la cantidad de numeros a ingresar: "))
        for i in range (0,cant_num):
            num = int (input ("Ingrese un numero entero: "))
            if num % 2 ==0:
                pares+=1
            else:
                impares+=1

            if num>0:
                positivos+1
            else:
                negativos+1
            print(f"Cantidad de numeros pares: {pares}")
            print(f"Cantidad de numeros impares: {impares}")
            print(f"Cantidad de numeros positivos: {positivos}")
            print(f"Cantidad de numeros negativos: {negativos}")

    case 9:
            
            suma = 0
            cantidad = 100  # Cambie este valor para probar con otra cantidad de números
            
            for i in range(cantidad):
                num = int(input(f"Ingrese el número {i + 1}: "))
                suma += num
            
            media = suma / cantidad
            print(f"La media de los {cantidad} números ingresados es: {media}")
        
    case 10:
        
        num = input("Ingrese un número entero: ")
        num_invertido = num[::-1]  # Invierte el string
        print(f"El número invertido es: {num_invertido}")
        