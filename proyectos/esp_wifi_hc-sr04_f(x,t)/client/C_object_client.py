import asyncio
import socket
#sock_connect, sock_sendall, sock_recv → son las versiones asincrónicas correctas.
class Client():
    def __init__(self,ESP32_IP, ESP32_PORT,Queue_obj):
        self.IP = ESP32_IP
        self.PORT = ESP32_PORT
        self.connect_state = False
        self.send_lock = asyncio.Lock() # es la forma más limpia y segura de serializar accesos a un recurso compartido
        self.queue = Queue_obj # cola para mensajes recibidos
        self.def_connect_state = False
        self.def_recv_state =  False
    # def the Connect and Disconnect
    async def Connect(self):
        try:
            if not self.connect_state and not self.def_connect_state:
                self.def_connect_state = True
                # create a socket object and set socker
                self.socker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socker.setblocking(False)
                loop = asyncio.get_running_loop()
                await loop.sock_connect(self.socker, (self.IP, self.PORT))
                self.connect_state = True
                self.def_connect_state = False
                print("connect")
        except Exception as e:
            self.def_connect_state = False
            print(e)
            
    def Disconnect(self):
        try:
            if self.connect_state:
                self.socker.close()
                self.connect_state = False
                print("disconnect")
        except Exception as e:
            print(e)
        
    # def the Send and Recv
    async def Send_to_the_server(self,msj):
        try:
            loop = asyncio.get_running_loop()
            async with self.send_lock: 
                await loop.sock_sendall(self.socker, msj.encode())
        except Exception as e:
            print(e)
            self.connect_state = False
        
    async def Recv_to_the_server(self):
        loop = asyncio.get_running_loop()
        if not self.def_recv_state:
            self.def_recv_state = True
            print("recv ok")
            try:
                while self.connect_state and self.def_recv_state:
                    try:
                        data = await loop.sock_recv(self.socker, 64)
                        if not data: # pq quiere decir que el server cerro la conexión 
                            await self.queue.put(None)  # señal de fin
                            self.connect_state = False
                            self.def_recv_state = False
                            break
                        list_data = data.decode().split()
                        for _data_ in list_data:
                            await self.queue.put(_data_.strip())
                        # no puedo usar return pq me saca del bucle
                    except Exception as e:
                        print(e)
                        self.connect_state = False
                        self.def_recv_state = False
            finally:
                self.def_recv_state = False