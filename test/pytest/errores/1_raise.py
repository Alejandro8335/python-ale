# Qué hace: la palabra reservada raise crea y lanza una excepción; si no se captura, interrumpe la ejecución y 
# (en tests) hará que la prueba falle (a menos que uses pytest.raises)

# Cuándo usar: cuando detectas un estado inválido en tu lógica y quieres que el llamador lo maneje. 
# También para crear excepciones personalizadas.

import os

def abrir_archivo(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"No existe: {path}")
