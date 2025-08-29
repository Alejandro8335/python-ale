
import csv

with open("C:/Users/gabri/OneDrive/Desktop/ALE/python=ale/csv.txt")as archivo:
    leer = csv.reader(archivo)
    for r in leer:
        print(r)