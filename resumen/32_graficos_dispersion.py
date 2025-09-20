
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/gabri/OneDrive/Desktop/ALE/python-ale/grafico_dispersion.txt")

#creando el grafico
sns.scatterplot (x="tiempo",y="dinero",data=df)
 
#mostrando el grafico
plt.show()