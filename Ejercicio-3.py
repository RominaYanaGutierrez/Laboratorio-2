nros_pares = 0
nros_impares = 0

while True:
    nro = int(input("Ingrese un número (o ingrese 0 para salir): "))
    
    if nro == 0:
        break
    
    if nro % 2 == 0:
        nros_pares += 1
    else:
        nros_impares += 1

print("Cantidad de números pares:", nros_pares)
print("Cantidad de números impares:", nros_impares)
