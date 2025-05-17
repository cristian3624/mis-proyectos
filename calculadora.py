# Solicitar los dos números reales
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Solicitar el carácter de la operación
operacion = input("Ingrese la operación (+, -, *, /): ")

# Evaluar la operación
if operacion == "+":
    resultado = num1 + num2
    print(f"Resultado: {resultado}")

elif operacion == "-":
    resultado = num1 - num2
    print(f"Resultado: {resultado}")

elif operacion == "*":
    resultado = num1 * num2
    print(f"Resultado: {resultado}")

elif operacion == "/":
    if num2 == 0:
        print("⚠ Error: No se puede dividir por cero.")
    else:
        resultado = num1 / num2
        print(f"Resultado: {resultado}")

else:
    print("⚠ Error: Operación no válida.")