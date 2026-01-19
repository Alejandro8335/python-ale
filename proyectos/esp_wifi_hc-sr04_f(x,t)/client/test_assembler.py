# pytest "C:\Users\gabri\OneDrive\Desktop\ALE\python-ale\proyectos\esp_wifi_hc-sr04_f(x,t)\client\test_assembler.py"
import pytest
import B_assembler as Assembler
from unittest.mock import Mock ,call
from tkinter import Tk
import asyncio

@pytest.fixture
def Pass_and_create_Mock_and_assembler():
    Client = Mock()
    Queue = Mock()
    Graph = Mock()
    assembler = Assembler.Assembler(Client,Graph,Queue)
    yield Client, Queue, Graph, assembler

def test_Assembler_disconnect(Pass_and_create_Mock_and_assembler):
    Client, Queue, Graph, assembler = Pass_and_create_Mock_and_assembler
    
    label_mock = Mock()
    label_mock.config(text="disconnect")
    
    Client.Disconnect("disconnect")
    
    assembler.Assembler_disconnect(label_mock)

    Client.Disconnect.assert_called_once_with()
    label_mock.config.assert_called_once_with(text="disconnect")
    
def test_Assembler_open_graph(Pass_and_create_Mock_and_assembler):
    Client, Queue, Graph, assembler = Pass_and_create_Mock_and_assembler
    
    label_mock = Mock()
    label_mock.config(text="open")
    
    Graph.Graph_open()
    
    assembler.Assembler_open_graph(label_mock)
    
    Graph.Graph_open.assert_called_once_with()
    label_mock.config.assert_called_once_with(text="open")
    
def test_Assembler_close_graph(Pass_and_create_Mock_and_assembler):
    Client, Queue, Graph, assembler = Pass_and_create_Mock_and_assembler
    
    label_mock = Mock()
    label_mock.config(text="close")
    
    Graph.Graph_close()
    
    assembler.Assembler_close_graph(label_mock)
    
    Graph.Graph_close.assert_called_once_with()
    label_mock.config.assert_called_once_with(text="open")

def test_Assembler_send_to_serve(Pass_and_create_Mock_and_assembler):
    Client, Queue, Graph, assembler = Pass_and_create_Mock_and_assembler
    
    entry_mock = Mock()
    entry_mock.get.return_value = "send"
    
    Client.connect_state = True
    Client.Send_to_the_server()
    
    assembler.Assembler_send_to_serve(entry_mock)
    
    Client.Send_to_the_server.assert_called_once_with("send")
    entry_mock.get.assert_called_once_with()
    
def test_Assembler_connect(Pass_and_create_Mock_and_assembler):
    Client, Queue, Graph, assembler = Pass_and_create_Mock_and_assembler
    
    Client.Connect()
    Client.connect_state = True
    Client.def_connect_state = False
    
    label_Client_mock = Mock()
    label_Client_mock.config(text="connect")
    
    root = Tk()
    
    Queue.get.return_value = None
    
    asyncio.create_task(assembler.Assembler_connect(label_Client_mock,root))
    
    #########################################################################
    
    assert assembler.second_window is True