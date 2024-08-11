from tkinter import *

# Creacion de la ventana y del frame con su tamanio
ventana = Tk()
ventana.title ('Configuración')

frame = Frame()
frame.pack()
frame.config(width='450', height= '300')

#Creacion de etiquetas de texto (labes)
Label(frame, text = 'Ingrese los parámetros de calificación', font= ('Arial 13 bold')).place(x=75, y=25)
Label(frame, text = 'Calificación mínima:', font= ('Arial 12')).place(x=85, y=80)
Label(frame, text = 'Calificación máxima:', font= ('Arial 12')).place(x=85, y=120)
Label(frame, text = 'Calificación para aprobar:', font= ('Arial 12')).place(x=85, y=160)

#Creacion de entradas de texto 
entradaNotaMinima = Entry(frame, width=10,)
entradaNotaMinima.place(x=290, y=82)
entradaNotaMinima.config(justify=CENTER)

entradaNotaMaxima = Entry(frame, width=10)
entradaNotaMaxima.place(x=290, y=122)
entradaNotaMaxima.config(justify=CENTER)

entradaNotaAprobacion = Entry(frame, width=10)
entradaNotaAprobacion.place(x=290, y=162)
entradaNotaAprobacion.config(justify=CENTER)

#Funcion que permite borrar los datos de los campos Entry
def borrarDatos():
    entradaNotaMinima.delete(0,END)
    entradaNotaMaxima.delete(0,END)
    entradaNotaAprobacion.delete(0,END)

#Funcion que permite almacenar los datos que estan en las entradas de texto en variables e imprime su contenido
def guardarDatos():
    valorNotaminima = entradaNotaMinima.get()
    valorNotamaxima = entradaNotaMaxima.get()
    valorNotaAprobacion = entradaNotaAprobacion.get()

    notaMinima = float(valorNotaminima)
    notaMaxima = float(valorNotamaxima)
    notaAprobacion = float(valorNotaAprobacion)

    print (notaAprobacion, notaMinima, notaMaxima)
    
#Creacion de botones borrar y guardar    
botonBorrar = Button(frame, text='Borrar', height= 2, width= 10, command=borrarDatos)
botonBorrar.place(x=140, y=222)

botonAceptar = Button(frame, text='Aceptar', height= 2, width= 10, command= guardarDatos)
botonAceptar.place(x=228, y=222)


ventana.mainloop()