import uasyncio
class Wifi_sta_server:
    def __init__(self, client):
        self.client = client
        self.client_state = True
        self.lock = uasyncio.Lock()
        self.list_recv = []
    async def Send_to_the_client(self, msj):
        try:
            print("enviando msj")
            self.client.send((str(msj) + "\n").encode())
        except Exception as e:
            print("in server,error send_to_the_client", e)
            self.client_state = False
            
    async def Recv_to_the_client(self):
        print("intentando resivir msj")
        self.client.setblocking(False)
        while self.client_state:
            try:
                data = self.client.recv(1024)
                if isinstance(data, bytes):
                    data = data.decode()
                data = data.strip()
                if not data:  # conexión cerrada
                    self.client_state = False
                    break
                self.list_recv.append(data)
                print("msj okey")
            except OSError as e: 
                if e.args[0] == errno.EAGAIN: # no hay datos disponibles 
                    await uasyncio.sleep(0.1) # ceder al loop y reintentar
                    continue 
                else: 
                    print("in server,error Recv_to_the_client", e) 
                    self.client_state = False