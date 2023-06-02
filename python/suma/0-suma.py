def suma(numero_1, numero_2):
    try:
        value_1 = int(numero_1)
        value_2 = int(numero_2)
    except:
        return "Error: ingrese un valor valido."
    return value_1 + value_2