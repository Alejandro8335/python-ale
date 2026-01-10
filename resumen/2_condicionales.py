#CONDICIONALES

#if true:
  #accion se ejecuta 

#if false:
  #accion no se ejecuta 
  
edad= 16
  
if edad >= 18:
    print("podes pasar")
else:
    print("no podes pasar")

#if anidados 
ingreso_mensual= 81000
gasto_mensual=80000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas gastando mucho")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("estas bien")
    else :
        print("te estas quedando pobre")

           
#if not x:    # se ejecuta si x es False

 
# x = 1

# if x == True:     # Falso, porque 1 no es exactamente True (aunque se comporte como tal)
# if x:             # Verdadero, porque 1 es "truthy"

#truthy
#falsy

#if x: → Esto evalúa si x es truthy, es decir, cualquier valor que Python considere como verdadero: 
#        números distintos de cero, listas no vacías, strings no vacíos, etc.


#if / elif

#Estructura	|¿Evalúa múltiples condiciones si todas son verdaderas?
#Varios if	|✅ Sí
#if + elif	|❌ No, solo la primera verdadera

if 1:
    print("si")
 
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # True, porque tienen el mismo contenido
print(a is b)   # False, porque son listas distintas en memoria

x = True
y = True

print(x == y)   # True, mismo valor
print(x is y)   # True, misma identidad (es el mismo objeto)

x = None
y = None

print(x == y)   # True
print(x is y)   # True, ambos apuntan al único objeto None
