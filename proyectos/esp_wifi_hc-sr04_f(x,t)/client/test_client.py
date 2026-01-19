# pytest "C:\Users\gabri\OneDrive\Desktop\ALE\python-ale\proyectos\esp_wifi_hc-sr04_f(x,t)\client\test_client.py"
import pytest
import pytest_asyncio
import asyncio
from C_object_client import Client

@pytest_asyncio.fixture(scope="module")
def Pass_the_Client():
    ESP_IP = "192.168.100.219"
    ESP_PORT = (8080)
    queue = asyncio.Queue()
    client = Client(ESP_IP, ESP_PORT,queue)
    yield queue ,client
    
@pytest.mark.asyncio
async def test_Send_to_the_server(Pass_the_Client):
    recv_task = None
    try:
        queue ,client = Pass_the_Client
        #conecion al servidor
        await client.Connect()
        assert client.connect_state is True
        
        await asyncio.sleep(1)
        
        recv_task = asyncio.create_task(client.Recv_to_the_server())
        assert client.connect_state is True
        
        await asyncio.sleep(1)
        await client.Send_to_the_server(msj="Ale1524\n")
        assert client.connect_state is True
        
        await asyncio.sleep(1)
        
        try: 
            data = await asyncio.wait_for(queue.get(), timeout=180) # espera total 60s
        except asyncio.TimeoutError: 
            pytest.fail("No response from server within 60 seconds") 
            
        if data is None:
            pytest.fail("Connection closed by server") 
        if data is True: 
            return 0
        if data is False:
            pytest.fail("Server signaled timeout")
        if data == "Incorrect password":
            pytest.fail("The password is incorrect.")

    finally:
        client.Disconnect()
        if recv_task:recv_task.cancel()