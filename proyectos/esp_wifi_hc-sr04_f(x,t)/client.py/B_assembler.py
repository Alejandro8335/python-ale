import tkinter as tk
import asyncio
# modulos
from C_object_client import Clint
from D_object_graph import Graph

class Assembler():
    def __init__(self,ESP32_IP, ESP32_PORT):
        # communication channel
        self.queue = asyncio.Queue()
        # creating a Client object
        self.Clint = Clint(ESP32_IP, ESP32_PORT,self.queue)
        # creating a Graph object
        self.Graph = Graph(self.queue)
        # creating a Tk object
    
    async def Root_open(self):
        # creating rood and set the rood
        root = tk.Tk()
        root.title("Client esp32s")
        root.geometry("200x100")
        
        # creating label
        label_clint = tk.Label(root,font=("arial",12,"bold"))
        label_clint.grid(row=0, column=0, columnspan=2, sticky="nsew")
        label_graph = tk.Label(root,font=("arial",12,"bold"))
        label_graph.grid(row=2, column=0, columnspan=2, sticky="nsew")
        
        # creating button
        list_btn = [("Connect",lambda: asyncio.ensure_future(self.Clint.Connect()),1,0),
                    ("Disconnect",self.Clint.Disconnect,1,1),
                    ("Graph open",self.Graph.Graph_open,3,0),
                    ("Graph close",self.Graph.Graph_close,3,1)]
        
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
    
    async def HC_SR04(self):
        await asyncio.gather(self.Clint.Recv_to_the_server(),self.Graph.Data_consumer())
        
    async def assembler(self):
        task_root = asyncio.create_task(self.Root_open())
        task_hcsr04 = asyncio.create_task(self.HC_SR04())

        done, pending = await asyncio.wait(
            [task_root, task_hcsr04],
            return_when=asyncio.FIRST_COMPLETED
        )

        # si Root_open terminó (ventana cerrada), cancelamos el resto
        if task_root in done and not self._running:
            for t in pending:
                t.cancel()
                try:
                    await t
                except asyncio.CancelledError:
                    pass