# ¿Qué hace any()?
# Propósito: Verificar si algún elemento de una colección cumple una condición de verdad.

# Sintaxis:
# any(iterable)
# Donde iterable puede ser una lista, tupla, conjunto, diccionario o cualquier objeto iterable.

# Funcionamiento:
# Recorre todos los elementos.
# Convierte cada uno a booleano con bool().
# Si encuentra al menos un True, retorna True.
# Si todos son False, retorna False.

# Ejemplo 1: lista con valores booleanos
valores = [False, False, True]
print(any(valores))   # Resultado: True

# Ejemplo 2: lista vacía
print(any([]))        # Resultado: False

# Ejemplo 3: números
numeros = [0, 0, 5]
print(any(numeros))   # Resultado: True (porque 5 es True)

# Ejemplo 4: strings
palabras = ["", "", "hola"]
print(any(palabras))  # Resultado: True (porque "hola" no es vacío)



# any() → Al menos un elemento es verdadero → any([0, 1, 0]) → True
# all() → Todos los elementos son verdaderos → all([1, 2, 3]) → True

###################################################################################
usuarios = [
    {"nombre": "Ana", "activo": False},
    {"nombre": "Luis", "activo": False},
    {"nombre": "María", "activo": True}
]

# ¿Hay algún usuario activo?
hay_activo = any(u["activo"] for u in usuarios)
print(hay_activo)  # Resultado: True

###################################################################################

productos = [
    {"id": 1, "nombre": "Laptop", "precio": 950},
    {"id": 2, "nombre": "Mouse", "precio": 25},
    {"id": 3, "nombre": "Teclado", "precio": 45}
]

# ¿Algún producto cuesta más de 100?
caro = any(p["precio"] > 100 for p in productos)
print(caro)  # Resultado: True

###################################################################################

estudiantes = [
    {"nombre": "Juan", "nota": 4},
    {"nombre": "Sofía", "nota": 8},
    {"nombre": "Pedro", "nota": 5}
]

aprobado = any(e["nota"] >= 6 for e in estudiantes)
print(aprobado)  # Resultado: True

###################################################################################

pedidos = [
    {"id": 1, "items": ["pan", "leche"]},
    {"id": 2, "items": ["agua", "galletas"]},
    {"id": 3, "items": ["carne", "vino"]}
]

# ¿Algún pedido incluye 'vino'?
contiene_vino = any("vino" in pedido["items"] for pedido in pedidos)
print(contiene_vino) # Resultado: True

###################################################################################

#✨ Como ves, any() se convierte en una herramienta poderosa para consultar y 
# validar datos en estructuras complejas sin necesidad de escribir bucles largos.

###################################################################################

estudiantes = [
    {"nombre": "Juan", "nota": 4, "inscripto": True},
    {"nombre": "Sofía", "nota": 8, "inscripto": True},
    {"nombre": "Pedro", "nota": 5, "inscripto": True}
]

# ¿Algún estudiante aprobó?
aprobado = any(e["nota"] >= 6 for e in estudiantes)

# ¿Todos están inscriptos?
todos_inscriptos = all(e["inscripto"] for e in estudiantes)

print(aprobado and todos_inscriptos)  # Resultado: True