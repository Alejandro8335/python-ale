import re

texto = "hola ale,mi numero es: +54 11 4321-4321"

patron = r"\+\d{2}\s\d{2}\s\d{4}-\d{4}"

remplazo = re.sub(patron,"numero oculto",texto)

print(remplazo)