import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import random

x_data = []
y_data = []

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

# fig, ax = plt.subplots() 
#🔹 Crea una figura (fig) y un eje (ax) donde se dibujará el gráfico. 
#🔹 Es la base sobre la que se construye el gráfico.

# line, = ax.plot([], [], lw=2) 
#🔹 Crea una línea vacía que luego se irá actualizando con datos. 
#🔹 lw=2 significa "line width" (grosor de la línea). 
#🔹 El , después de line es importante: ax.plot() devuelve una lista de líneas, y esto extrae la primera.

start_time = time.time()
def Update_grafico(Frame):
    global x_data,y_data,start_time
    x_data.append(time.time()-start_time)
    y_data.append(random.uniform(0, 10))

    line.set_data(x_data, y_data)
    #line.set_data(...) 🔹 Actualiza la línea con los nuevos datos acumulados.
    ax.relim()
    #ax.relim()
    #🔹 Recalcula los límites del gráfico (mínimos y máximos) según los nuevos datos.
    ax.autoscale_view()
    #ax.autoscale_view()
    # 🔹 Ajusta automáticamente la vista del gráfico para que se vea todo el contenido.
    return line,

ani = FuncAnimation(fig, Update_grafico)
# interval=750(para que tarde en reiniciarse(esta en milisegundos))

plt.title("Gráfico en tiempo real")
plt.xlabel("Tiempo")
plt.ylabel("Valor")
plt.show()