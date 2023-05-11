#---------------------------------
# Desktop app No. 2- Temperatura
#---------------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

#-------------------------
# funciones de la app
#-------------------------




#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Plataforma 1.0")

# tamaño de la ventana
ventana_principal.geometry("500x500")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="black")

#--------------------------------
# variables globales
#--------------------------------
c = StringVar()
kf = StringVar()
global logo

#--------------------------------
# frame entrada datos
#--------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=480)
frame_entrada.place(x=10, y=10)

# logo de la app
logo = PhotoImage(file="IMG/escudo_colegio.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=200,y=40)

# titulo de la app
titulo = Label(frame_entrada, text="Por favor ingrese sus datos")
titulo.config(bg = "white",fg="blue", font=("Helvetica", 20))
titulo.place(x=100,y=10)

# ingrese su nombre
lb_c = Label(frame_entrada, text = "Nombre = ")
lb_c.config(bg="white", fg="blue", font=("Helvetica", 18))
lb_c.place(x=40, y=240)

# caja del nombre
entry_c = Entry(frame_entrada, textvariable=c)
entry_c.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
entry_c.focus_set()
entry_c.place(x=155,y=240)

# ingrese su grado
lb_c = Label(frame_entrada, text = "Grado = ")
lb_c.config(bg="white", fg="blue", font=("Helvetica", 18))
lb_c.place(x=40, y=240)

# caja del nombre
entry_c = Entry(frame_entrada, textvariable=c)
entry_c.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
entry_c.focus_set()
entry_c.place(x=155,y=240)
# run
# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc).  Cada acción del usuario se conoce como un evento.  El método mainloop() es un bucle infinito.
ventana_principal.mainloop()