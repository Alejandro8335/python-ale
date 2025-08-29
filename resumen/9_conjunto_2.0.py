
#creando un conjunto con set(con una lista)
conjunto = set(["ale","leon","minguez"])

#metiendo conjunto dentro de otro conjunto
conjunto1 = frozenset ({"dato1","dato2"})
conjunto2 = {conjunto1,"dato3" }
print(conjunto2)

#teoria de conjunto 
conjunto_1 = {1,2,3}
conjunto_2 = {1,2,3,-4}

#verificando si es un subconjunto
resultado = conjunto_1.issubset(conjunto_2)
resultado_1 = conjunto_1 <= conjunto_2 #es lo mismo

#verificando si es un superconjunto
resultado_2 = conjunto_2.issuperset(conjunto_1)
resultado_3 = conjunto_2 > conjunto_1 #es lo mismo(el igual sobra,pero no importa si esta)

#verificar si hay algun numero en comun
resultado_4 = conjunto_2.isdisjoint(conjunto_1)
#si hay un elemento en comun devuelve false si no devuelve true

print(resultado_4)
