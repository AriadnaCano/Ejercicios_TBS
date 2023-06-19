def dias(numero_semana):
    if numero_semana == 1:
        return "Lunes"
    elif numero_semana == 2:
        return "Martes"
    elif numero_semana == 3:
        return "Miércoles"
    elif numero_semana == 4:
        return "Jueves"
    elif numero_semana == 5:
        return "Viernes"
    elif numero_semana == 6:
        return "Sábado"
    elif numero_semana == 7:
        return "Domingo"
    else:
        return "No es válido"

def comparacion(num_1, num_2):
    if num_1 == num_2:
        return "Son iguales"
    if num_1 > num_2:
        return "Es mayor"
    if num_2 > num_1:
        return "Es menor"

def funcion (argumento):
    diccionario = {}
    for letra in argumento:
        if letra in diccionario:
            diccionario[letra] = diccionario [letra] + 1
        else:
            diccionario[letra] = 1
    return diccionario

def junta_palabras(*args):
    return " ".join(args)

def triangulo (base, altura):
    return base * altura / 2
