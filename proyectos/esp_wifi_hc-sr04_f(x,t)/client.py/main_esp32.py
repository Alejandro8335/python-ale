import network
import socket
import machine
import asyncio
from time import sleep

# create a sta object and set sta
sta = network.WLAN(network.STA_IF)
sta.active(True)

sta.connect("Toti", "avion123")
while not sta.isconnected():
    sleep(1)
ip = sta.ifconfig()[0]

server = socket.socket()
server.bind(('0.0.0.0', 8080))
server.listen(1)

# def of read and send_information
async def Read(client):
    await msj = client.recv(64)
    return msj

async def Read(client,msj):
    await client.send(msj)

# creating an esp_32 object
class Esp_32():
    pass

# main loop
try:
    while True:
        try:
            client, addr = server.accept()# Si no hay clientes, levanta OSError por el timeout
            client.settimeout(1.0)  # evita bloqueos largos
        except OSError:
            continue                         # Volvemos al loop para permitir detener el script
        client.settimeout(5.0)
        while True:
            pass
            
finally:
    server.close()