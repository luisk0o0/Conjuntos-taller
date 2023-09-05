import random
import string

def cerradura_de_estrella_aleatoria(num_simbolos):
    alfabeto = string.ascii_lowercase  # Alfabeto en minúsculas (a-z)
    palabras_generadas = set()
    
    for _ in range(num_simbolos):
        palabra = ''.join(random.choice(alfabeto) for _ in range(random.randint(1, 5)))  # Genera palabras aleatorias
        palabras_generadas.add(palabra)
    
    return palabras_generadas

# Solicita al usuario ingresar el número de símbolos para la cerradura de estrella
num_simbolos = 5

# Calcula y muestra la cerradura de estrella con 5 símbolos generados de forma aleatoria
cerradura_estrella = cerradura_de_estrella_aleatoria(num_simbolos)
print("Cerradura de estrella generada de forma aleatoria:", cerradura_estrella)
#for palabra in cerradura_estrella:
#print(palabra)