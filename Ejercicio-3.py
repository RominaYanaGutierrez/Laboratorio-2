numeros = []

while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ")
    
    if respuesta.upper() == "NO":
        break
    
    numero = int(input("Ingrese el número: "))
    numeros.append(numero)

nros_pares = 0
nros_impares = 0

for numero in numeros:
    if numero % 2 == 0:
        nros_pares += 1
    else:
        nros_impares += 1

print("Números ingresados:", numeros)
print("Cantidad de números pares:", nros_pares)
print("Cantidad de números impares:", nros_impares)
