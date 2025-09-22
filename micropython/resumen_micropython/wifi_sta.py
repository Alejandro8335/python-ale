import network
import time

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

ssid = "Toti"
password = "avion123"

sta_if.connect(ssid, password)

while not sta_if.isconnected():
    time.sleep(1)

print("Conectado, configuración de red:", sta_if.ifconfig())

