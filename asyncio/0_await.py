# Pensá en await como “esperar en la fila”:

# Si la función es async → te da un ticket y tenés que esperar (await).

# Si la función es normal → te da el resultado en el momento, no hay que esperar.

# Si creás una Task → es como pedir un turno y seguir haciendo otras cosas; 
# solo usás await cuando querés el resultado.

# con event loop
# Cuando hacés await algo(), tu corutina actual se pausa en ese punto y 
# no ejecuta lo que está debajo hasta que algo() termine.

# Pero el event loop no se detiene: mientras tu corutina espera, 
# el loop sigue corriendo otras tareas que ya estaban pendientes o que se vayan programando.