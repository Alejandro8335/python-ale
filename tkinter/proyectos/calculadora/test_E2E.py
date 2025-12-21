# pytest "C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python-ale\\tkinter\\proyectos\\calculadora\\test_E2E.py"
import pytest 
from calculadora import *
import tkinter as tk

@pytest.fixture()
def window_fixture():
    ventana , set_bts ,entry = crear_ventana()
    entry.delete(0, tk.END)
    yield entry ,set_bts
    entry.delete(0, tk.END)
    ventana.destroy()

def test_clear_AC(window_fixture):
    entry , set_bts = window_fixture
    entry.insert(0, "1000")
    set_bts["AC"].invoke()
    assert entry.get() == ""

def test_borrar(window_fixture):
    entry , set_bts = window_fixture
    entry.insert(0, "1234")
    set_bts["⌫"].invoke()
    assert entry.get() == "123"

def test_bts_num(window_fixture):
    entry , set_bts = window_fixture
    for num in range(10):
        set_bts[str(num)].invoke()
    assert entry.get() == "0123456789"

@pytest.mark.parametrize("insert_entry, resultado_esperado",[
    ("","-"),
    ("-15*","-15*-"),
    ("15+","15-"),
    ("50-","50-")])
def test_sustraccion(window_fixture,insert_entry,resultado_esperado):
    entry , set_bts = window_fixture
    entry.insert(tk.END,insert_entry)
    set_bts["-"].invoke()
    assert entry.get() == resultado_esperado

@pytest.mark.parametrize("insert_entry, resultado_esperado",[
    ("","("),
    ("9","9("),
    ("(10","(10)"),
    ("15*","15*("),
    ("(20/","(20/("),
    ("100.","100("),
    ("(100.","(100)")])
def test_agregar_parentesis(window_fixture,insert_entry,resultado_esperado):
    entry , set_bts = window_fixture
    entry.insert(tk.END,insert_entry)
    set_bts["(  )"].invoke()
    assert entry.get() == resultado_esperado

@pytest.mark.parametrize("signo,insert_entry, resultado_esperado",[
    ("%","",""),
    ("+","5-","5"),
    ("/","-5","-5/"),
    ("*","95*84/","95*84*")])
def test_operaciones(window_fixture,signo,insert_entry,resultado_esperado):
    entry , set_bts = window_fixture
    entry.insert(tk.END,insert_entry)
    set_bts[signo].invoke()
    assert entry.get() == resultado_esperado
    
@pytest.mark.parametrize("insert_entry, resultado_esperado",[
    ("",""),
    ("4+","4+"),
    ("5-","5-"),
    ("6*","6*"),
    ("7/","7/"),
    ("8%","8%"),
    ("9.","9."),
    ("10)","10)"),
    ("11(","11("),
    ("3.14","3.14"),
    ("12","12.")])
def test_agregar_punto(window_fixture,insert_entry,resultado_esperado):
    entry , set_bts = window_fixture
    entry.insert(tk.END,insert_entry)
    set_bts["."].invoke()
    assert entry.get() == resultado_esperado
    
@pytest.mark.parametrize("insert_entry,resultado_esperado",[
    ("",""),
    ("1.0","1"),
    ("1","1"),
    ("1.5","1.5"),
    ("8%(9)","0.72"),
    ("((((9))))","9"),
    ("(((15+5","20"),
    ("1.5)))","1.5"),
    ("(9)8+5)","77")])
def test_calcular(window_fixture,insert_entry,resultado_esperado):
    entry , set_bts = window_fixture
    entry.insert(tk.END,insert_entry)
    set_bts["="].invoke()
    assert entry.get() == resultado_esperado