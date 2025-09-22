import network
import socket
from machine import Pin
from time import sleep

sta = network.WLAN(network.STA_IF)
sta.active(True)

sta.connect("Toti", "avion123")
while not sta.isconnected():
    sleep(1)
ip = sta.ifconfig()[0]

server = socket.socket()
server.bind(('0.0.0.0', 8080))
server.listen(1)

pin = Pin(2,Pin.OUT)

while True:
    try:
        client, addr = server.accept()# Si no hay clientes, levanta OSError por el timeout
    except OSError:
        continue                         # Volvemos al loop para permitir detener el script
    client.settimeout(5.0)
    
    # mientras el cliente siga enviando…
    while True:
        try:
            data = client.recv(64)      # lee hasta 64 bytes
        except OSError:
            break                       # timeout en recv()
        if not data:
            break                       # cliente cerró la conexión
        
        msg = data.decode().strip()
        
        # Procesar comando 1/2 u otro mensaje
        if msg == "1":
            pin.on()
            msg_on = "1"
            client.send(msg_on.encode())
        elif msg == "2":
            pin.off()
            msg_off = "2"
            client.send(msg_off.encode())
            
        elif msg == "3":
            respuesta = "3"
            client.send(respuesta.encode())  # enviamos confirmación
            client.close()                   # cerramos conexión con este cliente
            break                            # salimos del bucle interno
