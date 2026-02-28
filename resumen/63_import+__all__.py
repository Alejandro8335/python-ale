# __init__.py marca una carpeta como paquete importable y actúa como punto de entrada del paquete: 
# se ejecuta la primera vez que importás el paquete y define qué nombres (atributos) tendrá ese paquete en tiempo de ejecución.

###############################################################################################################################
# ¿Qué hace?

# Marca la carpeta como paquete.

# Se ejecuta al primer import paquete.

# Define el namespace del paquete (qué atributos tiene paquete.nombre).

# Puede reexportar símbolos para que from paquete import X funcione.

###############################################################################################################################
# ¿Por qué importamos módulos dentro de __init__.py?

# Porque un paquete es un módulo: cuando hacés from paquete import Nombre, 
# Python busca paquete.Nombre en el objeto módulo paquete. Si __init__.py no crea ese atributo, 
# no existe. Importando dentro de __init__.py asignás esos nombres al módulo paquete.

###############################################################################################################################
# ¿Por qué eso funciona?

# Al ejecutar __init__.py, 
# Python crea el objeto módulo paquete. Cualquier asignación o import dentro de __init__.py añade atributos a ese objeto. 
# Por ejemplo from .modulo import Clase hace que paquete.Clase exista.

###############################################################################################################################
# 1. Import “normal” (simple) (es un import absoluto teoricamente pq import solo funciona import absoluto)

# import utils
# Cuándo: cuando el archivo que querés importar está en el mismo directorio que el script que ejecutás, o cuando es un módulo estándar de Python o instalado en site-packages.

# Código
# mi_proyecto/
# ├── main.py
# └── utils.py
# Desde main.py podés hacer import utils porque está en el mismo directorio.

# 2. Import absoluto

# from paquete.subpaquete.modulo import Clase
# Cuándo: cuando querés importar desde otro paquete o carpeta que ya está en sys.path.

# Uso típico: en el código principal (main.py) y en tests, porque es más claro y explícito.

# Código
# mi_proyecto/
# ├── app/
# │   └── main.py
# └── modulos/
#     ├── __init__.py
#     └── calculos.py
# Desde main.py:

# from modulos.calculos import Calculadora

# 3. Import relativo

# from .modulo import Clase
# from ..otro import funcion
# Cuándo: dentro de un paquete (es decir, cuando el archivo se importa como parte del paquete, no ejecutado directamente).

# Uso típico: en archivos internos del paquete y en __init__.py, porque permite referenciar módulos sin depender del nombre absoluto del paquete.

# Código
# mi_proyecto/
# ├── __init__.py
# ├── app/
# │   ├── __init__.py
# │   └── main.py
# └── modulos/
#     ├── __init__.py
#     └── calculos.py
# Dentro de app/__init__.py:

# from ..modulos import calculos

# Resumen rápido (regla práctica)
# Import normal → cuando no hay paquetes, solo archivos en el mismo directorio, o módulos estándar.

# Import absoluto → para el código principal y tests; claro y explícito, depende de sys.path.

# Import relativo → dentro de paquetes, especialmente en __init__.py o módulos internos; más portable, pero no funciona si ejecutás el archivo directamente.

# 👉 Una forma de pensarlo:

# Normal = “traigo algo que está al lado mío o en la librería estándar”.

# Absoluto = “traigo algo desde la raíz del proyecto o instalación, con su nombre completo”.

# Relativo = “traigo algo desde mi posición dentro del paquete, usando puntos para moverme”

###############################################################################################################################
# Python no importa desde el archivo, importa desde el programa que se ejecuta.

###############################################################################################################################
# ¿Qué tiene que ver __init__.py con estos imports?
# __init__.py define el namespace del paquete. Cuando hacés import paquete, 
# Python crea el objeto módulo paquete y ejecuta paquete/__init__.py. 
# Cualquier import o asignación dentro de __init__.py añade atributos a paquete. 
# Por eso si querés que from paquete import Nombre funcione, Nombre debe estar definido (o importado) en __init__.py. 

# Cómo se usan los imports en __init__.py:

# Reexportar símbolos (común):

# # paquete/__init__.py
# from .modulo_a import ClaseA
# from .modulo_b import funcion_b

# __all__ = ["ClaseA", "funcion_b"] 
# Esto permite from paquete import ClaseA.

# Exponer submódulos:

# # paquete/__init__.py
# from . import submodulo
# Esto permite import paquete.submodulo o from paquete import submodulo.

# Evitar cargas pesadas: si __init__.py importa todo, esas importaciones se ejecutan en el primer import paquete. Para paquetes grandes, 
# preferir lazy imports o exponer solo lo necesario

###############################################################################################################################
# Los imports relativos con puntos (. , .., ...) solo se pueden usar en la sintaxis from ... import ....

# Ejemplo válido:

# python
# from .modulo import Clase
# from ..paquete import calculos
# ¿Por qué no funcionan con import?
# Si escribís:

# python
# import .modulo   # ❌ ERROR
# Python lo rechaza porque la sintaxis de import espera un nombre absoluto (que esté en sys.path).
# El mecanismo de los puntos (.) es exclusivo de la forma from ... import ..., porque ahí Python sabe que estás pidiendo un import relativo dentro de un paquete.

# Un punto (.) → significa “el mismo paquete donde estoy”.
# Ejemplo:

# python
# from . import calculos
# → busca el módulo calculos.py en la misma carpeta que el archivo actual.
################
# from modulo import Clase (sin punto)
# Es un import absoluto.

# Python busca el módulo modulo en el sys.path (que incluye el directorio actual, librerías instaladas, etc.).

# Funciona aunque el archivo se ejecute directamente, siempre que modulo.py esté en el mismo directorio o en el sys.path.

# Es global: no depende de la posición del archivo dentro de un paquete.


# from .modulo import Clase (con punto)
# Es un import relativo.

# El punto (.) significa “buscá en la misma carpeta/paquete donde está este archivo”.

# Solo funciona si el archivo se ejecuta como parte de un paquete (ejemplo: python -m paquete.otro).

# Si ejecutás el archivo directamente (python otro.py), falla porque Python no sabe qué significa “.`”.


# Entonces, ¿buscan en el mismo lugar?
# Sí, en el caso más simple (cuando modulo.py está en la misma carpeta).
# El absoluto lo encuentra porque el directorio actual está en sys.path.
# El relativo lo encuentra porque “.`” apunta a la misma carpeta.

# Pero la diferencia está en el contexto:
# El absoluto depende de sys.path.
# El relativo depende de la posición del archivo dentro del paquete.

################
# Dos puntos (..) → significa “subir un nivel en la jerarquía de paquetes”.
# Ejemplo:

# python
# from ..modulos import calculos
# → sube un nivel (a la carpeta padre) y desde ahí entra en la carpeta modulos.

# Tres puntos (...) → subir dos niveles, y así sucesivamente.
# Ejemplo:

# python
# from ...otro_paquete import algo
# → sube dos niveles en la jerarquía de carpetas.
###############################################################################################################################
# ¿Qué es __all__ en Python?
# __all__ es una lista especial que se puede definir dentro de un módulo o paquete (por ejemplo en __init__.py) para controlar qué nombres se exportan cuando alguien hace:

# python
# from paquete import *
# ¿Qué hace exactamente?
# Si no definís __all__, Python exporta todos los nombres del módulo que no empiezan con _ (subrayado).

# Si definís __all__, Python solo exporta los nombres que están en esa lista.

# Ejemplo práctico
# Estructura:

# Código
# paquete/
# ├── __init__.py
# └── calculos.py
# calculos.py


# class Calculadora:
#     pass

# def funcion_interna():
#     pass

# __init__.py

# from .calculos import Calculadora, funcion_interna

# __all__ = ["Calculadora"]   # solo exporta Calculadora

# Uso:

# from paquete import *
# print(Calculadora)      # ✅ funciona
# print(funcion_interna)  # ❌ NameError

# ¿Por qué es útil?
# Define la API pública del paquete: decidís qué símbolos querés que los usuarios vean.

# Oculta detalles internos: funciones auxiliares o clases que no deberían usarse fuera del paquete.

# Hace más claro el código: quien importa sabe qué está “oficialmente” expuesto.


# Resumen rápido
# __all__ = lista de nombres que se exportan con from paquete import *.

# Sin __all__ → se exporta todo lo que no empieza con _.

# Con __all__ → se exporta solo lo que vos pongas en la lista.

# Se usa mucho en __init__.py para definir la API pública del paquete.

###############################################################################################################################
# como ejecutar un paquete

# Paso a paso
# python → estás diciendo “ejecutá el intérprete de Python”.

# -m → significa “ejecutá un módulo como script”.

# En vez de pasarle un archivo (python archivo.py), le pasás el nombre de un módulo o paquete.

# Python busca ese módulo en sys.path y lo ejecuta.

# snake.pc.main_snake_for_pc → es el nombre completo del módulo que querés ejecutar.

# snake es el paquete raíz.

# pc es un subpaquete dentro de snake.

# main_snake_for_pc es el archivo (módulo) dentro de pc.

# ¿Qué pasa internamente?
# Python busca la carpeta snake en el directorio actual o en sys.path.

# Encuentra snake/__init__.py → lo ejecuta y crea el paquete snake.

# Dentro de snake, busca el subpaquete pc → ejecuta snake/pc/__init__.py.

# Finalmente, carga y ejecuta el archivo snake/pc/main_snake_for_pc.py como si fuera el “script principal”.