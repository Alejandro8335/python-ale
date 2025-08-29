
#lsp,Principio de Sustitución de Liskov
#liskov's substitution principle

#class ave:
    ##return "estoy volando"
     
#class pinguino(ave):
    ##return "no puedo volas"
    
#def hacer_volar(ave = ave):
    #return ave.volar()

#print(hacer_volar(pinguino()))

class Ave:
    pass
class Ave_voladora(Ave):
    def valor(self):
        return "estoy volando"
    
class Ave_no_voladora(Ave):
    pass

#"Los objetos de una clase derivada deben poder reemplazar objetos de su clase base sin alterar el correcto 
# funcionamiento del programa."

#En otras palabras, si una clase B hereda de una clase A, cualquier instancia de B debe poder usarse en lugar 
#de una instancia de A sin causar errores o cambios inesperados en el comportamiento