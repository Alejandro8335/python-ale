import network
import socket
import uasyncio
from time import sleep_ms,sleep
from machine import Pin

from server import Wifi_sta_server
from hc_sr04 import HCSR04

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect("Toti", "avion123")
while not sta.isconnected():
    sleep_ms(200)
ip = sta.ifconfig()[0]

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('0.0.0.0', 8080))
server.listen(1)

there_is_client = False

async def On_off_led(blue_led):
    blue_led.on()
    await uasyncio.sleep(0.5)
    blue_led.off()
async def Assembler(client):
    global there_is_client
    try:
        red_led_connect_state = Pin(23, Pin.OUT)
        blue_led_recv_client = Pin(5, Pin.OUT)
        red_led_connect_state.on()
        sta = Wifi_sta_server(client)
        uasyncio.create_task(sta.Recv_to_the_client())
        customer_login = False
        for _ in range(6100):
            if sta.list_recv:
                print("hay data")
                uasyncio.create_task(On_off_led(blue_led_recv_client))
                if sta.list_recv.pop(0) == "Ale1524":
                    print("la password es correcta")
                    customer_login = True
                    uasyncio.create_task(sta.Send_to_the_client("True\n"))
                    break
                else:
                    uasyncio.create_task(sta.Send_to_the_client("Incorrect password\n"))
                    print("Incorrect password")
                if sta.client_state is False:
                    break
            await uasyncio.sleep(0.01)
        sta.list_recv.clear()
        if not customer_login and sta.client_state:
            print("chau")
            uasyncio.create_task(sta.Send_to_the_client("False\n"))
            client.close()
            sta.client_state = False
        sensor = HCSR04(15,14)
        sending_msj = False
        while sta.client_state:
            try:
                if sta.list_recv:
                    sta.list_recv.pop(0)
                    uasyncio.create_task(On_off_led(blue_led_recv_client))
                if not sending_msj:
                    sending_msj = True
                    uasyncio.create_task(sta.Send_to_the_client(await sensor.Sendpulse_cm()))
                    sending_msj = False
                await uasyncio.sleep(0.1)
            except Exception as e:
                    print(e)
        try: client.close()
        except: pass
        there_is_client = False
        red_led_connect_state.off()
    finally:
        red_led_connect_state.off()
async def Main():
    global there_is_client
    try:
        while True:
            try:
                client, addr = server.accept()
                client.settimeout(1.0)
            except OSError:
                continue
            client.settimeout(5.0)
            uasyncio.create_task(Assembler(client))
            there_is_client = True
            while there_is_client:
                await uasyncio.sleep(3600)
    finally:
        server.close()
uasyncio.run(Main())