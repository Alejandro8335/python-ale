# assert condición, "mensaje opcional de error"
# Si la condición es True → el programa sigue normalmente.

# Si la condición es False → se lanza una excepción AssertionError.

# Podés agregar un mensaje para entender qué falló.

x = 5
assert x > 0, "x debe ser positivo"
print("Todo bien")

x = -3
assert x > 0, "x debe ser positivo"#es el texto
print("Todo bien")
