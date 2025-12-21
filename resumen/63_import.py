# 📁 Ejemplo práctico de estructura
# Supongamos esta estructura:

# Código
# mi_proyecto/
# │
# ├── app/
# │   ├── main.py
# │   └── utils.py
# │
# └── modulos/
#     └── calculos.py
# ✅ Desde main.py podés importar utils.py así:
# python
# import utils
# Porque está en el mismo directorio.

###################################################################################

# ❌ Pero NO podés importar calculos.py así nomás:
# python
# import calculos  # ERROR
# Porque está en otra carpeta que no es un paquete y no está en sys.path.

###################################################################################

# ✅ ¿Cómo hacer que una carpeta sea importable?
# Opción 1: Convertirla en paquete
# Agregá un archivo vacío:

# modulos/
#     __init__.py
#     calculos.py
# Ahora podés hacer:

# from modulos import calculos
# Opción 2: Usar imports relativos (solo dentro de paquetes)
# Si app y modulos están dentro de un paquete mayor:

# Código
# mi_proyecto/
#     __init__.py
#     app/
#         __init__.py
#         main.py
#     modulos/
#         __init__.py
#         calculos.py
# Entonces desde main.py:

# from ..modulos import calculos