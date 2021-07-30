class Cadena():
    def __init__(self,cadena):
        self.cadena=cadena   
    def  recorrerCadena(self):
        print('_______________________________________')
        print("Recorrer y presentar los datos de una cadena")
        print('____________________________________')
        for x in self.cadena:
            print(x,'',end='')  
    def  buscarCaracter(self,buscado):
        print('______________________________')
        print("Buscar un carácter en una cadena")
        print('____________________________')
        acum=0
        for x,i in enumerate(self.cadena):
            if i== buscado:
                acum=acum+1
        print("Su caracter se encuentra {} veces, dentro de la cadena".format(acum))
        print()  
    def  listaPosiciones(self,caracter):
        print('_________________________________________________________________')
        print("Retornar una lista con la posiciones dado un carácter de la cadena")
        print('__________________________________________________________________')
        acum=0
        aux=[]
        for x,i in enumerate(self.cadena):
            acum=acum+1
            if i == caracter:
                aux.append(acum)
                lista=aux
        print(lista)        
                  
    def listaPalabras(self):
        pass  
    def cadenaLista(self):
        pass  
    def insertarDato(self,buscado,posicion):
        pass  
    def eliminarOcurrencias(buscado):
        pass  
    def retornaValor(posicion):
        pass  
    def concatenarCadena(dato):
        pass         

cadena='hola como estas'
cad= Cadena(cadena)
# cad.recorrerCadena()
#cad.buscarCaracter('b')
cad.listaPosiciones('v')
