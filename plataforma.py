from tkinter import *
from tkinter import messagebox

def abrir_nueva_ventana():
    nueva_ventana = Toplevel()
    nueva_ventana.title("Bases_de_datos")
    nueva_ventana.geometry("600x500")
    nueva_ventana.resizable(False, False)
    nueva_ventana.config(bg="cornflower blue")

    frame_entrada1 = Label(nueva_ventana, bg="cornflower blue", width=580, height=480)
    frame_entrada1.place(x=10, y=10)
# cognitivo
    lb_cognitivo = Label(nueva_ventana, text="Cognitivo 30% = ", bg="white", fg="blue", font=("Helvetica", 18))
    lb_cognitivo.place(x=40, y=250)
    entry_cognitivo = Entry(nueva_ventana, bg="white", fg="blue", font=("Times New Roman", 15), width=6)
    entry_cognitivo.focus_set()
    entry_cognitivo.place(x=225, y=250)
# procedimental
    lb_nombre = Label(nueva_ventana, text="procedimental 30% = ", bg="white", fg="blue", font=("Helvetica", 18))
    lb_nombre.place(x=40, y=280)
    entry_nombre = Entry(nueva_ventana, bg="white", fg="blue", font=("Times New Roman", 15), width=6)
    entry_nombre.focus_set()
    entry_nombre.place(x=275, y=280)
# actitudinal
    lb_nombre = Label(nueva_ventana, text="actitudinal 10% = ", bg="white", fg="blue", font=("Helvetica", 18))
    lb_nombre.place(x=40, y=310)
    entry_nombre = Entry(nueva_ventana, bg="white", fg="blue", font=("Times New Roman", 15), width=6)
    entry_nombre.focus_set()
    entry_nombre.place(x=225, y=310)
# autoevaluacion
    lb_nombre = Label(nueva_ventana, text="autoevaluacion 10% = ", bg="white", fg="blue", font=("Helvetica", 18))
    lb_nombre.place(x=40, y=340)
    entry_nombre = Entry(nueva_ventana, bg="white", fg="blue", font=("Times New Roman", 15), width=6)
    entry_nombre.focus_set()
    entry_nombre.place(x=275, y=340)
# bimestral
    lb_nombre = Label(nueva_ventana, text="bimestral 20% = ", bg="white", fg="blue", font=("Helvetica", 18))
    lb_nombre.place(x=40, y=370)
    entry_nombre = Entry(nueva_ventana, bg="white", fg="blue", font=("Times New Roman", 15), width=6)
    entry_nombre.focus_set()
    entry_nombre.place(x=220, y=370)


# Ventana principal de la app
ventana_principal = Tk()
ventana_principal.title("Plataforma 1.0")
ventana_principal.geometry("500x500")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="black")


# Frame de entrada de datos
frame_entrada = Label(ventana_principal, bg="white", width=480, height=480)
frame_entrada.place(x=10, y=10)

# Logo de la app
logo = PhotoImage(file="IMG/escudo_colegio.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=200, y=40)

# Título de la app
titulo = Label(frame_entrada, text="Por favor ingrese sus datos", bg="white", fg="blue", font=("Helvetica", 20))
titulo.place(x=100, y=10)

# Ingrese su nombre
lb_nombre = Label(frame_entrada, text="Nombre = ", bg="white", fg="blue", font=("Helvetica", 18))
lb_nombre.place(x=40, y=290)

# Caja del nombre
entry_nombre = Entry(frame_entrada, bg="white", fg="blue", font=("Times New Roman", 18), width=6)
entry_nombre.focus_set()
entry_nombre.place(x=155, y=290)

# Ingrese su grado
lb_grado = Label(frame_entrada, text="Grado = ", bg="white", fg="blue", font=("Helvetica", 18))
lb_grado.place(x=40, y=240)

# Caja del grado
entry_grado = Entry(frame_entrada, bg="white", fg="blue", font=("Times New Roman", 18), width=6)
entry_grado.focus_set()
entry_grado.place(x=155, y=240)

# Botón de ingresar
btn_ingresar = Button(frame_entrada, text="Ingresar", command=abrir_nueva_ventana, bg="blue", fg="white", font=("Helvetica", 16))
btn_ingresar.place(x=200, y=350)

# Ejecutar el bucle de la aplicación
ventana_principal.mainloop()