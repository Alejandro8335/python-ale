import asyncio
from B_assembler import Assembler
from C_object_client import Client
from D_object_graph import Graph

# communication channel
queue = asyncio.Queue()

# creating a Client object
ESP_IP = "192.168.100.219"
ESP_PORT = (8080)
client = Client(ESP_IP,ESP_PORT,queue)

# creating a Graph object
graph = Graph(queue)

# create Assembler object and set Assembler
assembler = Assembler(client,graph)

if __name__ == "__main__":
    asyncio.run(assembler.Root_open())