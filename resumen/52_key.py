# Usando key para comparar por longitud de cadenas(max,min)
palabras = ["uno", "tres", "cien", "cuarenta"]
print(max(palabras, key=len))   # "cuarenta"
print(min(palabras, key=len))   # "uno"

personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 40},
    {"nombre": "Marta", "edad": 30}
]

print(max(personas, key=lambda p: p["edad"]))  # Luis (edad 40)
print(min(personas, key=lambda p: p["edad"]))  # Ana (edad 25)

# En realidad, key transforma cada elemento en un valor auxiliar,
# y la comparación se hace sobre esos valores auxiliares.

# sorted() devuelve una nueva lista ordenada a partir de los elementos que recibe.
palabras = ["uno", "tres", "cien", "cuarenta"]
print(sorted(palabras, key=len))  # ['uno', 'tres', 'cien', 'cuarenta']
# No modifica la lista original, siempre crea una copia ordenada.(osea retorna una nueva list)

# list.sort() ordena la lista en el lugar, modificando la lista original.
palabras.sort(key=len)
print(palabras)  # ['uno', 'tres', 'cien', 'cuarenta']

personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 40},
    {"nombre": "Marta", "edad": 30}
]

# Ordenar por edad
personas.sort(key=lambda p: p["edad"])
print(personas)
# [{'nombre': 'Ana', 'edad': 25}, {'nombre': 'Marta', 'edad': 30}, {'nombre': 'Luis', 'edad': 40}]

# No devuelve nada (None), porque el cambio ocurre directamente en la lista.