def cerradura_de_estrella(conjunto, num_simbolos):
    resultado = {()}  # Inicializamos con el conjunto vacío como primer elemento

    for _ in range(num_simbolos):
        nueva_combinacion = set()
        for combinacion in resultado:
            for elemento in conjunto:
                nueva_combinacion.add(combinacion + (elemento,))
        resultado.update(nueva_combinacion)

    return resultado

# Define un conjunto de 5 símbolos específicos
conjunto_simbolos = {'albania', 'bucaramnga', 'cucuta', 'dios', 'elemento'}

# Calcula y muestra la cerradura de estrella con 5 símbolos
cerradura = cerradura_de_estrella(conjunto_simbolos, 2)
print("Cerradura de estrella del conjunto de 5 símbolos:", cerradura)