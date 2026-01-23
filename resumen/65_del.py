# Resumen de del

# Qué es 
# del es una instrucción que elimina una referencia a un objeto, no necesariamente el 
# objeto en sí.

# Cómo actúa
# Si borrás una variable local o global, desaparece el nombre del espacio de nombres 
# correspondiente.

x = 10
del x
# ahora x ya no existe → NameError si lo usás
try:
    print(x)
except Exception as e:
    print(e)

####################################################################

class A: pass
a = A()
a.valor = 5
del a.valor
# ahora 'valor' ya no está en 'a'
try:
    print(a.valor)
except Exception as e:
    print(e)
####################################################################

lista = [1, 2, 3]
del lista[1]   # borra el elemento en índice 1
# lista = [1, 3]
print(lista)

dic = {"a": 1, "b": 2}
del dic["a"]
# dic = {"b": 2}
print(dic)
####################################################################

# Conclusión
# del elimina nombres, atributos o ítems, no objetos directamente.

# El recolector de basura se encarga de liberar la memoria cuando ya no hay referencias.

# Es útil para limpiar variables, atributos o elementos de colecciones.