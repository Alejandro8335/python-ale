#control de las excepciones adentro de un bucle while

while True:
    try:
        numero0 = int(input("dame un numero y te lo sumo: "))
        numero1 = int(input("dame un numero y te lo sumo: "))
        resultado = numero0 + numero1
        print(resultado)
        break
    except: 
        print("solo numeros")
    
    finally:
        print("el bucle termino")
        
#El bloque try se usa para probar un fragmento de código que podría lanzar un error 
#(excepción) mientras se ejecuta.

#La idea es: “intenta ejecutar esto… y si algo sale mal, pasa al plan B” (que normalmente está en except).

#Debe ir siempre acompañado de al menos un except o un finally (o ambos).