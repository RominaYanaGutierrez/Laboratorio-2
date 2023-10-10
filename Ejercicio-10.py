def convertir_fecha(fecha):
    meses = {
        "Enero": "01",
        "Febrero": "02",
        "Marzo": "03",
        "Abril": "04",
        "Mayo": "05",
        "Junio": "06",
        "Julio": "07",
        "Agosto": "08",
        "Septiembre": "09",
        "Octubre": "10",
        "Noviembre": "11",
        "Diciembre": "12"
    }
    partes = fecha.split()
    if len(partes) == 3:
        mes = meses[partes[0]]
        dia = partes[1].strip(",")
        anio = partes[2]
    else:
        mes, dia, anio = fecha.split("/")
    return f"{anio}-{mes}-{dia.zfill(2)}"

fecha = input("Ingrese una fecha (en formato mes-día-año (8-21-2984) o mes día, año (Agosto 11, 5451)): ")
fecha_convertida = convertir_fecha(fecha)
print("Fecha convertida:", fecha_convertida)
