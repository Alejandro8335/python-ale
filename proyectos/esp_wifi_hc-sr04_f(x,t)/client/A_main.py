import asyncio
import tkinter as tk
from B_assembler import Assembler
from C_object_client import Client
from D_object_graph import Graph

# communication channel
queue = asyncio.Queue()

# creating a Client object
ESP_IP = "192.168.100.219"
ESP_PORT = (8080)
client = Client(ESP_IP,ESP_PORT,queue)

# creating a Graph object
graph = Graph(queue)

# create Assembler object and set Assembler
assembler = Assembler(client,graph,queue)

if __name__ == "__main__":
    root , _ , _ , _ = assembler.Root_open()
    # Integrate Asyncio with Tkinter
    async def Root_update():
        while assembler._running:
            try:
                root.update_idletasks()
            except tk.TclError:
                # ventana destruida
                break
            await asyncio.sleep(0.01)
    asyncio.run(Root_update())