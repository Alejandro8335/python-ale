def Input_binario():
    str_bi = input("ingrese un numero binario: ")
    return str_bi

def Binario(x):
    decimal = 0
    for i in x:
        decimal = decimal * 2 + int(i)#multublicas por la base
    print(decimal)
        
x = Input_binario()
Binario(x)