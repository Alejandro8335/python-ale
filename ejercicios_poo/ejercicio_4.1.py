
#hay que profundisar mas en esto

from textblob import TextBlob

class Analizar_Sentimientos:
    def analizar_sentimiento(self, texto):
        analisis = TextBlob(texto)
        if analisis.sentiment.polarity > 0:
            return "positivo"
        elif analisis.sentiment.polarity == 0:
            return "neutral"
        else:
            return "negativo"
        
analizador = Analizar_Sentimientos()
resultado = analizador.analizar_sentimiento("prime")
print(resultado)
