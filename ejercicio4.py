# Pedir un número al usuario
numero = int(input("Ingresá un número: "))

# Mostrar la tabla del 1 al 10
print(f"Tabla del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
