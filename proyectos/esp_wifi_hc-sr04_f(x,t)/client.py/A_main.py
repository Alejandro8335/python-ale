import asyncio
from B_assembler import Assembler
# create Assembler object and set Assembler
assembler = Assembler("192.168.100.219",8080)

asyncio.run(assembler.Root_open())