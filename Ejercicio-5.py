def contar_digitos_en_numero():
    numero_str = input("Ingrese un número entero: ")
    digito_str = input("Ingrese un dígito a contar: ")
  
    if len(digito_str) != 1 or not digito_str.isdigit():
        print("Por favor, ingrese un solo dígito válido.")
        return
      
    cantidad = numero_str.count(digito_str)
    print(f"Cantidad de veces {digito_str} en el número: {cantidad}")
contar_digitos_en_numero()
