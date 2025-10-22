import tkinter as tk
import asyncio
# modulos
from C_object_client import Clint
from D_object_graph import Graph

class Assembler():
    def __init__(self,socker_obj,ESP32_IP, ESP32_PORT):
        # communication channel
        self.queue = asyncio.Queue()
        # creating a Client object
        self.Clint = Clint(socker_obj,ESP32_IP, ESP32_PORT,self.queue)
        # creating a Graph object
        self.Graph = Graph(self.queue)
        
    async def Root(self):
        # creating rood and set the rood
        root = tk.Tk()
        root.title("Mi primera ventana")
        root.geometry("400x400")
        
        # creating label
        label =