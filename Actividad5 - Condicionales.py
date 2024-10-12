# Ejemplo de función para determinar si una persona es mayor de edad

def es_mayor_de_edad(edad):
    """
    Función que determina si una persona es mayor de edad.
    
    Parámetros:
    edad (int - integer - entero): La edad de la persona.
    
    Retorna:
    bool: True si es mayor de edad, False si no. True=verdadero, False=falso

    >= es el simbolo que significa mayor o igual
    """
    if edad >= 18:  # Verificar si la edad es mayor o igual a 18
        return True  # Retorna True si es mayor de edad
    else: # Si no es mayor o igual a 18 else significa "si no"
        return False  # Retorna False si no es mayor de edad

# Ejemplo de uso de la función

edad_usuario = 20  # Cambia este valor para probar con diferentes edades
print("Edad del usuario:", edad_usuario)
resultado = es_mayor_de_edad(edad_usuario)

# Imprimir el resultado
print("¿Es mayor de edad?", resultado)


""" 
Nivel básico:
Verificar si un número es positivo, negativo o cero
Descripción: Crea un programa que pida al usuario un número y verifique si es positivo, negativo o cero.

Determinar si un estudiante aprobó o no
Descripción: Crea un programa que pida la calificación de un estudiante y determine si ha aprobado (60 o más) o no.


Nivel intermedio:
Comprobar si un número es par o impar
Descripción: Crea un programa que pida al usuario un número y determine si es par o impar.

Verificar si un número está dentro de un rango
Descripción: Crea un programa que pida al usuario un número y verifique si está en el rango de 1 a 10 (inclusive). 
"""