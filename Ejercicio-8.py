def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

nro = int(input("Ingrese un número entero no negativo: "))

resultado_factorial = factorial(nro)

if resultado_factorial is None:
    print("El número ingresado es negativo. Por favor, ingrese un número entero no negativo.")
else:
    print(f"El factorial de {nro} es: {resultado_factorial}")
