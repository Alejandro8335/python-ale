# En Python, dentro de unittest.mock, el método mock_add_spec se usa para añadir una 
# especificación (spec) a un mock ya existente.

# 🔧 ¿Qué significa "spec"?
# Un spec es una referencia a una clase, función u objeto real.

# Cuando un mock tiene un spec, solo permite atributos y métodos que existen en ese objeto real.

# Esto ayuda a evitar errores en las pruebas, porque si intentas llamar a un método que no 
# existe en el objeto original, el mock lanzará un AttributeError.

from unittest.mock import Mock

class API:
    def get(self): pass
    def post(self): pass

# Creamos un mock sin restricciones
m = Mock()

# Le añadimos un spec basado en la clase API
m.mock_add_spec(API)

# Ahora solo acepta métodos de API
m.get()   # ✅ permitido
m.post()  # ✅ permitido

m.delete()  # ❌ AttributeError: Mock object has no attribute 'delete'

##################################################################################
class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def Disconnect(self):
        print("Desconectado")
        

# Creamos una instancia real de Client
real_client = Client("localhost", 8080)

# Creamos el mock y le damos el spec de esa instancia
client = Mock()
client.mock_add_spec(real_client)

# Ahora podés llamar métodos sin que te pida 'self'
client.Disconnect()
print(client.Disconnect.called)  # True
