# pytest "C:\Users\gabri\OneDrive\Desktop\ALE\python-ale\proyectos\esp_wifi_hc-sr04_f(x,t)\client\test_client.py"
import pytest
import asyncio
from C_object_client import Client

@pytest.mark.asyncio
async def test_Send_to_the_server_and_Recv_to_the_server():
    recv_task = None
    try:
        ESP_IP = "192.168.100.219"
        ESP_PORT = (8080)
        queue = asyncio.Queue()
        client = Client(ESP_IP, ESP_PORT,queue)
        #conecion al servidor
        assert await client.Connect() is True and client.connect_state is True
        
        await asyncio.sleep(0.5)
        
        recv_task = asyncio.create_task(client.Recv_to_the_server())
        await asyncio.sleep(0.5)
        assert client.connect_state is True
        assert client.def_recv_state is True
        
        await asyncio.sleep(0.5)
        await client.Send_to_the_server(msj="Ale1524\n")
        assert client.connect_state is True
        
        await asyncio.sleep(0.5)
        
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

        assert client.Disconnect() is True
        assert client.connect_state is False and client.def_recv_state is False
    finally:
        if recv_task and client.def_recv_state:
            recv_task.cancel()
            try:
                await recv_task
            except asyncio.CancelledError:
                pass
        if client and client.connect_state:client.Disconnect()