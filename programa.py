print("____________________________________________")
print("|OPERACIONES ARITMETICAS CON DOS FRACCIONES|")
print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

class Fraccion():
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
        if denominador == 0:
            raise Exception("El denominador no puede ser 0")

    def __str__(self):
        return str(self.numerador) + "/" + str(self.denominador)

    def maximo_comun_divisor(self, n, m):
        variable = 0
        while m != 0:
            variable = m
            m = n % m
            n = variable
        return n

    def suma(self, otra):
        mcd = self.maximo_comun_divisor(self.denominador, otra.denominador)
        d_self = mcd/self.denominador
        d_otra = mcd/otra.denominador
        numerador_resultado = (d_self*self.numerador) + (d_otra*otra.numerador)
        return Fraccion(numerador_resultado, mcd)
    def resta(self, otra):
        mcd = self.maximo_comun_divisor(self.denominador, otra.denominador)
        d_self = mcd/self.denominador
        d_otra = mcd/otra.denominador
        numerador_resultado = (d_self*self.numerador) - (d_otra*otra.numerador)
        return Fraccion(numerador_resultado, mcd)
    def multiplicar(self,otra):
        return Fraccion(self.numerador*otra.numerador,self.denominador*otra.denominador)
    def dividir(self,otra):
        return Fraccion(self.numerador*otra.denominador,self.denominador*otra.numerador)
print("\n")
print("SELECCIONE QUE OPERACION DESEA REALIZAR")
print("|(1)|SUMAR||(2)|RESTAR||(3)|MULTIPLICAR||(4)|DIVIDIR|")
print("\n")
z=int(input("Que operacion desea realizar: "))
if(z==1):
  print("Usted escogio sumar:")
  
  numerador=int(input("Ingrese numerador de la primera fraccion: "))
  denominador=int(input("Ingrese denominador de la primera fraccion: "))
  numerador2=int(input("Ingrese numerador de la segunda fraccion: "))
  denominador2=int(input("Ingrese denominador de la segunda fraccion: "))
  f = Fraccion(numerador,denominador)
  f2 = Fraccion(numerador2, denominador2)
  print(f"{f} + {f2} = {f.suma(f2)}")
elif(z==2):
  print("Usted escogio restar:")
  
  numerador=int(input("Ingrese numerador de la primera fraccion: "))
  denominador=int(input("Ingrese denominador de la primera fraccion: "))
  numerador2=int(input("Ingrese numerador de la segunda fraccion: "))
  denominador2=int(input("Ingrese denominador de la segunda fraccion: "))
  f = Fraccion(numerador,denominador)
  f2 = Fraccion(numerador2, denominador2)
  print(f"{f} - {f2} = {f.resta(f2)}")
elif(z==3):
  print("Usted escogio multiplicar:")
 
  numerador=int(input("Ingrese numerador de la primera fraccion: "))
  denominador=int(input("Ingrese denominador de la primera fraccion: "))
  numerador2=int(input("Ingrese numerador de la segunda fraccion: "))
  denominador2=int(input("Ingrese denominador de la segunda fraccion: "))
  f = Fraccion(numerador,denominador)
  f2 = Fraccion(numerador2, denominador2)
  print(f"{f} X {f2} = {f.multiplicar(f2)}")
elif(z==4):
  print("Usted escogio dividir:")
  
  numerador=int(input("Ingrese numerador de la primera fraccion: "))
  denominador=int(input("Ingrese denominador de la primera fraccion: "))
  numerador2=int(input("Ingrese numerador de la segunda fraccion: "))
  denominador2=int(input("Ingrese denominador de la segunda fraccion: "))
  f = Fraccion(numerador,denominador)
  f2 = Fraccion(numerador2, denominador2)
  print(f"{f} / {f2} = {f.dividir(f2)}")


