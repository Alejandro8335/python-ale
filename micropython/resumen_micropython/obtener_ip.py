import network
import time

# Configura tu red WiFi
ssid = "Toti"
password = "avion123"
# Crea el objeto de red
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Espera a que se conecte
while not wlan.isconnected():
    time.sleep(1)

# Imprime la dirección IP
print('Dirección IP:', wlan.ifconfig()[0])
