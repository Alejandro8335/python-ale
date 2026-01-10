import tkinter as tk
import asyncio
import time as tm
# modulos

class Assembler:
    def __init__(self,Client,Graph,queue):
        # Client object
        self.Clint = Client
        # Graph object
        self.Graph = Graph
        self.queue = queue
    def Root_open(self):
        # creating rood and set the rood
        root = tk.Tk()
        root.title("Client esp32s")
        root.geometry("300x200")
        
        entry = tk.Entry(root,font=("arial",12,"bold"))
        entry.grid(row=5, column=0, columnspan=2, sticky="nsew")
        entry.insert(0,"send to server")
        # creating label
        label_clint = tk.Label(root,font=("arial",12,"bold"),text="disconnect")
        label_clint.grid(row=0, column=0, columnspan=2, sticky="nsew")
        label_graph = tk.Label(root,font=("arial",12,"bold"),text="close")
        label_graph.grid(row=2, column=0, columnspan=2, sticky="nsew")
        
        set_label = {label_clint,label_graph}
        # creating button
        list_btn = [("Connect",lambda: asyncio.get_event_loop().create_task(self.Assembler_connect(label_clint,root)),1,0,1),
                    ("Disconnect",lambda: self.Assembler_disconnect(label_clint),1,1,1),
                    ("Graph open",lambda:self.Assembler_open_graph(label_graph),3,0,1),
                    ("Graph close",lambda:self.Assembler_close_graph(label_graph),3,1,1),
                    ("send",lambda:self.Assembler_send_to_serve(entry),6,0,2)]
        
        set_bts = {}
        for text_ , command_ , row_,column_ ,columnspan_ in list_btn:
            btn = tk.Button(root,text=text_,command=command_)
            btn.grid(row=row_,column=column_,sticky="nsew",columnspan=columnspan_)
            set_bts[text_] = btn
            
        # expandable columns and rows
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for j in range(2):
            root.grid_columnconfigure(j, weight=1)
        
        self._running = True
        root.protocol("WM_DELETE_WINDOW",self.On_closing)

        return root ,set_bts ,set_label ,entry
    
    async def Assembler_connect(self, label_clint,root):
        await self.Clint.Connect()
        if self.Clint.connect_state and not self.def_connect_state and self.second_window is False:
            asyncio.create_task(self.Clint.Recv_to_the_server())
            label_clint.config(text="connect")
            second_window = tk.Toplevel(root)
            label_passwordstate = tk.Label(second_window)
            label_passwordstate.grid(row=0, column=0, sticky="nsew")
            entry_passwordstate = tk.Entry(second_window)
            entry_passwordstate.grid(row=0, column=1, sticky="nsew")
            entry_passwordstate.insert("Enter the password")
            button_passwordstate = tk.Button(second_window,text="send",command=lambda: self.Assembler_send_to_serve(entry_passwordstate))
            button_passwordstate.grid(row=0,column=2,sticky="nsew")
            self.second_window = True
            for _ in range(6100):
                try:
                    data = await asyncio.wait_for(self.queue.get(),timeout=2)
                except TimeoutError:
                    pass
                if data is True:
                    asyncio.create_task(self.Graph.Data_consumer())
                    second_window.destroy()
                    self.second_window = False
                elif data is False:
                    if self.Clint.def_recv_state:
                        await asyncio.create_task(self.queue.put(None))
                    second_window.destroy()
                    self.second_window = False
                    label_clint.config(text="disconnect")
                elif data == "Incorrect password":
                    label_passwordstate.config(text="Incorrect password")
                tm.sleep(0.01)
            
            
    def Assembler_disconnect(self,label_clint):
        self.Clint.Disconnect()
        label_clint.config(text="disconnect")
        
    def Assembler_open_graph(self,label_graph):
        self.Graph.Graph_open()
        label_graph.config(text="open")
        
    def Assembler_close_graph(self,label_graph):
        self.Graph.Graph_close()
        label_graph.config(text="close")
    
    def Assembler_send_to_serve(self,entry):
        if self.Clint.def_connect_state:
            asyncio.create_task(self.Clint.Send_to_the_server(entry.get()))
    def On_closing(self):
        self._running = False
        if self.Clint.def_connect_state:
            self.Clint.Disconnect()
        if self.Clint.def_recv_state:
            asyncio.create_task(self.queue.put(None))