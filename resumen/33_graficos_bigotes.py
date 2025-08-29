
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/gabri/OneDrive/Desktop/ALE/python=ale/grafico_bigotes.txt")

#creando el grafico
sns.boxplot(x="categoria",y="valor",data=df)
 
#mostrando el grafico
plt.show() 