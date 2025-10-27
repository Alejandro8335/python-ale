import asyncio

# import modules
from B_assembler import Assembler

# create a Client object and set client
ESP32_IP = "192.168.100.219"
ESP32_PORT = 8080

# create Assembler object and set Assembler
assembler = Assembler(ESP32_IP,ESP32_PORT)

asyncio.run(assembler.assembler())