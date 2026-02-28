import socket

ESP32_IP   = '192.168.100.219'
ESP32_PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ESP32_IP, ESP32_PORT))
    for comando in ['1', '2']:
        s.send(comando.encode())
        respuesta = s.recv(64).decode().strip()
        print('Respuesta del ESP32:', respuesta)    