
import pandas as pd
df = pd.read_csv("C:/Users/gabri/OneDrive/Desktop/ALE/python=ale/csv.txt")#names = ["nombre","apellido","edad"]

nombre = df["nombre"] 

#ordenamos el dataframe por edad
orden = df.sort_values("edad")

#ordenando de forma desendente
orden2 = df.sort_values("edad",ascending=False)

#concatenando los 2 dataframes
concatenar = pd.concat([df,df])

#accediendo a la primer fila con head()
primer = df.head(2)

#accediendo a las ultimas 3 filas con tail()
ultima = df.tail(2)

#accediendo a la cantidad de filas y columnas con shape
filas_columnas = df.shape

#desempaquetando
filas,columnas = df.shape

filas1 = df.shape[0]

#obteniendo data estadistica del dataframe 
inf = df.describe()

#accediendo a un alemento especifico del df con loc
elemento =  df.loc[2,"edad"]

#accediendo a un alemento especifico del df con loc
elemento1 =  df.iloc[2,2]

#accediendoa todas las filas de una  columna
apellidos = df.loc[:,"apellido"]

#accediendoa todas las filas de una  columna
apellidos1 = df.iloc[:,1]

#accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]

#accediendo a la fila 3 con loc
fila_4 = df.iloc[2,:]#es lo mismo

#accediendo a filas con edad mayor que 30                
mayor = df.loc[df["edad"]>30,:]

print(mayor)

# En términos simples, te permite trabajar con estructuras como:
# Series: una lista de datos con etiquetas, como una columna de Excel.
# DataFrame: una tabla entera, con filas y columnas etiquetadas.

# Con pandas podés:
# Leer y escribir archivos como CSV, Excel, JSON, etc.
# Filtrar, ordenar y agrupar información fácilmente.
# Aplicar operaciones matemáticas o estadísticas en columnas enteras.
# Preparar datos para visualizaciones o modelos de machine learning.