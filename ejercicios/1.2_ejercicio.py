#A)pedirle al usuario que diga cualquier texto real y :
#calcular cuanto tardaria en decir esa (1g=2p)
#cuantas palabras digo?
#B)si se tarda mas de 1 min
#decirle "para flaco no te pedi un testamento"
#C)cuanto tardaria si hablan 30% mas rapido?

#A)
texto= input("decime un frace:  ")
palabras = texto.split(" ")
contando_palabras = len(palabras)
cuanto_tardarias = contando_palabras//2
print(f"digiste {contando_palabras} palabras")
print(f"tardarias {cuanto_tardarias} segundoo")

#B)
if cuanto_tardarias >= 60:
    print("para flaco no te pedi un testamento")

#hola soy ale ¿como estas? ¿que haces aca?
#C)
mas_rapido =  contando_palabras*100//2*1.3 /100
print(F"si lo decis un 30% mas rapido tardarias{mas_rapido}")