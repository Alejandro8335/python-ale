#OPERADORES

#suma y resta(+ y -)
suma= 12+5
resta=12 - 5

#multi y division(* y /)
multi= 12 * 5
divicion= 12 / 5 #devuelve un dato float

#potenciacion(**)
exponente= 12**5

#divicion baja(//)
divicion_baja = 12//5#devuelve un entero redondiado asi abajo 

#resto/moludo
resto= 12 % 5 #devuelve 2
#es una divicion pero retorna el resto
#en otras palabras resta todas las veces posibles y retorna lo que ya no puede restar
#en este caso resta 2 veces 5 y retorna 2 pq ya no puede restar mas veces el 5 
#(obviamente sin que sea negativo(pq es una divicion))

resto2 = -12 % 5 # devuelve 3
#siempre devuelve un resultado con el mismo signo que el divisor
#-12 dividido por 5 da -3 con un resto de 3.
#Porque -3 * 5 = -15, y -12 - (-15) = 3.

######
#OPERADORES DE COMPARACION (devuelven true or false)
 
igual_que=  5 == 6 #false
# != Compara si dos valores son distintos
distinto_que = 5 != 6 #true

mayor_que = 5>6 #false

menor_que = 5<6 #true

mayor_o_igual= 5>=6 #false

menor_o_igual= 5 <= 6 #true

(a := 5) == 5   # guarda 5 en a y además compara si es igual a 5
# lo pone en la caja y además lo muestra/retorna en ese mismo momento dentro de la expresión.
######
# OPERADORES LOGICOS

# and
resultado1= True and True # True
resultado2= False and True # False
resultado3=True and False # False
resultado4= False and False # False
# or
resultado5= True or True # True
resultado6= False or False # False
resultado7= True or False # True 
resultado8= False or True # True
# not
resultado9=not True # False
resultado10=not False # True

# BIT A BIT
#and(&)
resultado1= True & True # True
resultado2= False & True # False
resultado3=True & False # False
resultado4= False & False # False
#or(|)
resultado5= True | True # True
resultado6= False | False # False
resultado7= True | False # True 
resultado8= False | True # True
# xor(^)
resultado11 = True ^ True # False
resultado12 = False ^ True # True
resultado13 = True ^ False # True
resultado14 = False ^ False # False

# not(~)
# invierte bits (cambia 1→0 y 0→1)
resultado15 = ~5 # -6
resultado16 = ~0 # -1
resultado17 = ~-1 # 0
resultado18 = ~-7 # 6
resultado19 = ~True # -2
resultado20 = ~False # -1

# desplazamiento
# x * (2**n)
resultado21 = 5 << 1 # 10
resultado22 = 5 << 2 # 20
# x // (2**n)
resultado23 = 20 >> 1 # 10
resultado24 = 20 >> 2  # 5

#reglas de preferencia,siempre es recomendable usar paréntesis:
# comparaciones (<, >, <=, >=, ==, !=, is, in, etc)
# bit a bit
# not
# and
# or

print(resultado20)

# +=, -=, *=, /=, //=, %=, **=, &=, |=, ^=, <<=, >>=
x = 10
x -= 3  # Equivalente a x = x - 3
# print(x)  # Resultado: 7

x = 10
x += 3  # Equivalente a x = x + 3
# print(x)  # Resultado: 13

a = 6      # binario: 110
a &= 3     # binario: 011
# print(a)   # resultado: 2 (binario 010)

a = 6      # binario: 110
a |= 3     # binario: 011
# print(a)   # resultado: 7 (binario 111)

a = 6      # binario: 110
a ^= 3     # binario: 011
# print(a)   # resultado: 5 (binario 101)

a = 3      # binario: 011
a <<= 2    # desplaza 2 bits a la izquierda → 1100
# print(a)   # resultado: 12

a = 12     # binario: 1100
a >>= 2    # desplaza 2 bits a la derecha → 0011
# print(a)   # resultado: 3

# raices :
# x ** (1/n)
def raiz(num,num_raiz):
    return num ** (1/num_raiz)

# print(raiz(16,2)) #4
# print(raiz(27,3)) #3.0