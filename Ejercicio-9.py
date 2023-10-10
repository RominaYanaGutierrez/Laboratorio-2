def omitir_vocales(cadena):
    vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    nueva_cadena = ''
    for caracter in cadena:
        if caracter not in vocales:
            nueva_cadena += caracter
    return nueva_cadena

cadena = input("Ingrese una cadena de texto: ")
cadena_sin_vocales = omitir_vocales(cadena)
print("Cadena sin vocales:", cadena_sin_vocales)
