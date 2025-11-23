
opcion = int(input("1,2,3:"))
match opcion:
    #funcionan como elif 
    case 1:
        print("elegiste la opcion 1")
        
    case 2:
        print("elegiste la opcion 2")
        
    case 3:
        print("elegiste la opcion 3")
    
    #es como un else (comodín)    
    case _:
        print("no elegiste ni 1 ni 2 ni 3")
        
x = int(input("tu numero es: "))

match x:
    case _ if x > 0:
        print("positivo")
    case _ if x < 0:
        print("negativo")
    case _:
        print("cero")

lista = [1,3,3]
match lista:
    case [] | [0]:
        print("La lista está vacía")
    case [x]:
       print(f"Un solo elemento: {x}")
    case [x, y]:
        print(f"Dos elementos: {x} y {y}")
    case [x, *resto]:
        print(f"Empieza con {x} y luego hay {len(resto)} más")
        
#no optimo
num = 0
#match num:
#    case _ if num < 3:
#        print("tu numero es menor que 3")
        
#    case _ if num > 1:
#        print("tu numero es mayo que 1")

match num:
    case x if 3 > x > 1:
        print("tu numero es mayo que 1 y es menor que 3")
    
    case x if x < 3:
        print("tu numero es menor que 3")
     
    case x if x > 1:
        print("tu numero es mayo que 1")
        
booll = True

match booll:
    case x if x:
        print("True")
        
    case x if not x:
        print("False")
        
#Para combinar varios patrones (por ejemplo, “lista vacía” o “[0]”), 
#no uses el operador lógico or, sino el operador de patrones |

#¿Deberías sustituir if por match-case?
#No es necesario abandonar por completo if/elif/else. 
#Cada técnica tiene su espacio:
#usa if cuando tu lógica depende de comparaciones simples o de varias condiciones booleanas,
#y reserva match-case para cuando quieras hacer un pattern matching más estructurado y legible.

#Cuándo mantener if-elif-else
#Condiciones booleanas y comparaciones con operadores lógicos (==, !=, <, >, and, or).