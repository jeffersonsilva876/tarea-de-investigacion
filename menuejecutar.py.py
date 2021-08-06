import os

class Menu:
    def __init__(self, titulo, opciones=[]):
        self.titulo=titulo
        self.opciones= opciones
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc = input("Elija la opción [1...{}]:".format(len(self.opciones)))
        return opc
opc = ""
while opc != "5":
    os.system("cls")
    men = Menu("Menu Principal",["1)Calculadora", "2)Operación Numeros", "3)Tratamiento de Listas","4)Operacion de Cadenas", "5)Salir" ])
    opc = men.menu()

    if opc == "1":
        opc1 = ""
        while opc1 != "10":
            os.system("cls")
            men1 = Menu("Menu Calculadora",["1)Suma", "2)Resta", "3)Multiplicación","4)División", "5)Exponente", "6)Valor Absoluto", "7)Circunferencia", "8)Área del Circulo", "9)Área del Cuadrado", "10)Salir"])
            opc1 = men1.menu()
            if opc1 == "1":
                os.system("cls")
                print("Ingresa los números para la suma")
                n1 = int(input("Ingrese el número 1 :"))
                n2 = int(input("Ingrese el segundo valor:"))
                print("La suma total es: ", n1 + n2)
                input("Presione enter para avanzar...")
                
            elif opc1 == "2":
                os.system("cls")
                print("Ingresa los números para la resta")
                n1 = int(input("Ingrese el número 1:"))
                n2 = int(input("Ingrese el número 2:"))
                print("La resta de los números es: ", n1 - n2)
                input("Presione enter para avanzar...")
                
            elif opc1 == "3":
                os.system("cls")
                print("Ingresa los números para la  multiplicacion")
                n1 = int(input("Ingrese el número 1:"))
                n2 = int(input("Ingrese el número 2:"))
                print("La multiplicación de los números es: ", n1 * n2)
                input("Presione enter para avanzar...")
             
            elif opc1 == "4":
                os.system("cls")
                print("Ingresa los números para la división")
                n1 = int(input("Ingrese el número 1:"))
                n2 = int(input("Ingrese el número 2:"))
                print("La división de los números es: ", n1/n2)
                input("Presione enter para avanzar...")   
                
            elif opc1 == "5":
                os.system("cls")
                print("Calculadora de Exponentes")
                n1 = int(input("Ingresa el primer número como base:"))
                n2 = int(input("Ingrea el segundo número como exponente:"))
                print("La respuesta es: ", n1**n2)
                input("Presione enter para avanzar...")
                
            elif opc1 == "6":
                os.system("cls")
                print("Valor Absoluto")
                n1 = int(input("Ingresa el número:"))
                print("El valor absoluto del valor es: ", abs(n1))
                input("Presione enter para avanzar...") 
            
            elif opc1 == "7":
                os.system("cls")
                print("Circunferencia")
                pi=3.1416
                n1 = int(input("Ingresa el valor del radio:"))
                print("Respuesta: ", 2*pi*n1)
                input("Presione enter para avanzar...")
                
            elif opc1 == "8":
                os.system("cls")
                print("Área del Circulo")
                pi=3.1416
                n1 = int(input("Ingrea el valor del radio:"))
                print("El área del Circulo es: ", pi*n1**2)
                input("Presione enter para avanzar...")  
                
            elif opc1 == "9":
                os.system("cls")
                print("Área del Cuadrado")
                n2 = int(input("Ingresa el valor del lado:"))
                print("El área del cuadrado es: ", n2**2)
                input("Presione enter para avanzar...")   

    elif opc == "2":
        opc2 = ""
        while opc2 != "10":
            os.system("cls")
            men2 = Menu("Menu Operación Numeros",["1)Presentar los números de 1 a n", "2)Múltiplo de cualquier numero", "3)Presentar los divisores de un numero","4)Número Primo", "5)Perfecto", "6)factorial", "7)Fibonacci de una serie de n números", "8)Primos Gemelos", "9)Números Amigos", "10)Salir"])
            opc2 = men2.menu()
            if opc2 == "1":
                os.system("cls")
                print("Presentar los números de 1 a n")
                n1 = int(input("Ingrese el número hasta donde desea presentar:"))
                for x in range(1,n1 +1):
                     print( x )
                input("Presione enter para avanzar...")
                
            elif opc2 == "2":
                os.system("cls")
                print("Múltiplo de cualquier número")
                n1 = int(input("Ingresa el primer número:"))
                n2 = int(input("Ingresa el segundo número:"))
                if n1 % n2 == 0:
                    print("El numero {} si es multiplo de {}".format(n1,n2))
                else:
                    print("El numero {} no es multiplo de {}".format(n1,n2))
                input("Presione enter para avanzar...")
                
            elif opc2 == "3":
                os.system("cls")
                print("Presentar los divisores de un número")
                n1 = int(input("Ingrese el primer valor:"))
                contador = 0
                print("los divisores de ",n1)
                for divisor in range(1,n1+1):
                     if (n1 % divisor) == 0 :
                         print(divisor,"es divisor")
                         contador += 1
                print("el numero ",n1," tiene ",contador," divisores")
                input("Presione enter para avanzar...")
                
            elif opc2 == "4":
                os.system("cls")
                print("Número Primo")
                n1 = int(input("Ingresa el valor para saber si es o no primo:"))
                contador = 0
                for i in range(1, n1 + 1):
                    if n1 % i == 0:
                        contador += 1
                if contador == 2:
                    print("Es un número primo")
                else:  
                   print("No es un número primo")
                input("Presione enter para avanzar...")
                
            elif opc2 == "5":
                os.system("cls")
                print("Perfecto")
                n1 = int(input("Ingrese el número:"))
                acu=0
                for i in range(1, n1):
                    if n1 % i == 0:
                        acu = acu+i
                if acu == n1:
                    print("Numero Perfecto")
                else:
                    print("Numero no es perfecto")
                input("Presione enter para avanzar...")
                
            elif opc2 == "6":
                os.system("cls")
                print("Factorial de cualquier numero")
                def factorial(n):
                    if n==0 or n==1:
                        resultado = 1
                    elif n>1:
                        resultado=n*factorial(n-1)
                    return resultado
                n1= int(input("Ingrese el valor:"))
                fact=factorial(n1)
                print(fact)
                input("Presione enter para avanzar...")
                
            elif opc2 == "7":
                os.system("cls")
                print("Fibonacci de una serie de n números")
                def fib(n):
                    a, b = 0,1
                    while a < n:
                        print(a, end=' ')
                        a, b = b, a + b
                m = int(input("Ingresa límite máximo de la sucesión: "))     
                fib(m)
                input("Presione enter para avanzar...")
                
            elif opc2 == "8":
                os.system("cls")
                print("Primos Gemelos")
                n1 = int(input("Ingresa el primer número:"))
                n2 = int(input("Ingresa el segundo número:"))
                ejer= 2
                siesprimo= lambda x: x == 3 or (x % 2 != 0 and x % 3 != 0)
                
                if n1 == n2:
                    print("Los números ingresados no son rimos gemelos")
                    
                elif n1 == 1 or n2 == 1:
                    print("los números ingresados son primos gemelos")
                    
                else:
                    if siesprimo(n1) and siesprimo(n2):
                        if n1>n2:
                            if n1-n2==ejer:
                                print("Los números ingresados son primos gemelos")
                            else:
                                print("Los números ingresados no son primos gemelos")
                                
                        elif n2>n1:
                            if n2-n1==ejer:
                                print("Los números ingresados son primos gemelos")
                            else:
                                print("Los números ingresados no son primos gemelos")
                    
                    else:
                        print("Los números ingresados no son primos gemelos")
                                
                input("Presione enter para avanzar...")
                
            elif opc2 == "9":
                os.system("cls")
                print("Números Amigos")
                
                # Definición de la función de comprobación de números amigos
                def numeros_amigos(x,y):
                    suma_x=0
                    suma_y=0
                    for i in range(1,x):
                        if x%i==0:
                            suma_x+=i
 
                    for k in range(1,y):
                        if y%k==0:
                            suma_y+=k
 
                    return suma_x==y and suma_y==x
 
                # Cuerpo del programa
                n1=int(input('Ingrese el número 1: '))
                n2=int(input('Ingrese el número 2: '))
 
                if numeros_amigos(n1,n2):
                    print ('¡Son amigos!')
                else:
                    print ('No son amigos')

                input("Presione enter para avanzar...")       

    elif opc == "3":
        opc3 = ""
        while opc3 != "11":
            os.system("cls")
            men3 = Menu("Menu Tratamiento Listas",["1)Recorrer y presentar los datos de una lista", "2)Buscar un valor en una lista", "3)Retornar una lista con los factoriales","4)Retornar una lista de números primos", "5)Recorrer una lista de diccionario con notas de alumnos", "6)Insertar un dato en una Lista dada lo Posición", "7)Eliminar todas las ocurrencias en una Lista", "8)Retornar cualquier valor de una lista eliminándolo", "9)Copiar cada elemento de una tupla en una lista", "10)Dar el vuelto a varios clientes", "11)Salir"])
            opc3 = men3.menu()   
            if opc3 == "1":
                os.system("cls")
                print("Recorrer y presentar los datos de una lista")      
                num = int(input("¿Cuántos elementos desea en la lista?: "))
                lista = []
                for x in range(num):
                    valor = int(input("Ingresa el elemento:")) 
                    lista.append(valor)
                aux=lista    
                print("Resultado: ", lista) 
                input("Presione enter para avanzar...") 
            
            elif opc3 == "2":
                os.system("cls")
                print("Buscar un valor en una lista")
                lista = []       
                num = int(input("Cuantos elementos desea en la lista?: "))
                for i in range(num):
                    valor = int(input("Ingrese el elemento:")) 
                    lista.append(valor)
                aux=lista
                buscar = int(input("Ingrese el valor a buscar:"))                
                print("El elemento buscado es: ", buscar) 
                input("Presione enter para avanzar...") 
                
            elif opc3 == "3":
                os.system("cls")
                print("Retornar una lista con los factoriales")
                lista = []       
                num = int(input("Cuantos elementos desea en la lista?: "))
                for i in range(num):
                    valor = int(input("Ingrese el elemento:")) 
                    lista.append(valor)
                aux=lista
                print("Elementos retornados: ", lista) 
                input("Presione enter para avanzar...") 
                
            elif opc3 == "4":
                os.system("cls")
                print("Retornar una lista de números primos")
                lista = []       
                num = int(input("Cuantos elementos desea en la lista?: "))
                for i in range(num):
                    valor = int(input("Ingrese el elemento:")) 
                    lista.append(valor)
                aux=lista
                print("Elementos retornados: ", lista) 
                input("Presione enter para avanzar...") 
                
            elif opc3 == "5":
                os.system("cls")
                print("Recorrer una lista de diccionario con notas de alumnos")
                diccionario=[{'nombre':'Javier', 'nota':50},{'nombre':'Arianna','nota':100},{'nombre':'Heidy','nota':80}]
                print("Elementos recorridos: ", diccionario) 
                input("Presione enter para avanzar...") 
                
            elif opc3 == "6":
                os.system("cls")
                print("Insertar un dato en una Lista dada lo Posición")
                lista = []       
                num = int(input("¿Cuántos elementos desea en la lista?: "))
                for i in range(num):
                    valor = int(input("Ingrese el elemento:")) 
                    lista.append(valor)
                aux=lista
                ele = int(input("Ingrese el elemento que desea colocar a la lista:"))
                val = int(input("Ingrese la posicion en la que se insertara el elemento:"))
                print("Insertar datos: ", ele,val-1)  
                input("Presione enter para avanzar...") 
                
            elif opc3 == "7":
                os.system("cls")
                print("Eliminar todas las ocurrencias en una Lista")
                miLista = [2, 1, 3, 5, 1, 1, 1, 0]
                valueToBeRemoved = 1

                result = filter(lambda val: val !=  valueToBeRemoved, miLista) 
                print(list(result))
                input("Presione enter para avanzar...") 
                
                
            elif opc3 == "8":
                os.system("cls")
                print("Retornar cualquier valor de una lista eliminándolo")
                lista = []       
                num = int(input("¿Cuántos elementos desea en la lista?: "))
                for i in range(num):
                    valor = int(input("Ingrese el elemento:")) 
                    lista.append(valor)
                aux=lista
                print("Respuesta: ", lista)  
                input("Presione enter para avanzar...") 
                
            elif opc3 == "9":
                os.system("cls")
                print("Copiar cada elemento de una tupla en una lista")
                tupla = (2,2,3,4,5,6,7)
                print("Respuesta: ", tupla)  
                input("Presione enter para avanzar...") 
                
            elif opc3 == "10":
                os.system("cls")
                print("Dar el vuelto a varios clientes")
                diccionario={}
                lista=[]
                num=int(input("Digite el número de diccionarios que desea ingresar: "))
                for x in range(num):
                    clave=(input("ingrese su clave para el diccionario: ")).capitalize()
                    valor=int(input("ingrese el valor de la clave para el diccionario: "))
                    diccionario[clave]=valor
                    lista.append(diccionario)
                    diccionario={}
                print("Respuesta: ", lista)  
                input("Presione enter para avanzar...") 
                

    elif opc == "4":
        opc4 = ""
        while opc4 != "10":
            os.system("cls")
            men4 = Menu("Menu Operaciónes de Cadenas",["1)Recorrer y presentar los datos de una cadena", "2)Buscar un carácter en una cadena", "3)Retornar una lista con la posiciones dado un carácter de la cadena","4)Retornar una lista con todas las palabras de una cadena", "5)Retornar una cadena a partir de una lista", "6)Insertar un dato en una cadena dada lo Posición", "7)Eliminar todas las ocurrencias en una cadena", "8)Retornar cualquier valor de una cadena eliminándolo", "9)Concatenar cadena", "10)Salir"])
            opc4 = men4.menu()
            if opc4 == "1":
                os.system("cls")
                print(" Recorrer y presentar los datos de una cadena")
                Texto = input("Ingrese la Cadena:")
                # print("Respuesta: ", Texto) 
                # input("Presione enter para avanzar...")
                print("Respuesta: ")
                for x in Texto:
                    print( x,'',end='')
                input("Presione enter para avanzar...")
            
            elif opc4 == "2":
                os.system("cls")
                print("Buscar un carácter en una cadena")
                Texto = input("Ingrese la Cadena:")
                buscar = input("Ingrese el caracter que desea buscar:")
                print("Respuesta: ", buscar)
                input("Presione enter para avanzar...")
                
            elif opc4 == "3":
                os.system("cls")
                print("Retornar una lista con la posiciones dado un carácter de la cadena")
                Texto = input("Ingrese la Cadena:")
                buscar = input("Ingrese el caracter:")
                print("Respuesta: ", buscar)
                input("Presione enter para avanzar...")
                
            elif opc4 == "4":
                os.system("cls")
                print("Retornar una lista con todas las palabras de una cadena")
                Texto = input("Ingrese la Cadena:")
                print("Respuesta: ", Texto)
                input("Presione enter para avanzar...")
                
            elif opc4 == "5":
                os.system("cls")
                print("Retornar una cadena a partir de una lista")
                lista=[]
                num = int(input("¿Cuántos elementos desea insertar en la lista?: "))
                lista = []
                for x in range(num):
                    frase = (input("Ingrese el elemento:")) 
                    lista.append(frase)
                aux=lista 
                print("La lista se creada es la siguuente:")
                print(lista)   
                print("Transformacion a cadena:")
                input("Presione enter para avanzar...")
                
            elif opc4 == "6":
                os.system("cls")
                print("Insertar un dato en una cadena dada lo Posición")
                Texto = input("Ingresa la Cadena:")
                textoInsertar = input("Ingresa el texto que desea insertar:")
                posicionInsertar = int(input("¿En qué posicion desea insertar el texto?"))
                print("Respuesta: ", textoInsertar,posicionInsertar)
                input("Presione enter para avanzar...")   
            
            elif opc4 == "7":
                os.system("cls")
                print("Eliminar todas las ocurrencias en una cadena")
                Texto = input("Ingrese la Cadena:")
                Buscado = input("Ingrese el elemento a buscar:")
                print("Respuesta: ", Buscado)
                input("Presione enter para avanzar...")
        
            elif opc4 == "8":
                os.system("cls")
                print("Retornar cualquier valor de una cadena eliminándolo")
                texto = input("Ingrese el texto:")    
                pos = (input("Ingrese posicion:"))  
                print("Respuesta: ", pos)
                input("Presione enter para avanzar...")
                
            elif opc4 == "9":
                os.system("cls")
                print("Concatenar cadenas")
                n1=(input('Ingresa texto 1: '))
                n2=(input('Ingresa texto 2: '))
                mensaje1 = n1 + ' ' + n2
                print("Respuesta: " , mensaje1)
                input("Presione enter para avanzar...")
                  
    elif opc == "5":
        print("*** HA SALIDO DEL PROGRAMA ***")
    else:
        print("Opcion no valida")

print("VUELVA PRONTO")
    