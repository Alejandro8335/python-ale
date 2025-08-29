
#2 listas una con nombres y otra con apellidos 
nombres = ["ale","alex","alexandre","alejandro","alejo"]
apellidos = ["dominguez","dalto","zing","papa","pa"]

#registrar esta informacion en un txt de forma optima 
with open("nombre_apelidos.txt","w") as arch:
    arch.writelines("los datos son:\n\n")
    [arch.writelines(f"nombre: {n}\napellidos: {a}\n-------------\n")for n,a in zip(nombres,apellidos)]
    