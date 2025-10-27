import network
import socket
import machine
import uasyncio as asyncio
from time import sleep_ms,sleep
import time
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect("Toti", "avion123")
while not sta.isconnected():
    sleep(1)
ip = sta.ifconfig()[0]
list_hcsr04 = []
list_recv = []
class HCSR04:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger = machine.Pin(trigger_pin, machine.Pin.OUT)
        self.echo = machine.Pin(echo_pin, machine.Pin.IN)
        self.trigger.value(0)
        sleep_ms(50)
    async def medir_cm(self, timeout_us=30000):
        self.trigger.value(1)
        time.sleep_us(10)
        self.trigger.value(0)
        start_wait = time.ticks_us()
        while self.echo.value() == 0:
            if time.ticks_diff(time.ticks_us(), start_wait) > timeout_us:
                return None
            await asyncio.sleep_ms(1)
        start = time.ticks_us()
        while self.echo.value() == 1:
            if time.ticks_diff(time.ticks_us(), start) > timeout_us:
                return None
            await asyncio.sleep_ms(1)
        end = time.ticks_us()
        duration = time.ticks_diff(end, start)
        distance = (duration / 2) / 29.1
        return distance
    async def Distance_cm(self):
        global list_hcsr04
        while True:
            if len(list_hcsr04) < 4:
                list_hcsr04.append(await self.medir_cm())
            else:
                list_hcsr04[4] = await self.medir_cm()
            await asyncio.sleep(1)
class Esp_32:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer
        self.client_state = True
        self.lock = asyncio.Lock()
    async def Send_to_the_client(self, msj):
        try:
            async with self.lock:
                print(f"enviando,{msj}")
                self.writer.write(msj.encode())
                await self.writer.drain()
                print("listo")
        except Exception as e:
            print("Error en envío:", e)
            self.client_state = False
    async def Recv_to_the_client(self):
        global list_recv
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
        list_recv.append("close")
async def Assembler(reader,writer):
    global list_recv ,list_hcsr04
    esp = Esp_32(reader, writer)
    asyncio.create_task(esp.Recv_to_the_client())
    sensor = HCSR04(15,5)
    asyncio.create_task(sensor.Distance_cm())
    while True:
        if not list_recv and not list_hcsr04:
            await asyncio.sleep(0.25)
            continue
        if list_recv:
            data_recv = list_recv.pop(0)
            if data_recv == "close":
                break
            else:
                print(f"valor que manda el cliente :{data_recv}")
        if list_hcsr04:
            data_hcsr04 = list_hcsr04.pop(0)
            if not(data_hcsr04 == None):
                await esp.Send_to_the_client(str(data_hcsr04)) 
async def Main():
    await asyncio.start_server(Assembler, "0.0.0.0", 8080)
    # Sabés que hay clientes porque Main_loop se ejecuta por cada conexión.
    while True:
        await asyncio.sleep(3600)
asyncio.run(Main())