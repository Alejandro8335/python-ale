import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from time import time

class Graph():
    def __init__(self,Queue_obj):
        self.queue = Queue_obj
        # axis (x) y (y),x is time dependent variable
        self.X_data = []
        self.Y_data = []
        # start time and data the axis y
        self.open_state = False
        self.data_consumer_state = False
    def Graph_open(self):
        try:
            if not self.open_state:
                self.fig, self.ax = plt.subplots()
                self.line, = self.ax.plot([], [], lw=2)
                plt.title("Gráfico de distancia")
                plt.xlabel("Tiempo")
                plt.ylabel("Valor")
                self.animacion = FuncAnimation(self.fig, self.Update_frame, interval=200, cache_frame_data=False)
                plt.show(block=False)
                self.open_state = True
            return True
        except Exception as e:
            print(e)
            return False
    def Graph_close(self):
        try:
            if self.open_state:
                plt.close(self.fig)
                self.open_state = False
            return True
        except Exception as e:
            print(e)
            return False
    def Update_frame(self,frame):
        self.line.set_data(self.X_data, self.Y_data)
            
        self.ax.relim()
        self.ax.autoscale_view()
        return self.line,
    
    async def Data_consumer(self):
        if not self.data_consumer_state:
            self.data_consumer_state = True
            self.start_time = time()
            try:
                while self.data_consumer_state:
                    try:
                        data = await self.queue.get()
                        print(data)
                        if data is None:  # señal de fin
                            return True
                        else:
                            try:
                                data = round(float(data),5)
                            except ValueError:
                                print("Dato no numérico ignorado:", data)
                            else:
                                self.X_data.append(time()-self.start_time)
                                self.Y_data.append(data)
                    except Exception as e:
                        self.data_consumer_state = False
                        print(e)
            finally:
                self.data_consumer_state = False