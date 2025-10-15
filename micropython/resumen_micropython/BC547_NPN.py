#    _______
#   |       | ← parte plana
#   |_______|
#    | | |
#    | | |
#    C B E

# B = Base (izquierda)

# C = Colector (centro)

# E = Emisor (derecha)

from machine import Pin

button = Pin(12,Pin.OUT)

led = Pin(27,Pin.OUT)

while True:
    button.value(1)
    led.value(1)