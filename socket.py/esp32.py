import socket

# IP del ESP32 en modo AP
ESP32_IP = "192.168.4.1"
ESP32_PORT = 8080  # Debe coincidir con el puerto del servidor en el ESP32

# Crear socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET → indica que usaremos direcciones IPv4.
# socket.SOCK_STREAM → indica que será un socket TCP (conexión confiable, orientada a flujo de datos).
try:
    # Conectar al ESP32
    client_socket.connect((ESP32_IP, ESP32_PORT))
    print(f"Conectado a {ESP32_IP}:{ESP32_PORT}")
    # Abre la conexión hacia el ESP32.
    # Si el ESP32 no tiene un servidor escuchando en ese puerto, aquí dará error.
    
    # Enviar mensaje
    mensaje = "Hola desde la PC"
    client_socket.send(mensaje.encode())
    print("Mensaje enviado")
    # mensaje.encode() → convierte el texto a bytes, porque la red transmite bytes, no cadenas.
    # .send() → envía esos bytes al ESP32.
    
    # Recibir respuesta (opcional)
    respuesta = client_socket.recv(1024).decode()
    print("Respuesta del ESP32:", respuesta)
    
    # .recv(1024) → espera recibir hasta 1024 bytes desde el ESP32.
    # .decode() → convierte los bytes recibidos de nuevo a texto.
except Exception as e:
    print("Error:", e)

finally:
    client_socket.close()
