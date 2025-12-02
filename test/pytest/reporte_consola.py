# Pytest solo detecta funciones cuyo nombre empieza con test o Test
# Funciones → nombre empieza con test en minúsculas.

# Clases → nombre empieza con Test con T mayúscula.

#######################################################
# Si, por ejemplo, tu función suma devolviera mal un resultado, verías algo como:

# Código
# .F..
# ======================================================================
# FAIL: test_suma_basica (__main__.TestCalc)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "test_calc.py", line 8, in test_suma_basica
#     self.assertEqual(suma(2, 3), 5)
# AssertionError: 6 != 5

# ----------------------------------------------------------------------
# Ran 4 tests in 0.002s

# FAILED (failures=1)
# El F marca un fallo en ese test.

# AssertionError: 6 != 5 te muestra exactamente qué valores no coincidieron.

# Al final, FAILED (failures=1) indica cuántos tests fallaron.


#######################################################
# Ejecutar con más verbosidad

# pytest -v
# Esto muestra cada test y, en los skipped, agrega el motivo.

# Ejecutar con reporte detallado de skips

# pytest -rs
# La opción -rs significa report skipped tests.

# Con -s pytest no captura stdout y vas a ver los print en la salida. 
# También podés usar pytest --capture=no

# -W ves los warning ir a F_filterwarning.py para entender mejor

# -x Si querés parar en el primer error:
# pytest -v -rs -s -W always "C:\Users\gabri\OneDrive\Desktop\ALE\python-ale\test\pytest\@pytest.mark\def\.py"

#######################################################
# Si querés correr funcion sin el nombre test, tenés que hacer:

# pytest -k nombre_def
#######################################################
# Ejecutar solo los slow de todo el proyecto:

# pytest -m slow
# Ejecutar todo menos los slow en todo el proyecto:

# pytest -m "not slow"

# se pueden usar operadores logicas