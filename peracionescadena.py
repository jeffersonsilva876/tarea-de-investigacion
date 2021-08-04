class Cadena():
    def __init__(self,cadena):
        self.cadena=cadena   
    def  recorrerCadena(self):
        print("Recorrer y presentar los datos de la cadena")
        for x in self.cadena:
            print(x,'',end='')
    def  buscarCaracter(self,buscado):
        print("Buscar un carácter en la cadena")
        acum=0
        for x,i in enumerate(self.cadena):
            if i== buscado:
                acum=acum+1
        print("Su caracter se encuentra {} , dentro de la cadena".format(acum))
        print()
  
    def  listaPosiciones(self,caracter):
        print("Retornar una lista con la posiciones dado un carácter de la cadena")
        acum=0
        aux=[]
        for x,i in enumerate(self.cadena):
            acum=acum+1
            if i == caracter:
                aux.append(acum)
                lista=aux
        print(lista)        
    def listaPalabras(self):
        print("Retornar una lista con todas las palabras de una cadena")
        print(self.cadena.split())
  
    def cadenaLista(self):
        
        print("Retornar una cadena a partir de una lista")
        print(" ".join(self.cadena))  
    def insertarDato(self,insertar,posicion):
        print("Insertar un dato en una cadena dado su Posición")
        if posicion <= len(self.cadena):
            izquierda = self.cadena[:posicion]
            derecha =self.cadena[posicion+1:]
            
            print("{} {} {}".format(izquierda, insertar, derecha))
        else:
            print("La posicion no existe")
          
    def eliminarOcurrencias(self,buscado):
        print("Eliminar las ocurrencias en una cadena")

        print("El elemento buscado se encontro {} veces en la cadena".format(self.cadena.count(buscado)))
  
    def retornaValor(self,posicion):
        print("Retornar cualquier valor de una cadena eliminándolo")

        lista = []
        lista2 = []
        for pos, ele in enumerate (self.cadena):
            if pos == posicion:
                lista.append(self.cadena[pos])      
            else:
                lista2.append(self.cadena[pos])
        print("Se retorna la cadena de esta forma:")
        print(" ".join(lista2))     
        print("Letra de la posicion removido:")           
        print(" ".join(lista))  
    def concatenarCadena(self,nombre):
        print("Concatenar Cadena")
        dato = "Hola, señor(a)"
        final= "Gracias por usar nuestro programa."
        frase= dato+" "+nombre+" "+final
        print(frase)         

# cadena="hola como estas"
# cad= Cadena(cadena)
# # cad.recorrerCadena()
# #cad.buscarCaracter('b')
# cad.listaPosiciones('p')
