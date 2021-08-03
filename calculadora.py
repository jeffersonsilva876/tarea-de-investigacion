class Calculadora:
    def _init_(self, numero1, numero2):
        self.num1=numero1
        self.num2=numero2
        
    def suma(self):
        Suma= self.num1 + self.num2
        print("La suma de los numeros {} y {} es de: {}".format(self.num1,self.num2,total_Sum))
    
    def resta(self):
        Resta= self.num1 - self.num2
        print("La resta de los numeros {} y {} es de: {}".format(self.num1, self.num2, total_Res))
    
    def multiplicacion(self):
        Mult= self.num1 * self.num2
        print("La multiplicación de los numeros {} y {} es de: {}".format(self.num1,self.num2,total_Mul))
                
    def division(self):
        Div=self.num1 / self.num2
        print("La division de los numeros es de: {}".format(total_Div))
        
class CalEstandar(Calculadora):
    def _init_(self, numero1, numero2):
        super()._init_(numero1, numero2)
        
        
    def multiplicacion(self):
        Result= self.num1 * self.num2
        return Result
    
    def exponente(self):
        Exp= self.num1**self.num2
        print("la respuesta es: ",total_Exp)

    def valorAbsoluto(sefl,numero3):
        if numero3 < 0:
            numero3 = numero3 *- 1
        return numero3

    
class calCientifica(Calculadora):
    def _init_(self, numero1, numero2):
        super()._init_(numero1, numero2)
        
    def circunferencia(self):
        PI = 3.1416
        Perimetro = 2 * PI * self.num1
        return Perimetro
    
    def areaCirculo(self):
        PI = 3.1416
        area = PI * (self.num1**2)
        return area
    
    def areaCuadrado(self):
        return self.num2 ** 2
    

# cal = calCientifica(1,2,3,4)
# print(cal.circunferencia())
# print(cal.areaCirculo())
# print(cal.areaCuadrado())
