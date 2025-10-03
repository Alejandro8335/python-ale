
#import * importamos todo
#as renombre el modulo o la funcion 
import modulos_1 as m_saludar

saludo = m_saludar.saludar("ale")
print(saludo)


from modulos_1 import saludar#con la , podes inportar mas funciones

saludo = saludar("ale1")
print(saludo)

#para ver las propiedades y metodos de el naspace
print(dir(m_saludar))

#accedemos al nombre de este modulo llamado
print(m_saludar.__name__)



# diferencias entre modulos,paquetes y librerias

# Si vos creás un archivo mis_funciones.py → eso ya es un módulo propio.

# Si armás una carpeta mi_paquete/ con varios modulos organizados → eso es un paquete.

# Cuando instalás algo con pip install ... (ej. pandas) → eso es una librería 
# (que internamente puede estar hecha de paquetes y módulos).