# Códigos ANSI para colores básicos
rojo = "\033[31m"
verde = "\033[32m"
azul = "\033[34m"
reset = "\033[0m"  # vuelve al color normal

print(rojo + "Este texto es rojo" + reset)
print(verde + "Este texto es verde" + reset)
print(azul + "Este texto es azul" + reset)
#el + es pq son variables si no son necesarios

#Qué pasa aquí:
# \033[ inicia la secuencia ANSI (el número 33 es el carácter escape en octal).

# El número (31, 32, 34, etc.) define el color.

# RESET devuelve el color a la configuración normal del terminal.


Negro = "\033[30m"
Rojo = "\033[31m"
Verde = "\033[32m"
Amarillo = "\033[33m"
Azul = "\033[34m"
Magenta = "\033[35m"
Cian = "\033[36m"
Blanco = "\033[37m"
Normal = "\033[0m"

#convinando colores
print("\033[33mhola \033[32mmundo\033[0m")

# \1, \2, \3 → son caracteres de control ASCII (códigos 1, 2 y 3).

# ASCII 1 → ☺

# ASCII 2 → ☻

# ASCII 3 → ♥

# ASCII 4 → ♦

# ASCII 5 → ♣

# ASCII 6 → ♠

#cada numero devuelve un caracter diferente
print("\5")