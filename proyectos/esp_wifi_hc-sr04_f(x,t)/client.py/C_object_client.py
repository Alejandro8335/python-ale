import asyncio

#sock_connect, sock_sendall, sock_recv → son las versiones asincrónicas correctas.
class Clint():
    def __init__(self,socker_obj,ESP32_IP, ESP32_PORT,Queue_obj):
        self.socker = socker_obj
        self.IP = ESP32_IP
        self.PORT = ESP32_PORT
        self.connect_state = False
        self.send_lock = asyncio.Lock() # es la forma más limpia y segura de serializar accesos a un recurso compartido
        self.queue = Queue_obj # cola para mensajes recibidos
        
    # def the Connect and Disconnect
    async def Connect(self):
        try:
            if not self.connect_state:
                loop = asyncio.get_running_loop()
                await loop.sock_connect(self.socker, (self.IP, self.PORT))
                self.connect_state = True
                return True # retornamos True si todo salio bien
        except Exception as e:
            print(e)
            return False # retornamos False si hubo un error
            
    def Disconnect(self):
        try:
            if self.connect_state:
                self.socker.close()
                self.connect_state = False
                return True
        except Exception as e:
            print(e)
            return False
        
    # def the Send and Recv
    async def Send_to_the_server(self,msj):
        try:
            loop = asyncio.get_running_loop()
            async with self.send_lock: 
                await loop.sock_sendall(self.socker, msj.encode())
            return True
        except Exception as e:
            print(e)
            self.connect_state = False
            return False
        
    async def Recv_to_the_server(self):
        loop = asyncio.get_running_loop()
        while self.connect_state:
            try:
                data = await loop.sock_recv(self.socker, 64)
                if not data: # pq quiere decir que el server cerro la conexión 
                    await self.queue.put(None)  # señal de fin
                    self.connect_state = False
                    break
                await self.queue.put(data.decode().strip())
                # no puedo usar return pq me saca del bucle
            except Exception as e:
                print(e)
                self.connect_state = False
                return False