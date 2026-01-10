import network
import socket
import uasyncio as asyncio
from time import sleep_ms,sleep
from machine import Pin
# modulos
from server import Wifi_sta_server
from hc_sr04 import HCSR04
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect("Toti", "avion123")
while not sta.isconnected():
    asyncio.sleep(1)
ip = sta.ifconfig()[0]
async def blue_led(blue_led):
    blue_led.on()
    await asyncio.sleep(0.5)
    blue_led.off()
async def Assembler(reader,writer):
    red_led_connect_state = Pin(23, Pin.OUT)
    blue_led_recv_client = Pin(5, Pin.OUT)
    list_recv = []
    wifi = Wifi_sta_server(reader, writer)
    asyncio.create_task(wifi.Recv_to_the_client(list_recv))
    customer_login = False
    for _ in range(6100):
        if list_recv:
            if list_recv[0] == "Ale1524":
                customer_login = True
                await wifi.Send_to_the_client(True)
                break
            else:
                await wifi.Send_to_the_client("Incorrect password")
        sleep(0.01)
    if not customer_login:
        await wifi.Send_to_the_client(False)
        writer.close()
        await writer.wait_closed()
    sensor = HCSR04(15,5)
    sending_msj = False
    red_led_connect_state.on()
    try:
        while wifi.client_state:
            try:
                if list_recv is None:
                    red_led_connect_state.off()
                elif list_recv:
                    list_recv.pop(0)
                    blue_led(blue_led_recv_client)
                if not sending_msj:
                    sending_msj = True
                    await wifi.Send_to_the_client(await asyncio.create_task(sensor.Sendpulse_cm()))
                    sending_msj = False
                await asyncio.sleep(0.1)
            except Exception as e:
                print(e)
            return red_led_connect_state
    finally:
        red_led_connect_state.off()
async def Main():
    server = await asyncio.start_server(Assembler,"0.0.0.0", 8080)
    try:
        while True:
            await asyncio.sleep(3600)
    finally:
        server.close()
        await server.wait_closed()
asyncio.run(Main())