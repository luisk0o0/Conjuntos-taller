
def calculate_union(alphabet_a, alphabet_b):
    return alphabet_a.union(alphabet_b)
    

def calculate_difference(alphabet_a, alphabet_b):
    return alphabet_a.difference(alphabet_b)
    

def calculate_intersection(alphabet_a, alphabet_b):
    return alphabet_a.intersection(alphabet_b)

enter_a = input("Ingrese el alfabeto A en el formato {elemento1, elemento2, ...}: ")
try:
    # Parseamos la entrada del usuario y convertimos los elementos en un conjunto
    alphabet_1  = set(enter_a.strip('{}').split(','))

    # Solicitamos al usuario que ingrese el alfabeto B
    enter_b = input("Ingrese el alfabeto B en el formato {elemento1, elemento2, ...}: ")
    
    # Parseamos la entrada del usuario y convertimos los elementos en un conjunto
    alphabet_2 = set(enter_b.strip('{}').split(','))

    # Imprimimos los alfabetos A y B
    print("Alfabeto A:", alphabet_1)
    print("Alfabeto B:", alphabet_2)

except ValueError:
    print("Error al ingresar los conjuntos. Asegúrate de usar el formato correcto.")

union=calculate_union(alphabet_1,alphabet_2)
print("Union",union)

difeference= calculate_difference(alphabet_1,alphabet_2)
print("difeference",difeference)

intersection= calculate_intersection(alphabet_1,alphabet_2)
print("intersection",intersection)

