def sumar(a, b):
 # TODO: implementar suma
 return a + b
def restar(a, b):
 return a - b
 pass
def multiplicar(a, b):
    return a * b
pass
def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b
pass
def main():
 numero1 = float(input("Ingrese el primer número: "))
 numero2 = float(input("Ingrese el segundo número: "))
 print("Resultado de la suma:", sumar(numero1, numero2))
 print("Resultado de la resta:", restar(numero1, numero2))
 print("Resultado de la multiplicación:", multiplicar(numero1, numero2))
 print("Resultado de la división:", dividir(numero1, numero2))
if __name__ == "__main__":
 main()