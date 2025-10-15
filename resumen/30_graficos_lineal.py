
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/gabri/OneDrive/Desktop/ALE/python-ale/te.txt")

sns.lineplot(x="fechas",y="te",data=df)

plt.plot("01-09",17,"o")

plt.show()

# resumen de las librerias

# 📊 pandas
# Sirve para manejar datos estructurados, como tablas o archivos CSV.

# Te permite leer, filtrar, agrupar, ordenar y transformar datos fácilmente.

# Ideal para análisis de datos, estadísticas y preparación de información para gráficos.


# 📈 matplotlib.pyplot
# Es la librería base para crear gráficos en Python.

# Podés hacer gráficos de líneas, barras, tortas, dispersión, etc.

# Muy personalizable, aunque más manual que otras librerías.

# 🎨 seaborn
# Se basa en matplotlib, pero con estilos más modernos y gráficos más fáciles de crear.

# Se integra muy bien con pandas para graficar directamente desde un DataFrame.

# Ideal para visualizaciones estadísticas (correlaciones, distribuciones, boxplots, etc.)