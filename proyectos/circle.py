# (x - h)**2 + (y - k)**2 = r**2
# 𝑥,𝑦 → Son las coordenadas de cualquier punto en el plano.
# ℎ,𝑘 → Son las coordenadas del centro del círculo.

# <= r**2 (todo el circulo)
# ≈ r**2 (borde del circulo)

# ⬜ → cuadrado vacío (blanco)

# ⬛ → cuadrado lleno (negro)

number_of_pixels = 21

x = 0
y = 0
# el menos uno es pq va de 0 a 40 🤦
x_center_circle = x + (number_of_pixels - 1) / 2
y_center_circle = y + (number_of_pixels - 1) / 2
radio = (number_of_pixels) / 2 -1 # -1 si no quiere llegar hasta los bordes

dibujar_linea = ""
for y_for in range(y,y + number_of_pixels):
    for x_for in range(x,x + number_of_pixels):
        if (x_for - x_center_circle)**2 + (y_for - y_center_circle)**2 < (radio)**2:
            dibujar_linea += "⬜"
        else:
            dibujar_linea += "⬛"
    print(dibujar_linea)
    dibujar_linea = ""