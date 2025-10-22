import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from time import time

class Graph():
    def __init__(self,Queue_obj):
        self.queue = Queue_obj
        # axis (x) y (y),x is time dependent variable
        self.X_data = []
        self.Y_data = []
        # set the graph
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], lw=2)
        plt.title("Gráfico de distancia")
        plt.xlabel("Tiempo")
        plt.ylabel("Valor")
        # start time and data the axis y
        self.start_time = time()
        
        # graph
        self.animacion = FuncAnimation(self.fig, self.Update_frame,interval=200)

        self.open_state = False
        
    def Graph_open(self):
        if not self.open_state:
            plt.show(block=False)
            self.open_state = True
    
    def Graph_close(self):
        if self.open_state:
            plt.close(self.fig)
            self.open_state = False
    
    def Update_frame(self,frame):
        self.line.set_data(self.X_data, self.Y_data)
            
        self.ax.relim()
        self.ax.autoscale_view()
        return self.line,
    
    async def Data_consumer(self):
        while True:
            data = await self.queue.get()
            if data is None:  # señal de fin
                break
            self.X_data.append(time()-self.start_time)
            self.Y_data.append(float(data))