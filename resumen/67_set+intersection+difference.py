# Podemos calcular la intersección entre dos sets de la siguiente manera.

set1 = set(['amarillo', 'rojo', 'azul', 'verde', 'negro'])
set2 = set(['rojo', 'marrón'])
print(f"set2.intersection: {set2.intersection(set1)}")
# Salida: set(['rojo'])
print(f"set1.intersection: {set1.intersection(set2)}")
# Salida: set(['rojo'])

########################################################################
# Con el método difference podemos calcular la diferencia entre dos sets. 
# Es importante notar que no es lo mismo la diferencia A-B que B-A.

set1 = set(['amarillo', 'rojo', 'azul', 'verde', 'negro'])
set2 = set(['rojo', 'marrón'])
print(f"set2.difference(set1): {set2.difference(set1)}")
# Salida: set(['marrón'])
print(f"set1.difference(set2): {set1.difference(set2)}")
# Salida: set(['negro', 'amarillo', 'azul', 'verde'])