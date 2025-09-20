import network

# Crear objeto para la interfaz Access Point
ap = network.WLAN(network.AP_IF)

# Activar la interfaz
ap.active(True)

#network.AP_IF → selecciona la interfaz de punto de acceso.

#.active(True) → enciende la radio Wi‑Fi en modo AP.

ap.config(essid="ESP32_AP", password="Dominguez", authmode=3)

#essid → nombre de la red que verás en tu PC.

#password → clave WPA2 (mínimo 8 caracteres).

#authmode=3 → WPA2-PSK (modo seguro más común)

print("AP activo:", ap.active())
print("Configuración IP:", ap.ifconfig())
