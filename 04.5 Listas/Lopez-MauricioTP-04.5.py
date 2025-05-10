
opcion=int(input("Elija un aopcion:  \n1.  Numeros del 1 al 100. \n2.  Mostrar el penultimo elemento de la lista. \n3.  Agregar elemento con .append. \n4.  Reemplazar el segundo y último valor de la lista. \n5.  Explicacion del codigo. \n6.  Lista del 10 al 30 incluidos, saltando de 5 en 5. \n7.  Reemplazar valores centrales. \n8.  Lista de dobles. \n9.  Modificacion de lista. \n10. Lista anidada. \n11.Salir. ")) # Pide un numero entero al usuario

match opcion:

    case 1:

        num=[]                         # Crea una lista vacia
        for i in range(1,101):         # Recorre los numeros del 1 al 100
            if i % 4==0:               # Si el numero es divisible por 4           
                num.append(i)          # Agrega el numero a la lista
        print(num)                     # Imprime la lista de numeros divisibles por 4




    case 2:

        lista = [ "Jesus", "Familia", "Dios es real!!!, buscarlo mientras pueda ser hallado. ", "Conocimiento", "Programacion"]
        print(lista[2])




    case 3:

        lista=[]                                            # Crea una lista vacia
        for i in range(3):                                  # Recorre los numeros del 1 al 3
            lista.append(input("Ingrese un elemento: "))    # Agrega el numero a la lista
        print(lista)                                        # Imprime la lista de numeros divisibles por 4 




    case 4:

        animales = ["perro", "gato", "conejo", "pez"]    # Crea una lista de animales                                                                                                                           
        print(animales)                                  # Imprime la lista de animales
        animales[1]="loro"                               # Cambia el valor del segundo elemento de la lista       
        animales[3]="oso"                                # Cambia el valor del tercer elemento de la lista
        print(animales)                                  # Imprime la lista de animales

    


    case 5:

        """ EL programa muestra una lista de datos del tipo int, con 5 elementos.
            Luego en  la siguiente linea de codigo se hace uso de la funcion ".remove" sobre la lista "numeros".
            Para eliminar el ultimo elmento de la lista. Accediendo a el por medio de "max()"
            Luego se imprime la lista, y se hace uso de la funcion "sum()" para sumar todos los elementos de la lista.
            Finalmente se imprime la lista de numeros"""




    case 6:

        lista=[]
        for i in range(10,31,5):    # Recorre los numeros del 10 al 30 de 5 en 5
            lista.append(i)         # Agrega el numero a la lista 
        print(lista[0:2])           # Imprime los dos primeros elementos de la lista
    



    case 7:

        autos = ["sedan", "polo", "suran", "gol"]       # Crea una lista de autos
        autos[1]= input(" Ingrese el nuevo valor: ")    # Cambia el valor del segundo elemento de la lista
        autos[2]= input(" Ingrese el nuevo valor: ")    # Cambia el valor del tercer elemento de la lista
        print(autos)                                    # Imprime la lista de autos




    case 8:

        dobles=[]              # Crea una lista vacia
        dobles.append(5*2)     # Crea una lista vacia
        dobles.append(10*2)    # Crea una lista vacia
        dobles.append(15*2)    # Recorre los numeros del 1 al 100
        print(dobles)          # Imprime la lista de numeros divisibles por 4
    



    case 9:

        compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]    # Crea una lista de compras
        compras[2].append("jugo")                                              # Agrega un elemento a la lista de compras
        compras[1][1]="tallarines"                                             # Cambia el valor del segundo elemento de la lista
        compras[0].remove("pan")                                               # Elimina el primer elemento de la lista
        print (compras)                                                        # Imprime la lista de compras
    



    case 10:

        lista_anidad=[15, True, [25.5, 57.9, 30.6, ], [False]]    # Crea una lista anidada
        print(lista_anidad)                                       # Imprime la lista anidada
    