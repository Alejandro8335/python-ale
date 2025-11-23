import uasyncio as asyncio
class Wifi_sta_server:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer
        self.client_state = True
        self.lock = asyncio.Lock()
    async def Send_to_the_client(self, msj):
        try:
            async with self.lock:
                self.writer.write(str(msj).encode())
                await self.writer.drain()
        except Exception as e:
            print("in server,error send_to_the_client", e)
            self.client_state = False
    async def Recv_to_the_client(self,list_recv):
        try:
            while self.client_state:
                data = await self.reader.read(64)
                if not data:  # conexión cerrada
                    self.client_state = False
                    break
                list_recv.append(data)
        except Exception as e:
            print(e)
            self.client_state = False
        try:
            await self.writer.aclose()
        except:
            pass