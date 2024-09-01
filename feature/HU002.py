import tkinter as tk 
from tkinter import messagebox

ventana_UV= tk.Tk()
ventana_UV.title("Formulario de notas")
##ventana_UV.geometry("520x480")##

tk.Label(ventana_UV, text= "Nombre").grid(row= 0, column= 0, padx= 10, pady= 5)
entrada_Nombre= tk.Entry(ventana_UV, width= 30)
entrada_Nombre.grid (row= 0, column= 1, padx= 10, pady= 5, sticky= "w")

tk.Label(ventana_UV, text="Descipción").grid(row= 1, column= 0, padx= 10, pady= 5)
entrada_Descripcion = tk.Entry(ventana_UV, width= 30)
entrada_Descripcion.grid(row= 1, column= 1, padx= 10, pady= 5, sticky= "w")

tk.Label(ventana_UV, text="Semestre").grid(row= 2, column= 0, padx= 10, pady= 5)
entrada_Semestre = tk.Entry(ventana_UV, width= 20)
entrada_Semestre.grid(row= 2, column= 1, padx= 10, pady= 5, sticky= "w")

tk.Label(ventana_UV, text= "Créditos").grid(row= 3, column= 0, padx= 10, pady= 5)
entrada_Creditos = tk.Entry(ventana_UV, width= 5)
entrada_Creditos.grid(row=3, column= 1, padx= 10, pady= 3, sticky= "w") 

tk.Label(ventana_UV, text= "Nota").grid(row= 4, column= 0, padx= 10, pady= 5)
entrada_Nota = tk.Entry(ventana_UV, width= 5)
entrada_Nota.grid(row=4, column= 1, padx= 10, pady= 3, sticky= "w")

tk.Label(ventana_UV, text="Porcentaje").grid(row=5, column=0, padx=10, pady=5)
entrada_Porcentaje = tk.Entry(ventana_UV, width=5)
entrada_Porcentaje.grid(row=5, column=1, padx=10, pady=3, sticky="w")

materias_Registradas= [] #aquí se almacenarían las materias 

def registrar_Materia():
    nombre= entrada_Nombre.get()
    descripcion= entrada_Descripcion.get()
    semestre= entrada_Semestre.get()
    creditos= int(entrada_Creditos.get())

    materia= {

        "nombre": nombre,
        "descripcion": descripcion,
        "semestre": semestre,
        "creditos": creditos,
        "notas": []
    } #este es un diccionario para los campos de las materias que se registran
    materias_Registradas.append(materia)
    print("Materia registrada:", materia)

def agregar_Nota():
    nombre_materia = entrada_Nombre.get()
    descripcion_nota = entrada_Descripcion.get()
    porcentaje_nota = float(entrada_Porcentaje.get()) 
    nota_obtenida = float(entrada_Nota.get())

    materia = None
    for i in materias_Registradas:
        if i ['nombre'] == nombre_materia:
            materia = i
            break

    total_porcentaje = 0
    for nota in materia['notas']:
        total_porcentaje += nota['porcentaje']

        if total_porcentaje + porcentaje_nota > 100:
            messagebox.showerror("Error", "El porcentaje total no puede exceder el 100%.")
        else:
          materia['notas'].append({
           "descripcion": descripcion_nota,
           "porcentaje": porcentaje_nota,
           "nota_obtenida": nota_obtenida
         })

def calcular_Nota_Final(materia):
    return sum(nota['nota_obtenida'] * (nota['porcentaje'] / 100) for nota in materia['notas'])


def mostrar_Materias():
    ventana_materias = tk.Toplevel(ventana_UV)
    ventana_materias.title("Materias Registradas")

    for i, materia in enumerate(materias_Registradas):
        nota_final = calcular_Nota_Final(materia)
        tk.Label(ventana_materias, text=f"Materia: {materia['nombre']}").grid(row=i, column=0, padx=10, pady=5)
        tk.Label(ventana_materias, text=f"Descripción: {materia['descripcion']}").grid(row=i, column=1, padx=10, pady=5)
        tk.Label(ventana_materias, text=f"Semestre: {materia['semestre']}").grid(row=i, column=2, padx=10, pady=5)
        tk.Label(ventana_materias, text=f"Créditos: {materia['creditos']}").grid(row=i, column=3, padx=10, pady=5)
        tk.Label(ventana_materias, text=f"Nota Final: {nota_final:.2f}").grid(row=i, column=4, padx=10, pady=5)

        print(f"Materia mostrada: {materia}, Nota final: {nota_final:.2f}")

boton_Agregar = tk.Button(ventana_UV, text="Agregar", command= agregar_Nota) 
boton_Agregar.grid(row= 5, column= 2, padx= 10, pady= 4)

boton_Registrar = tk.Button(ventana_UV, text="Registrar", command= registrar_Materia) 
boton_Registrar.grid(row= 6, columnspan= 3, pady= 10)

boton_Mostrar = tk.Button(ventana_UV, text= "Mostrar Materias", command= mostrar_Materias) 
boton_Mostrar.grid(row=7, columnspan=3, pady=10)

ventana_UV.mainloop()





