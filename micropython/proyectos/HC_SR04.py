
from machine import Pin, time_pulse_us
from utime import sleep_us
import time


class HCSR04:
    # echo_timeout_us is based in chip range limit (400cm)
    def __init__(self, trigger_pin, echo_pin, echo_timeout_us=500*2*30):
        self.echo_timeout_us = echo_timeout_us
        # Init trigger pin (out)
        self.trigger = Pin(trigger_pin, mode=Pin.OUT, pull=None)
        self.trigger.value(0)

        # Init echo pin (in)
        self.echo = Pin(echo_pin, mode=Pin.IN, pull=None)

    def _send_pulse_and_wait(self):
        self.trigger.value(0) # Stabilize the sensor
        sleep_us(5)
        self.trigger.value(1)
        # Send a 10us pulse.
        sleep_us(10)
        self.trigger.value(0)
        try:
            pulse_time = time_pulse_us(self.echo, 1, self.echo_timeout_us)
            # time_pulse_us returns -2 if there was timeout waiting for condition; and -1 if there was timeout during the main measurement. It DOES NOT raise an exception
            # ...as of MicroPython 1.17: http://docs.micropython.org/en/v1.17/library/machine.html#machine.time_pulse_us
            if pulse_time < 0:
                MAX_RANGE_IN_CM = const(500) # it's really ~400 but I've read people say they see it working up to ~460
                pulse_time = int(MAX_RANGE_IN_CM * 29.1) # 1cm each 29.1us
            return pulse_time
        except OSError as ex:
            if ex.args[0] == 110: # 110 = ETIMEDOUT
                raise OSError('Out of range')
            raise ex

    def distance_mm(self):
        pulse_time = self._send_pulse_and_wait()

        # To calculate the distance we get the pulse_time and divide it by 2 
        # (the pulse walk the distance twice) and by 29.1 becasue
        # the sound speed on air (343.2 m/s), that It's equivalent to
        # 0.34320 mm/us that is 1mm each 2.91us
        # pulse_time // 2 // 2.91 -> pulse_time // 5.82 -> pulse_time * 100 // 582 
        mm = pulse_time * 100 // 582
        return mm

    def distance_cm(self):
        pulse_time = self._send_pulse_and_wait()

        # To calculate the distance we get the pulse_time and divide it by 2 
        # (the pulse walk the distance twice) and by 29.1 becasue
        # the sound speed on air (343.2 m/s), that It's equivalent to
        # 0.034320 cm/us that is 1cm each 29.1us
        cms = (pulse_time / 2) / 29.1
        return cms

#pin sensor
trigger = 2
echo = 4

#objeto
sensor = HCSR04(trigger,echo)

#pin leds 
verde0 = Pin(32, Pin.OUT)
verde1 = Pin(26,Pin.OUT)
verde2 = Pin(13, Pin.OUT)
verde3 = Pin(12,Pin.OUT)
verde4 = Pin(27, Pin.OUT)

#def pins
def pins(distacia):
    #led 1
    if distacia <= 7.4:
        verde4.on()
    else:
        verde4.off()
        
    if distacia <= 14.8:
        verde3.on()
    else:
        verde3.off()
    
    if distacia <= 22.3:
        verde2.on()
    else:
        verde2.off()
        
    if distacia <= 29.6:
        verde1.on()
    else:
        verde1.off()
    
    if distacia <= 37:
        verde0.on()
    else:
        verde0.off()
    
#obtener las distancias
while True:
    distanciaCM = sensor.distance_cm()
    distanciaMM = sensor.distance_mm()
    print(int(distanciaCM))
    time.sleep(0.25)
    pins(distanciaCM)
    
     