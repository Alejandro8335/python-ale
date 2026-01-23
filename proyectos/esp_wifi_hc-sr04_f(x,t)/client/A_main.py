import asyncio
import tkinter as tk
from B_assembler import Assembler
from C_object_client import Client
from D_object_graph import Graph
import matplotlib.pyplot as plt

# communication channel
queue = asyncio.Queue()

# creating a Client object
ESP_IP = "192.168.100.219"
ESP_PORT = (8080)
client = Client(ESP_IP,ESP_PORT,queue)

# creating a Graph object
graph = Graph(queue)

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

# create Assembler object and set Assembler
assembler = Assembler(client,graph,queue,loop)

del queue
def tk_loop(assembler,root, label_Client, client ,graph,set_bts):
    try:
        if graph.open_state:
            graph.fig.canvas.draw_idle()
        if not plt.fignum_exists(1):
            set_bts["Graph close"].invoke()
        if client.connect_state:
            label_Client.config(text="connect")
        else:
            label_Client.config(text="disconnect")
    except tk.TclError:
        assembler._running = False
        return False
    if assembler._running:
        root.after(
            100,
            lambda: tk_loop(assembler, root, label_Client, client, graph, set_bts)
        )
def pump_asyncio(assembler, loop ,root):
    if not assembler._running:
        return True

    try:
        loop.call_soon(loop.stop)
        loop.run_forever()
    except RuntimeError:
        return False

    root.after(20, lambda: pump_asyncio(assembler, loop,root))
    
if __name__ == "__main__":
    root, set_bts, set_label, _ = assembler.Root_open()
    plt.ion()

    root.after(10,lambda:pump_asyncio(assembler,loop,root))
    root.after(
        100,
        lambda: tk_loop(
            assembler,
            root,
            set_label["label_Client"],
            client,
            graph,
            set_bts
        )
    )
    root.mainloop()