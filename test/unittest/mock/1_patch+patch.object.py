# patch
# Sirve para parchear un atributo (función, clase, objeto) dentro de un módulo durante el 
# alcance del test.

# Se usa como decorador o context manager.

# Cuando termina el test, el parche se revierte automáticamente.

# Ejemplo con patch como decorador

from unittest.mock import patch

# Supongamos que tenemos un módulo "servicio" con una función "obtener_datos"
@patch("servicio.obtener_datos")
def test_funcion(mock_obtener):
    mock_obtener.return_value = {"ok": True}
    resultado = mock_obtener()
    print(resultado)   # → {"ok": True}
    
# Ejemplo con patch como context manager

with patch("servicio.obtener_datos") as mock_obtener:
    mock_obtener.return_value = {"ok": True}
    print(mock_obtener())   # → {"ok": True}
    
############################################################################
# 🔹 patch.object
# Similar a patch, pero en lugar de dar la ruta completa (modulo.funcion), 
# se aplica directamente sobre un objeto/clase ya importado.

# Útil cuando ya tienes la referencia del objeto y quieres modificar uno de sus atributos.

# Ejemplo con patch.object

from unittest.mock import patch

class Servicio:
    def obtener_datos(self):
        return {"real": True}

# Parcheamos el método en la clase
with patch.object(Servicio, "obtener_datos", return_value={"mock": True}):
    s = Servicio()
    print(s.obtener_datos())   # → {"mock": True}
    
############################################################################

# ⚖️ Diferencia clave
# patch: se usa con la ruta completa "modulo.nombre".

# patch.object: se usa directamente sobre un objeto/clase ya importado.

############################################################################

# Mock/MagicMock: los usas cuando controlas la dependencia (la pasas como argumento).

# patch/patch.object: los usas cuando necesitas interceptar algo que el código ya importa/usa internamente, 
# sin modificarlo.