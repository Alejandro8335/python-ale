import tkinter as tk
import asyncio
# modulos

class Assembler:
    def __init__(self,Client,Graph,queue,loop):
        # Client object
        self.Client = Client
        # Graph object
        self.Graph = Graph
        self.queue = queue
        self.second_window_state = False
        self.loop = loop
    def Root_open(self):
        # creating rood and set the rood
        root = tk.Tk()
        root.title("Client esp32s")
        root.geometry("300x200")
        
        entry = tk.Entry(root,font=("arial",12,"bold"))
        entry.grid(row=5, column=0, columnspan=2, sticky="nsew")
        entry.insert(0,"send to server")
        # creating label
        label_Client = tk.Label(root,font=("arial",12,"bold"),text="disconnect")
        label_Client.grid(row=0, column=0, columnspan=2, sticky="nsew")
        label_graph = tk.Label(root,font=("arial",12,"bold"),text="close")
        label_graph.grid(row=2, column=0, columnspan=2, sticky="nsew")
        
        set_label = {"label_Client":label_Client,"label_graph":label_graph}
        
        set_bts = {}
        
        for text_ , command_ , row_,column_ ,columnspan_ in [
        ("Connect",lambda: self.loop.create_task(self.Assembler_connect(label_Client,root)),1,0,1),
        ("Disconnect",lambda: self.Assembler_disconnect(label_Client),1,1,1),
        ("Graph open",lambda:self.Assembler_open_graph(label_graph),3,0,1),
        ("Graph close",lambda:self.Assembler_close_graph(label_graph),3,1,1),
        ("send",lambda:self.Assembler_send_to_serve(entry),6,0,2)]:
            btn = tk.Button(root,text=text_,command=command_)
            btn.grid(row=row_,column=column_,sticky="nsew",columnspan=columnspan_)
            set_bts[text_] = btn
            
        # expandable columns and rows
        [root.grid_rowconfigure(i, weight=1) for i in range(6)]
        [root.grid_columnconfigure(i, weight=1) for i in range(2)]
        
        self._running = True
        self.root = root
        root.protocol("WM_DELETE_WINDOW",self.On_closing)

        return root ,set_bts,set_label ,entry
    
    async def Assembler_connect(self, label_Client,root):
        if await self.Client.Connect() is True:
            if self.second_window_state is False:
                self.loop.create_task(self.Client.Recv_to_the_server())
                self.second_window_state = True
                label_Client.config(text="connect")
                second_window = tk.Toplevel(root)
                second_window.geometry("50x100")
                
                label_passwordstate = tk.Label(second_window)
                label_passwordstate.grid(row=0, column=0, sticky="nsew")
                
                entry_password = tk.Entry(second_window)
                entry_password.grid(row=1, column=0, sticky="nsew")
                entry_password.insert(0,"Enter the password")
                
                button_password = tk.Button(second_window,text="send",command=lambda: self.Assembler_send_to_serve(entry_password))
                button_password.grid(row=2,column=0,sticky="nsew")
                
                [second_window.grid_rowconfigure(i, weight=1) for i in range(3)]
                second_window.grid_columnconfigure(0, weight=1)
                
                self.set_second_window = {name: elem for name, elem in zip(("label_passwordstate", "entry_password", "button_password"), (label_passwordstate, entry_password, button_password))}
                while self.Client.connect_state is True:
                    try:
                        data = await asyncio.wait_for(self.queue.get(),timeout=2)
                    except asyncio.TimeoutError:
                        data = None
                    except Exception as e: print(e)
                    if data is True:
                        self.loop.create_task(self.Graph.Data_consumer())
                        second_window.destroy()
                        self.second_window_state = False
                        break
                    elif data is False:
                        self.Client.connect_state = False
                        label_Client.config(text="disconnect")
                        second_window.destroy()
                        self.second_window_state = False
                        break
                    elif data == "Incorrect password":
                        label_passwordstate.config(text="Incorrect password")
                    await asyncio.sleep(0.01)
                del self.set_second_window
            
    def Assembler_disconnect(self,label_Client):
        if self.Client.Disconnect() is True:
            label_Client.config(text="disconnect")

    def Assembler_open_graph(self,label_graph):
        if self.Graph.Graph_open() is True:
            label_graph.config(text="open")
        
    def Assembler_close_graph(self,label_graph):
        if self.Graph.Graph_close() is True:
            label_graph.config(text="close")
    
    def Assembler_send_to_serve(self,entry):
        if self.Client.connect_state:
            self.loop.create_task(self.Client.Send_to_the_server(entry.get()))
            
    def On_closing(self):
        self._running = False
        if self.Client.connect_state:
            self.Client.Disconnect()
        self.Client.def_recv_state = False
        self.Graph.Graph_close()
        self.Graph.data_consumer_state = False
        self.root.after(0, self.root.destroy)