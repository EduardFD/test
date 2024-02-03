# Este es un archivo Python basico para practicas de Git.

# Importamos la biblioteca math
import math

# Definimos una funcion para calcular el area de un circulo
def area_circulo(radio):
  """
  Esta funcion calcula el area de un circulo.

  Parametros:
    radio: El radio del circulo.

  Retorno:
    El area del circulo.
  """
  return math.pi * radio ** 2

# Imprimimos el �rea de un c�rculo con radio 5
print(f"El area de un circulo con radio 5 es: {area_circulo(5)}")

# Definimos una variable para almacenar el nombre del usuario
nombre_usuario = input("Introduce tu nombre: ")

# Imprimimos un mensaje de bienvenida
print(f"Hola {nombre_usuario}! Bienvenido a las practicas de Git.")
