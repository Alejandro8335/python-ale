# pytest "c:\Users\gabri\OneDrive\Desktop\ALE\python-ale\tkinter\proyectos\calculadora\test_individuales_calculadora.py"
import pytest
import re
@pytest.mark.parametrize("entry, resultado_esperado",[
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
def test_agregar_punto(entry, resultado_esperado):
    str_ = entry
    # Verifica que no termine en operador
    if str_ and str_[-1] not in "+-*/%.()":
        # Toma el último elemento de la lista que se va a dividir por +\-*/%
        ultimo_numero = re.split(r"[+\-*/%]", str_)[-1]
        # verifica que el elemnto no tenga punto
        if "." not in ultimo_numero:
            str_ += "."
    assert str_ == resultado_esperado

@pytest.mark.parametrize("signo,entry, resultado_esperado",[
    ("+","5-","5"),
    ("/","-5","-5/"),
    ("*","95*84/","95*84*")])
def test_operaciones(signo,entry,resultado_esperado):
    str_ = entry
    if (signo == "+")and str_ and (str_[-1] == "-"): # saca el signo - si se pone +
        str_ = str_[:-1]
            
    elif str_:
        match str_:
            case x if (x[-1] in "+-*/%.("):  # Evita operadores consecutivos
                if len(x) > 1 and not (x[-2] in "+-*/%."):
                    str_ = str_[:-1]
                    str_ += signo

            case _: # Caso general
                str_ += signo
    assert str_ == resultado_esperado
@pytest.mark.parametrize("entry, resultado_esperado",[
    ("","-"),
    ("-15*","-15*-"),
    ("15+","15-")])
def test_sustraccion(entry,resultado_esperado):
    # Permite el signo negativo al inicio pero evalua que no se repitan los signos -
    match entry:
        case x if x and x[-1] == "+":
            entry = entry[:-1]
            entry += "-"
        case x if x == "" or x[-1] != "-":
            entry += "-"
    assert entry == resultado_esperado

@pytest.mark.parametrize("entry, resultado_esperado",[
    ("","("),
    ("9","9("),
    ("(10","(10)"),
    ("15*","15*("),
    ("(20/","(20/("),
    ("100.","100("),
    ("(100.","(100)")])
def test_agregar_parentesis(entry,resultado_esperado):
    str_ = entry
    if str_:
        bool_count = str_.count("(") > str_.count(")")
        match str_:
            case x if (x[-1] not in "+-*/%.(") and bool_count:
                entry += ")"

            case x if x[-1] == ".":
                entry = entry[:-1]
                if bool_count:
                    entry += ")"
                else:
                    entry += "("
            case _:
                entry += "("

    else:
        entry += "("
    assert entry == resultado_esperado

@pytest.mark.parametrize("entry,contenido_antes_eval,resultado_despues_eval",[
    ("1.0","1.0","1"),
    ("1","1","1"),
    ("1.5","1.5","1.5"),
    ("8%(9)","8/100*(9)","0.72"),
    ("((((9))))","((((9))))","9"),
    ("(((15+5","(((15+5)))","20"),
    ("1.5)))","(((1.5)))","1.5"),
    ("(9)8+5)","((9)*8+5)","77")])
def test_calcular(entry,contenido_antes_eval,resultado_despues_eval):
    contenido = entry
    # cierra los parentesis abiertos
    falta_parentesis = contenido.count("(") - contenido.count(")")
    if falta_parentesis > 0:
        contenido += ")"*falta_parentesis
    else:
        contenido = "("*(falta_parentesis*-1) + contenido
    for i in reversed(list(re.finditer(r"(\d+|\))\(", contenido))):# devuelve objetos Match
        pos = i.start() + len(i.group(1))# devuelve un número entero
        contenido = contenido[:pos] + "*" + contenido[pos:]
    for i in reversed(list(re.finditer(r"\)\d+", contenido))):
        pos = i.start() + 1
        contenido = contenido[:pos] + "*" + contenido[pos:]


    # porcentajes
    for i in reversed(list(re.finditer(r"(\d+|\))%", contenido))):
        pos = i.start() + len(i.group(1))
        contenido = contenido[:pos] + "/100*" + contenido[pos+1:]#con + 1 me desplazo un caracter para eliminarlo (%)
        # % = /100 se pone al final de la expresion
    assert contenido == contenido_antes_eval
    resultado = eval(contenido)# interpreta el contenido de la cadena como si fuera código Python y lo ejecuta en tiempo real.
    if resultado % 1 == 0:
        resultado = int(resultado)
    else:
        pass
    assert str(resultado) == resultado_despues_eval