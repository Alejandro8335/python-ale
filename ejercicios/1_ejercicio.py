#A)
#promedio de duracion de los curso
otros_min = 2.5
otros_max = 7
otros_promedio = 4
dalto = 1.5

#diferencia de duracion
diferencia_min =100 - dalto*1000//otros_min /10
diferencia_max =100 - dalto * 1000//otros_max / 10
diferencia_pro =100 - dalto*1000//otros_promedio / 10
print("-----------------------")
print(f"el curso de dalto dura un {diferencia_min}% menos que el mas rapido")
print(f"el curso de dalto dura un {diferencia_max}% menos que el mas lento")
print(f"el curso de dalto dura un {diferencia_pro}% menos que el promedio")
print("-----------------------")

#B)
#duracion de crudos
crudo_dalto = 3.5
crudo_pro = 5
#calculando el porcentaje en crudo
vacio_pro =100 - otros_promedio*1000//crudo_pro/ 10
vacio_dalto = 100 - dalto*1000 // crudo_dalto/10
print(F"un curso promedio elimina un{vacio_pro}% de tiempo vacio")
print(f"este curso elimina el {vacio_dalto}% de tiempo vacio")
print("-----------------------")

#C) 
#mostrando diferencias si los cursos duran 10h
print(f"ver 10h de este curso equivale a ver {otros_promedio*100 // dalto/10}horas de otros cursos")
print(f"ver 10h de otros cursos equivale a ver {dalto*100 // otros_promedio/ 10}")
print("-----------------------")