import tkinter as tk
import asyncio
# modulos
from C_object_client import Clint
from D_object_graph import Graph

class Assembler:
    def __init__(self,ESP32_IP, ESP32_PORT):
        # communication channel
        self.queue = asyncio.Queue()
        # creating a Client object
        self.Clint = Clint(ESP32_IP, ESP32_PORT,self.queue)
        # creating a Graph object
        self.Graph = Graph(self.queue)
    
    async def Root_open(self):
        # creating rood and set the rood
        root = tk.Tk()
        root.title("Client esp32s")
        root.geometry("200x100")
        
        # creating label
        label_clint = tk.Label(root,font=("arial",12,"bold"),text="disconnect")
        label_clint.grid(row=0, column=0, columnspan=2, sticky="nsew")
        label_graph = tk.Label(root,font=("arial",12,"bold"),text="close")
        label_graph.grid(row=2, column=0, columnspan=2, sticky="nsew")
        
        # creating button
        list_btn = [("Connect",lambda: asyncio.get_event_loop().create_task(self.Assembler_connect(label_clint)),1,0),
                    ("Disconnect",lambda: self.Assembler_disconnect(label_clint),1,1),
                    ("Graph open",lambda:self.Assembler_open_graph(label_graph),3,0),
                    ("Graph close",lambda:self.Assembler_close_graph(label_graph),3,1)]
        
        for text_ , command_ , row_,column_ in list_btn:
            btn = tk.Button(root,text=text_,command=command_)
            btn.grid(row=row_,column=column_,sticky="nsew")
            
        # expandable columns and rows
        for i in range(4):
            root.grid_rowconfigure(i, weight=1)
        for j in range(2):
            root.grid_columnconfigure(j, weight=1)
        
        self._running = True
        root.protocol("WM_DELETE_WINDOW",
              lambda: (setattr(self, "_running", False),
                       self.Clint.Disconnect(),
                       asyncio.create_task(self.queue.put(None))))

        # Integrate Asyncio with Tkinter
        while self._running:
            try:
                root.update()
            except tk.TclError:
                # ventana destruida
                break
            await asyncio.sleep(0.01)
    async def Assembler_connect(self, label_clint):
        await self.Clint.Connect()
        if self.Clint.connect_state:
            asyncio.create_task(self.Clint.Recv_to_the_server())
            asyncio.create_task(self.Graph.Data_consumer())
            label_clint.config(text="connect")
    def Assembler_disconnect(self,label_clint):
        self.Clint.Disconnect()
        label_clint.config(text="disconnect")
    def Assembler_open_graph(self,label_graph):
        self.Graph.Graph_open()
        label_graph.config(text="open")
    def Assembler_close_graph(self,label_graph):
        self.Graph.Graph_close()
        label_graph.config(text="close")