machine.reset()  
Reinicia el dispositivo inmediatamente.

machine.soft_reset()  
Reinicia el intérprete de MicroPython sin reiniciar el hardware completo. Útil para limpiar el entorno.

machine.reset_cause()  
Devuelve la causa del último reinicio (por ejemplo: encendido, botón de reset, watchdog, etc.).

machine.freq([hz])  
Obtiene o establece la frecuencia de la CPU.

Sin argumentos → devuelve frecuencia actual.

Con argumento → ajusta frecuencia.

machine.idle()  
Pone la CPU en modo inactivo (reduce consumo, pero sigue ejecutando interrupciones).

machine.sleep()  
Suspende el dispositivo en modo bajo consumo (menos profundo que deepsleep).

machine.deepsleep([ms])  
Suspende el dispositivo en modo de consumo mínimo.

Opcionalmente se puede pasar un tiempo en milisegundos para que despierte automáticamente.

machine.unique_id()  
Devuelve un identificador único del dispositivo (por ejemplo, dirección MAC o ID de chip).

machine.rng()  
Genera un número aleatorio usando el generador de hardware (si está disponible).

machine.bootloader()  
Entra en modo bootloader (dependiendo del hardware, útil para flashear firmware).