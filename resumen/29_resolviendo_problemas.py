
import pandas as pd
df = pd.read_csv("C:/Users/gabri/OneDrive/Desktop/ALE/python=ale/csv.txt")

#comvertira string los datos de una calumna
df["edad"] = df["edad"].astype(str)  

#mostrando el tipo de dato del primer elemento de la columna edad
#print(type(df["edad"][0]))

#remplazando los datos "ale" por "maestro"
df["nombre"].replace("ale","maestro",inplace=True)

#eliminando las filas con datos faltantes
df = df.dropna()

#eliminando las filas repetidas
df = df.drop_duplicates()

#creando un csv con el dataframe resultante (limpio)
df.to_csv("C:/Users/gabri/OneDrive/Desktop/ALE/python=ale/csv.limpio.txt")