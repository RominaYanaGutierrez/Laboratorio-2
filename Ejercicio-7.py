def es_primo(nro):
    if nro < 2:
        return False
    for i in range(2, int(nro/2) + 1):
        if nro % i == 0:
            return False
    return True

nro = int(input("Ingrese un número: "))

if es_primo(nro):
    print(f"El número {nro} es primo")
else:
    print(f"El número {nro} no es primo")
