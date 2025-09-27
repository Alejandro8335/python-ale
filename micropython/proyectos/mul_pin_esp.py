import network
import socket
import machine
from time import sleep,sleep_ms
from utime import sleep_us

class HCSR04():
    # echo_timeout_us is based in chip range limit (400cm)
    def __init__(self, trigger_pin, echo_pin, echo_timeout_us=500*2*30):
        self.echo_timeout_us = echo_timeout_us
        # Init trigger pin (out)
        self.trigger = machine.Pin(trigger_pin, mode=machine.Pin.OUT, pull=None)
        self.trigger.value(0)

        # Init echo pin (in)
        self.echo = machine.Pin(echo_pin, mode=machine.Pin.IN, pull=None)

    def _send_pulse_and_wait(self):
        self.trigger.value(0) # Stabilize the sensor
        sleep_us(5)
        self.trigger.value(1)
        # Send a 10us pulse.
        sleep_us(10)
        self.trigger.value(0)
        try:
            pulse_time = machine.time_pulse_us(self.echo, 1, self.echo_timeout_us)
            if pulse_time < 0:
                MAX_RANGE_IN_CM = const(500)
                pulse_time = int(MAX_RANGE_IN_CM * 29.1)
            return pulse_time
        except OSError as ex:
            if ex.args[0] == 110:
                raise OSError('Out of range')
            raise ex

    def distance_mm(self):
        pulse_time = self._send_pulse_and_wait()

        mm = pulse_time * 100 // 582
        return mm

class Button():
    def __init__(self,Pinn):
        self.Pin = machine.Pin(Pinn, machine.Pin.IN, machine.Pin.PULL_UP)
        self.prev = False
    def Press(self):
        if not self.Pin.value() and not self.prev:
            sleep_ms(80)
            if not self.Pin.value():
                self.prev = True
                return True
            
        elif self.Pin.value() and self.prev:
            sleep_ms(80)
            if self.Pin.value():
                self.prev = False
        return False
button = Button(12)
sensor = HCSR04(32,33)

sta = network.WLAN(network.STA_IF)
sta.active(True)

sta.connect("Toti", "avion123")
while not sta.isconnected():
    sleep(1)
ip = sta.ifconfig()[0]

server = socket.socket()
server.bind(('0.0.0.0', 8080))
server.listen(1)


try:
    while True:
        try:
            client, addr = server.accept()# Si no hay clientes, levanta OSError por el timeout
            client.settimeout(1.0)  # evita bloqueos largos
        except OSError:
            continue                         # Volvemos al loop para permitir detener el script
        client.settimeout(5.0)
        while True:
            try:
                if button.Press():
                    msg_on = "(2,0)\n"
                    client.send(msg_on.encode())
                    print(msg_on)
                
                sleep_ms(25)
                data = client.recv(64)
                if data:
                    try:
                        text = data.decode()   # Convierte a string

                        # Evalúa el string como tupla
                        tupla = eval(text)  # ⚠️ Solo si confías en el origen
                        def_ , Pin_, number = tupla
                        
                        if def_ == 1:
                            Pin_auxiliary = machine.Pin(Pin_,machine.Pin.OUT)
                            Pin_auxiliary.value(number)
                            
                        if def_ == 2:
                            Pin_auxiliary = machine.PWM(machine.Pin(Pin_))
                            Pin_auxiliary.freq(90)
                            Pin_auxiliary.duty(number)
                            
                    except:
                        continue
                    
                sleep_ms(50)
            except OSError:
                    data = b''  # No hay datos, seguimos
                
finally:
    server.close()