import machine
import uasyncio as asyncio
class HCSR04:
    def __init__(self, trigger_pin, echo_pin, echo_timeout_us=500*2*30):
        self.echo_timeout_us = echo_timeout_us
        self.trigger = machine.Pin(trigger_pin, mode=machine.Pin.OUT, pull=None)
        self.trigger.value(0)
        self.echo = machine.Pin(echo_pin, mode=machine.Pin.IN, pull=None)
    async def Sendpulse_cm(self):
        self.trigger.value(0)
        await asyncio.sleep_ms(1)
        self.trigger.value(1)
        await asyncio.sleep_ms(1)
        self.trigger.value(0)
        try:
            pulse_time = machine.time_pulse_us(self.echo, 1, self.echo_timeout_us)
            if pulse_time < 0: 
                pulse_time = int(500 * 29.1)
            return str(round((pulse_time/2)/29.1,2)) + " "
        except OSError as ex:
            if ex.args[0] == 110:
                raise OSError('Out of range')
            raise ex