# pytest "C:\Users\gabri\OneDrive\Desktop\ALE\python-ale\proyectos\esp_wifi_hc-sr04_f(x,t)\client\test_assembler.py"
import pytest
import B_assembler as Assembler
from unittest.mock import Mock, AsyncMock
from tkinter import Tk ,Label , END
import asyncio
import pytest_asyncio
from C_object_client import Client
from D_object_graph import Graph

@pytest.fixture
def Pass_and_create_Mock_and_assembler():
    loop = None
    client = Mock()
    client.mock_add_spec(Client("esp32_ip","esp32_port","Queue"))
    Queue = Mock()
    Queue.mock_add_spec(asyncio.Queue())
    graph = Mock()
    graph.mock_add_spec(Graph("queue"))
    assembler = Assembler.Assembler(client,graph,Queue,loop)
    yield client, Queue, graph, assembler

@pytest_asyncio.fixture
async def Pass_and_create_AsyncMock_and_assembler():
    loop = asyncio.get_running_loop()

    client = AsyncMock()
    client.mock_add_spec(Client("esp32_ip","esp32_port","Queue"))

    Queue = AsyncMock()
    Queue.mock_add_spec(asyncio.Queue())

    graph = AsyncMock()
    graph.mock_add_spec(Graph("queue"))

    assembler = Assembler.Assembler(client, graph, Queue, loop)
    yield client, Queue, graph, assembler
    
def test_Assembler_disconnect(Pass_and_create_Mock_and_assembler):
    Client, Queue, Graph, assembler = Pass_and_create_Mock_and_assembler
    
    label_mock = Mock()
    Client.Disconnect.return_value = True
    assembler.Assembler_disconnect(label_mock)

    Client.Disconnect.assert_called_once()
    label_mock.config.assert_called_once_with(text="disconnect")
    
def test_Assembler_open_graph(Pass_and_create_Mock_and_assembler):
    Client, Queue, Graph, assembler = Pass_and_create_Mock_and_assembler
    
    label_mock = Mock()
    Graph.Graph_open.return_value = True
    assembler.Assembler_open_graph(label_mock)
    
    Graph.Graph_open.assert_called_once()
    label_mock.config.assert_called_once_with(text="open")
    
def test_Assembler_close_graph(Pass_and_create_Mock_and_assembler):
    Client, Queue, Graph, assembler = Pass_and_create_Mock_and_assembler
    
    label_mock = Mock()
    Graph.Graph_close.return_value = True
    assembler.Assembler_close_graph(label_mock)
    
    Graph.Graph_close.assert_called_once()
    label_mock.config.assert_called_once_with(text="close")


def test_On_closing(Pass_and_create_Mock_and_assembler):
    Client, Queue, Graph, assembler = Pass_and_create_Mock_and_assembler
    
    Client.connect_state = True
    Graph.data_consumer_state = True
    root = Mock()
    assembler.root = root
    
    assembler.On_closing()
    
    assert assembler._running is False
    
    Client.Disconnect.assert_called_once()
    Graph.Graph_close.assert_called_once()
    root.after.assert_called_once()
    assert Client.def_recv_state is False
    assert Graph.data_consumer_state is False
    
@pytest.mark.asyncio
async def test_Assembler_send_to_serve(Pass_and_create_AsyncMock_and_assembler):
    Client, Queue, Graph, assembler = Pass_and_create_AsyncMock_and_assembler
    
    entry_mock = Mock()
    entry_mock.get.return_value = "send"
    
    Client.connect_state = True
    
    assembler.Assembler_send_to_serve(entry_mock)
    
    Client.Send_to_the_server.assert_called_once_with("send")
    entry_mock.get.assert_called_once()
    
@pytest.mark.asyncio
async def test_Assembler_connect(Pass_and_create_AsyncMock_and_assembler):
    Client, Queue, Graph, assembler = Pass_and_create_AsyncMock_and_assembler
    
    Client.connect_state = True
    Client.def_connect_state = False
    Client.Connect.return_value = True
    root = Tk()
    
    label_Client = Label(root)
    
    Queue.get.return_value = None
    
    assembler.loop.create_task(assembler.Assembler_connect(label_Client,root))
    
    await asyncio.sleep(0.5)
    
    assert assembler.second_window_state is True
    assert label_Client.cget("text") == "connect"
    
    assembler.set_second_window["entry_password"].delete(0, END)
    assembler.set_second_window["entry_password"].insert(0, "Ale1524")
    assembler.set_second_window["button_password"].invoke()
    Client.Send_to_the_server.assert_called_once_with("Ale1524")
    
    ######################################################################################
    Queue.get.return_value = "Incorrect password"
    
    await asyncio.sleep(0.5)
    
    assert assembler.set_second_window["label_passwordstate"].cget("text") == "Incorrect password"
    
    #######################################################################################
    Queue.get.return_value = True
    
    await asyncio.sleep(0.5)
    
    Graph.Data_consumer.assert_called_once()
    assert assembler.second_window_state is False
    
    with pytest.raises(AttributeError):
        assembler.set_second_window
        
    #######################################################################################
    Queue.get.return_value = False
    
    assembler.loop.create_task(assembler.Assembler_connect(label_Client,root))
    
    await asyncio.sleep(0.5)
    
    assert Client.connect_state is False
    assert label_Client.cget("text") == "disconnect"
    assert assembler.second_window_state is False
    
    with pytest.raises(AttributeError):
        assembler.set_second_window

    
@pytest.mark.asyncio
async def test_Root_open(Pass_and_create_AsyncMock_and_assembler):
    client, Queue, graph, assembler = Pass_and_create_AsyncMock_and_assembler
    
    root ,set_bts ,set_label ,entry = assembler.Root_open()
    
    assert assembler._running is True
    assert set_label["label_Client"].cget("text") == "disconnect"
    assert set_label["label_graph"].cget("text") == "close"
    ######################################################################################
    
    ######################################################################################
    client.connect_state = True
    client.def_connect_state = False
    client.Connect.return_value = True
    
    set_bts["Connect"].invoke()
    
    await asyncio.sleep(0.5)
    
    assert assembler.second_window_state is True
    assert set_label["label_Client"].cget("text") == "connect"
    
    assembler.set_second_window["entry_password"].delete(0, END)
    assembler.set_second_window["entry_password"].insert(0, "Ale1524")
    assembler.set_second_window["button_password"].invoke()
    client.Send_to_the_server.assert_called_once_with("Ale1524")
    
    ######################################################################################
    Queue.get.return_value = "Incorrect password"
    
    await asyncio.sleep(0.5)
    
    assert assembler.set_second_window["label_passwordstate"].cget("text") == "Incorrect password"
    
    #######################################################################################
    Queue.get.return_value = True
    
    await asyncio.sleep(0.5)
    
    graph.Data_consumer.assert_called_once()
    assert assembler.second_window_state is False
    
    with pytest.raises(AttributeError):
        assembler.set_second_window
    
    assert set_label["label_Client"].cget("text") == "connect"
    #######################################################################################
    
    #######################################################################################
    assembler.Client = Mock()
    client = assembler.Client
    client.mock_add_spec(Client("esp32_ip","esp32_port","Queue")) 
    client.Disconnect.return_value = True
    
    set_bts["Disconnect"].invoke()
    
    client.Disconnect.assert_called_once()
    assert set_label["label_Client"].cget("text") == "disconnect"
    
    #######################################################################################
    
    #######################################################################################
    assembler.Client = AsyncMock()
    client = assembler.Client
    client.connect_state = True
    client.mock_add_spec(Client("esp32_ip","esp32_port","Queue")) 
    
    entry.delete(0, END)
    
    entry.insert(0,"Ale1524")
    
    set_bts["send"].invoke()
    
    client.Send_to_the_server.assert_called_once_with("Ale1524")
    
    #######################################################################################
    
    #######################################################################################
    assembler.Graph = Mock()
    graph = assembler.Graph
    graph.mock_add_spec(Graph("Queue"))
    graph.Graph_open.return_value = True
    
    set_bts["Graph open"].invoke()
    
    graph.Graph_open.assert_called_once()
    assert set_label["label_graph"].cget("text") == "open"
    
    #######################################################################################
    
    #######################################################################################
    graph.reset_mock()
    graph.Graph_close.return_value = True
    set_bts["Graph close"].invoke()
    
    graph.Graph_close.assert_called_once()
    assert set_label["label_graph"].cget("text") == "close"