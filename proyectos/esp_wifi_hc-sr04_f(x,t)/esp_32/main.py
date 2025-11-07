import network
import socket
import uasyncio as asyncio
from time import sleep_ms,sleep
import time
# modulos
from server import Wifi_sta_server
from hc_sr04 import HCSR04
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect("Toti", "avion123")
while not sta.isconnected():
    asyncio.sleep(1)
ip = sta.ifconfig()[0]

async def Assembler(reader,writer):
    list_recv = []
    peername = writer.get_extra_info("peername")
    if peername[0] != "192.168.100.5":
        print(f"Conexión rechazada de {peername[0]}")
        writer.close()
        await writer.wait_closed()
    wifi = Wifi_sta_server(reader, writer)
    asyncio.create_task(wifi.Recv_to_the_client())
    sensor = HCSR04(15,5)
    sending_msj = False
    while wifi.client_state:
        try:
            if list_recv:
                data_recv = list_recv.pop(0)
                print(f"valor que manda el cliente :{data_recv}")
            if not sending_msj:
                sending_msj = True
                await wifi.Send_to_the_client(asyncio.create_task(sensor.send_pulse_cm()))
                sending_msj = False
            await asyncio.sleep(0.1)
        except Exception as e:
            print(e)
async def Main():
    server = await asyncio.start_server(Assembler,"0.0.0.0", 8080)
    async with server:
        try:
            await server.serve_forever()
        finally:
            server.close()
            await server.wait_closed()
asyncio.run(Main())