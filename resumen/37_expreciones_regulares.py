
import re

texto = "the quick brawm fox jumps over the lazy dog"

x = re.search("^the.*dog$",texto)

if x:
    print("si")
else:
    print("no")
    
#(^the) indica que debe comenzar con "the".

# (.*) significa que puede haber cualquier cantidad de caracteres entre "the" y "dog".

# (dog$) indica que debe terminar en "dog".