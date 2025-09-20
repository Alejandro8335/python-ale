
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python-ale\\grafico_barras.txt")

#creando el grafico
sns.barplot(x="fuente",y="ingresos",data=df)

#obteniendo el total de ingresos
total = df["ingresos"].sum()

#mostrando el total
print(f"el total de ingresos es {total}")
 
#mostrando el grafico
plt.show()