from machine import Pin

class DIP():
    def __init__(self,input_0,input_1,input_2,input_3):
        self.list_input = [
                     Pin(input_0, Pin.IN, Pin.PULL_UP),
                     Pin(input_1, Pin.IN, Pin.PULL_UP),
                     Pin(input_2, Pin.IN, Pin.PULL_UP),
                     Pin(input_3, Pin.IN, Pin.PULL_UP)
                     ]
        self.last_num = None
        
    # def Read_binario(self):
    #     str_b2 = ""
    #     for i in self.list_input:
    #         if not i.value():
    #             str_b2 = str_b2 + "1"                
    #         else:
    #             str_b2 = str_b2 + "0"
    #     if str_b2 == None:
    #         str_b2 = "0"
    #     return str_b2

    # def B2_to_b10(self,str_b2):
    #     decimal = 0
    #     for i in str_b2:
    #         decimal = decimal * 2 + int(i)#multublicas por la base
    #     if self.last_num != decimal:
    #         self.last_num = decimal
    #         return decimal
    #     return None
    
    def B2_to_b10(self):
        decimal = 0
        for i in self.list_input:
            decimal *= 2
            if not i.value():
                decimal += 1
        #para que no retorne todo el tiempo el decimal
        if self.last_num != decimal:
            self.last_num = decimal
            return decimal
        return None

dip = DIP(27,32,19,18)

while True:
    x = dip.B2_to_b10()
    if x != None:
        print(x)

#Pin.IN, Pin.PULL_UP:
#Abierto 1
#Cerrado (a GND) 0
#Pin.IN, Pin.PULL_DOWN:
#Abierto 0
#Cerrado (a Vcc) 1

