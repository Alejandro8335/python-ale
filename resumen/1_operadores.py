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

#OPERADORES DE COMPARACION (devuelven true or false)
 
igual_que=  5 == 6 #false

distinto_que = 5 != 6 #true

mayor_que = 5>6 #false

menor_que = 5<6 #true

mayor_o_igual= 5>=6 #false

menor_o_igual= 5 <= 6 #true

#OPERADORES LOGICOS

#and(&)
 
resultado1= True & True #true
resultado2= False & True #false
resultado3=True & False #false
resultado4= False & False #false
#or(|)
resultado5= True | True #true
resultado6= False | False #false
resultado7= True | False #true 
resultado8= False | True #true
#not
resultado9=not True #false
resultado10=not False #true

#reglas de preferencia,siempre es recomendable usar paréntesis:
# not
# and
# or

print(resultado10)

#MAS
x = 10
x -= 3  # Equivalente a x = x - 3
print(x)  # Resultado: 7

x = 10
x += 3  # Equivalente a x = x + 3
print(x)  # Resultado: 13
