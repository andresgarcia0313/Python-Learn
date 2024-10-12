# Declaración de diferentes tipos de variables en Python

# Entero
numero_entero = 10

# Flotante
numero_flotante = 10.5

# Cadena de texto
cadena_texto = "Hola, mundo"

# Booleano
booleano = True

# Lista
lista = [1, 2, 3, 4, 5]

# Tupla
tupla = (1, 2, 3, 4, 5)

# Conjunto
conjunto = {1, 2, 3, 4, 5}

# Diccionario
diccionario = {
    "nombre": "Andrés",
    "edad": 25,
    "ciudad": "Bogotá"
}

# Ninguno (None)
ninguno = None
print(cadena_texto)

# Imprimir todas las variables

print(f"Entero: {numero_entero}")
print(f"Flotante: {numero_flotante}")
print(f"Cadena de texto: {cadena_texto}")
print(f"Booleano: {booleano}")
print(f"Lista: {lista}")
print(f"Tupla: {tupla}")
print(f"Conjunto: {conjunto}")
print(f"Diccionario: {diccionario}")
print(f"Ninguno: {ninguno}")

# Muestrame otros tipos de imprimir y concatenado
cadena_texto_numero_entero = str(numero_entero)
print("Entero:"  + cadena_texto_numero_entero)
print("Flotante: " + str(numero_flotante))
print("Cadena de texto: " + cadena_texto)
print("Booleano: " + str(booleano))
print("Lista: " + str(lista))
print("Tupla: " + str(tupla))
print("Conjunto: " + str(conjunto))
print("Diccionario: " + str(diccionario))
print("Ninguno: " + str(ninguno))
# Muestrame otros tipos de imprimir y concatenado
print("Entero: %d" % numero_entero)
print("Flotante: %f" % numero_flotante)

