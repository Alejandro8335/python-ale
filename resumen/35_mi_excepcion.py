
#creando mi propia excepcion personalizada
class Miexcepcion(Exception):
    def __init__(self,err):
        print(f"el error es {err}")

#lanzando mi propia excepcion
#raise Miexcepcion("jajjajajajjajajajja")

#manejandola
try:
    raise Miexcepcion("jajjaajaj")
except:
    print("como vas a cometer ese error")