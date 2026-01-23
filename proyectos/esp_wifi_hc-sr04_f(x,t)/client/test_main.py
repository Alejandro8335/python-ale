from unittest.mock import Mock
from A_main import tk_loop, pump_asyncio
import tkinter as tk
import pytest
import asyncio

# pytest "C:\Users\gabri\OneDrive\Desktop\ALE\python-ale\proyectos\esp_wifi_hc-sr04_f(x,t)\client\test_main.py"

def test_tk_loop():
    assembler = Mock();root = Mock();label_Client = Mock()
    client = Mock();graph = Mock();bts = Mock()
    
    set_bts = {"Graph close" : bts}
    graph.open_state = True
    client.connect_state = True
    assembler._running = False
    tk_loop(assembler,root, label_Client, client ,graph,set_bts)
    
    graph.fig.canvas.draw_idle.assert_called_once()
    label_Client.config.assert_called_once_with(text="connect")
    
    label_Client.reset_mock()
    
    graph.open_state = False
    client.connect_state = False
    assembler._running = True
    
    tk_loop(assembler,root, label_Client, client ,graph,set_bts)
    
    graph.fig.canvas.draw_idle.assert_called_once()
    label_Client.config.assert_called_once_with(text="disconnect")
    root.after.assert_called_once()
        
def test_pump_asyncio():
    assembler = Mock(); loop = Mock(); root = Mock()
    assembler._running = False
    
    assert pump_asyncio(assembler , loop,root) is True
    
    loop.call_soon.assert_not_called()
    loop.run_forever.assert_not_called()
    root.after.assert_not_called()
    
    ################################################################
    assembler._running = True
    
    loop.call_soon.side_effect = RuntimeError
    
    assert pump_asyncio(assembler , loop,root) is False
    
    root.after.assert_not_called()
    
    ################################################################
    loop.reset_mock()
    loop.call_soon.side_effect = None
    assembler._running = True
    
    pump_asyncio(assembler , loop, root)
    
    loop.call_soon.assert_called_once_with(loop.stop)
    loop.run_forever.assert_called_once()
    root.after.assert_called_once()