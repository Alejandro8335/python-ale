
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/gabri/OneDrive/Desktop/ALE/python-ale/te.txt")

sns.lineplot(x="fechas",y="te",data=df)

plt.plot("01-09",17,"o")

plt.show()
