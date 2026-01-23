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
                # create a socket object and set socket
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.setblocking(False)
                loop = asyncio.get_running_loop()
                await loop.sock_connect(self.socket, (self.IP, self.PORT))
                self.connect_state = True
                self.def_connect_state = False
                print("connect")
                return True
        except Exception as e:
            self.def_connect_state = False
            self.connect_state = False
            print(e)
            return False
            
    def Disconnect(self):
        try:
            if self.connect_state and self.socket:
                try:
                    self.socket.shutdown(socket.SHUT_RDWR)  # opcional: cierra lectura y escritura
                except Exception:
                    pass  # puede fallar si ya está cerrado
                self.socket.close()
                self.socket = None
                print("disconnect")
            # actualizar estados siempre
            self.connect_state = False
            self.def_recv_state = False
            return True
        except Exception as e:
            self.connect_state = False
            self.def_recv_state = False
            print("Error al desconectar:", e)
            return False
    
    # def the Send and Recv
    async def Send_to_the_server(self,msj):
        try:
            if self.connect_state:
                async with self.send_lock: 
                    await asyncio.get_running_loop().sock_sendall(self.socket, msj.encode())
                    print("el mjs okey")
        except Exception as e:
            print(e)
            self.connect_state = False
            self.Disconnect()
        
    async def Recv_to_the_server(self):
        loop = asyncio.get_running_loop()
        if not self.def_recv_state:
            self.def_recv_state = True
            print("recv ok")
            try:
                buffer = b""
                if self.connect_state and self.def_recv_state:
                    print("recv ok2")
                while self.connect_state and self.def_recv_state:
                    try:
                        data = await loop.sock_recv(self.socket, 1024)
                        if not data: # pq quiere decir que el server cerro la conexión 
                            await self.queue.put(None)  # señal de fin
                            self.connect_state = False
                            self.def_recv_state = False
                            return True
                        buffer += data
                        while b"\n" in buffer:
                            line, buffer = buffer.split(b"\n", 1) 
                            text = line.decode().strip() 
                            # normalizar a tipos: convertir "True"/"False" a booleanos 
                            if text == "True": 
                                await self.queue.put(True)
                            elif text == "False":
                                await self.queue.put(False) 
                            else: 
                                await self.queue.put(text)
                    except Exception as e:
                        print("Error en recv:", e)
                        await self.queue.put(None)
                        self.connect_state = False
                        self.def_recv_state = False
                        self.Disconnect()
            finally:
                self.def_recv_state = False