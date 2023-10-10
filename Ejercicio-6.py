def fibonacci(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return fib

serie_fibonacci = fibonacci(50)

print("Serie de Fibonacci entre 0 y 50:")
for numero in serie_fibonacci:
    print(numero)
