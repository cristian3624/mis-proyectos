nombre = input("ingrese su nombre:")
try:
    edad = int(input ("ingrese su edad:"))
    print(f"Hola {nombre} tenes {edad} años")
except ValueError:
           print("dato incorrecto")