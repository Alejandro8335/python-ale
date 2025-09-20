from machine import PWM,Pin


class Servo():
    def __init__(self,Pin_num,star_angle = 0):
        self.PWM = PWM(Pin(Pin_num),50)
        self.angle = 0
        self.star_angle = star_angle
        self.update(self.star_angle)
        
    def angle_to_pulse_us(self,angle):
        # a) Limita el rango de ángulo
        angle = max(0, min(180,angle))
        return 500 + (angle / 180) * 1900
    
    def pulse_us_to_duty(self,pulse_us, period_us=20000, resolution=1023):
        return int((pulse_us / period_us) * resolution)
    
    def update(self,angle):
        pulse = self.angle_to_pulse_us(angle)
        duty_value = self.pulse_us_to_duty(pulse)
        self.PWM.duty(duty_value)
        self.angle = angle
        
servo = Servo(5,90)

while True:
    angle = int(input("angle: "))
    servo.update(angle)
    print(servo.angle)