
opcion =input("Elija un Ejercicio para ejecutar: ")


match opcion:
    case "1": 
        """ 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
               deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”."""
                
        edad=int (input("Igrese su edad: "))
        if edad >= 18:
            print("Es mayor de edad")



match opcion :
     case "2":
        """2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
              mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
              mensaje “Desaprobado”."""

        nota=float(input("Ingrese su nota:"))
        if nota >= 6:
             print("Aprobado")
                 
        else: 
            print("Desaprobado")



match opcion:
     case "3":
        """ 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
               número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
               contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
               operador de módulo (%) en Python para evaluar si un número es par o impar. """

        numero= int(input("Ingrese un numero: "))
                 
        while numero %2 !=0:
             print ("Por favor ingrese un numero par")
             numero= int (input( "Ingrese un numero: "))
        else:
             print ("Ha ingresado un numero par")



match opcion:
    case "4":
        """4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
              siguientes categorías pertenece: 
                ● Niño/a: menor de 12 años. 
                ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
                ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
                ● Adulto/a: mayor o igual que 30 años. """
        
        edad=int (input("Ingrese su edad: "))
        if edad<12:
            print(" Niño/a")
        elif 12<= edad < 18:
            print ("Adolescente")
        elif 18<= edad < 30:
            print ("Adulto/a joven")
        else:
            print("Adulto/a")



match opcion:
    case "5":
        """5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
              (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
              pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
              pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
              de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
              como una lista o un string. """
        
        contraseña=input("Ingrese su contraseña: ")
        longitud=len(contraseña) # evalua la longitud de la contraseña
        while  longitud <8 or longitud >14:
            print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
            contraseña=input("Ingrese su contraseña: ")
            longitud=len(contraseña)
        if 8<= longitud <=14:
            print("Ha ingresado una contraseña correcta")



match opcion:
    case "6":
        """6) El paquete statistics de python contiene funciones que permiten tomar una lista de números 
              y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el 
              siguiente: 
              from statistics import mode, median, mean 
              mi_lista = [1,2,5,5,3] 
              mean(mi_lista) 

              En la documentación oficial se puede encontrar más información sobre este paquete: 
              https://docs.python.org/es/3.8/library/statistics.html.  
              La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se 
              pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio: 
                  ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la 
                    mediana es mayor que la moda. 
                  ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, 
                    la mediana es menor que la moda. 
                  ● Sin sesgo: cuando la media, la mediana y la moda son iguales. 

              Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista 
              numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
              hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 

              Definir la lista numeros_aleatorios de la siguiente forma: 
              import random 
              numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 

                Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de 
                      forma aleatoria."""
        
        import random # GENERA NUMEROS ALEATORIOS
        from statistics import mode, median, mean # IMPORTA LA LIBRERIA DE ESTADISTICA
        numeros_aleatorios = [random.randint(1,100) for i in range(50)] # GENERA UNA LISTTA CON 50 NUMEROS ENTRE 1 Y 100 ELEGIDOS DE FORMA ALEATORIA
        media=mean(numeros_aleatorios)
        mediana=median(numeros_aleatorios)
        moda=mode(numeros_aleatorios)

        sesgo_positivo=media>mediana>moda
        sesgo_negativo=media<mediana<moda
        sin_sesgo=media==mediana==moda

        if sesgo_positivo:
            print("Sesgo positivo")
        elif sesgo_negativo:
            print("Sesgo negativo")
        elif sin_sesgo:
            print("Sin sesgo")
        else:
            print("No se puede determinar el sesgo")



match opcion:
    case "7":
        """7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
              termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
              pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
              pantalla."""

        frase=str(input("Ingrese una palabra o frase: "))
        exclamacion="!"
        frase_termina_con_vocal=f" {frase}{exclamacion}" # CONCATENA LA FRASE CON UN SIGNO DE EXCLAMACION
        vocales=["a","e","i","o","u","A","E","I","O","U"] # LISTA DE VOCALES EN MAYUSCULA Y MINUSCULA
        ultimo_caracter=frase[-1] # EL INDICE -1 DEVUELVE EL ULTIMO CARACTER DE LA FRASE
       
        if ultimo_caracter in vocales: # SI EL ULTIMO CARACTER DE LA FRASE ES UNA VOCAL
            print(frase_termina_con_vocal)
        else:
            print (frase)



match opcion:
    case "8":
        """8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
              dependiendo de la opción que desee: 
                    1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
                    2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
                    3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.

              El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
              usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
              lower() y title() de Python para convertir entre mayúsculas y minúsculas."""

        nombre=input("Ingrese su nombre: ")
        opcion=input("Elija una opción: \n 1) Si quiere su nombre en mayúsculas. \n 2) Si quiere su nombre en minúsculas. \n 3) Si quiere su nombre con la primera letra mayúscula \n")
        mayuculas=nombre.upper() # cambia la variable a mayusculas
        minusculas=nombre.lower() # cambia la variable a minusculas  
        primera_letra_mayuscula=nombre.title() # primera letra mayuscula
        match opcion: # opcion elegida por el usuario
            case "1":
                print(mayuculas)
            case "2":
                print(minusculas)
            case "3":
                print(primera_letra_mayuscula)



match opcion:
    case "9":
        """Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
           magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
           por pantalla: 
                ● Menor que 3: "Muy leve" (imperceptible). 
                ● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
                ● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
                  generalmente no causa daños). 
                ● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
                  débiles). 
                ● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
                ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). """

        magnitud_terremoto=float(input("Ingrese la magnitud del terremoto: "))
        if magnitud_terremoto < 3:
            print(" Muy leve" + "(Imperceptible).")
        elif 3 <= magnitud_terremoto < 4:
            print("Leve" + "(Ligeramente perceptible).")
        elif 4 <= magnitud_terremoto < 5:
            print("Moderado" + "(Sentido por personas, pero generalmente no causa daños)")
        elif 5 <= magnitud_terremoto < 6:
            print("Fuerte" + "(Puede causar daños en estructuras débiles).")
        elif 6 <= magnitud_terremoto < 7:
            print("Muy fuerte")
        elif  magnitud_terremoto > 8:
            print("Extremo" + " (puede causar graves daños a gran escala).")



match opcion:
    case "10":
        """10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año 
                    Periodo del año Desde el 21 de diciembre hasta el 20 de marzo (incluidos) 
                    Estación en el hemisferio norte: Invierno
                    Estación en el hemisferio sur: Verano 

                    Estación en el hemisferio sur Desde el 21 de marzo hasta el 20 de junio (incluidos) 
                    Estación en el hemisferio norte: Primavera 
                    Estación en el hemisferio sur: Otoño

                    Desde el 21 de junio hasta el 20 de septiembre (incluidos) 
                    Estación en el hemisferio norte: Verano 
                    Estación en el hemisferio sur: Invierno

                    Desde el 21 de septiembre hasta el 20 de diciembre (incluidos) 
                    Estación en el hemisferio norte: Invierno
                    Estación en el hemisferio sur: Primavera

               Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
               del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
               si el usuario se encuentra en otoño, invierno, primavera o verano. """
    

        hemisferio=input("Ingrese el hemisferio (N/S): ") 
        hemisferio=hemisferio.upper()
        periodo=input("Elija el periodo actual: \n 1) Desde el 21 de diciembre hasta el 20 de marzo (incluidos) . \n 2) Desde el 21 de marzo hasta el 20 de junio (incluidos).  \n 3) Desde el 21 de junio hasta el 20 de septiembre (incluidos). \n 4) Desde el 21 de septiembre hasta el 20 de diciembre (incluidos): \n ")  
                
        invierno_norte= periodo=="1" and hemisferio=="N" # 21 de diciembre hasta el 20 de marzo (incluidos)
        invierno_sur= periodo=="3" and hemisferio=="S" # 21 de junio hasta el 20 de septiembre (incluidos)
        primavera_norte=periodo=="2" and hemisferio=="N" # 21 de marzo hasta el 20 de junio (incluidos)
        primavera_sur=periodo=="4" and hemisferio=="S" # 21 de septiembre hasta el 20 de diciembre (incluidos)
        verano_norte=periodo=="3" and hemisferio=="N" # 21 de junio hasta el 20 de septiembre (incluidos)
        verano_sur=periodo=="1" and hemisferio=="S" # 21 de diciembre hasta el 20 de marzo (incluidos)
        otoño_norte=periodo=="4" and hemisferio=="N" # 21 de septiembre hasta el 20 de diciembre (incluidos)
        otoño_sur=periodo=="2" and hemisferio=="S" # 21 de marzo hasta el 20 de junio (incluidos)       

        if invierno_norte or invierno_sur: # 
            print("Usted esta en invierno")
        elif primavera_norte or primavera_sur:
            print("Usted esta en primavera")
        elif verano_norte or verano_sur:
            print("usted esta en verano")
        elif otoño_norte or otoño_sur:
            print("Usted esta en otoño")
        else:
            pass
