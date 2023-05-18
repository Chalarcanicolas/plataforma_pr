from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk

def abrir_nueva_ventana2():
    nueva_ventana = Toplevel()
    nueva_ventana.title("Bases_de_datos")
    nueva_ventana.geometry("600x500")
    nueva_ventana.resizable(False, False)
    nueva_ventana.config(bg="cornflower blue")

    lb_cognitivo = Label(nueva_ventana, text="Peso = ", bg="white", fg="blue", font=("Helvetica", 18))
    lb_cognitivo.place(x=40, y=250)
    entry_cognitivo = Entry(nueva_ventana, bg="white", fg="blue", font=("Times New Roman", 15), width=6)
    entry_cognitivo.focus_set()
    entry_cognitivo.place(x=125, y=250)

    lb_cognitivo = Label(nueva_ventana, text="Altura = ", bg="white", fg="blue", font=("Helvetica", 18))
    lb_cognitivo.place(x=40, y=280)
    entry_cognitivo = Entry(nueva_ventana, bg="white", fg="blue", font=("Times New Roman", 15), width=6)
    entry_cognitivo.focus_set()
    entry_cognitivo.place(x=135, y=280)

def abrir_nueva_ventana():
    nueva_ventana = Toplevel()
    nueva_ventana.title("Bases_de_datos")
    nueva_ventana.geometry("600x500")
    nueva_ventana.resizable(False, False)
    nueva_ventana.config(bg="cornflower blue")

    lista_desplegable = ttk.Combobox(nueva_ventana, width=20)
    lista_desplegable.place (x=50, y=50)
        
    opciones = ["Estadistica", "Trigonometria y Geometria Analitica", "Valores", "Filosofia", "Lengua Castellana", "Ingles", "Artistica", "Quimica", "Fisica", "Ed.Fisica", "Ed.Religiosa", "Sociales", "Politica"]
    lista_desplegable["values"]=opciones
    # cognitivo
    lb_cognitivo = Label(nueva_ventana, text="Cognitivo 30% = ", bg="white", fg="blue", font=("Helvetica", 18))
    lb_cognitivo.place(x=40, y=250)
    entry_cognitivo = Entry(nueva_ventana, bg="white", fg="blue", font=("Times New Roman", 15), width=6)
    entry_cognitivo.focus_set()
    entry_cognitivo.place(x=225, y=250)
#     procedimental
    lb_procedimental = Label(nueva_ventana, text="procedimental 30% = ", bg="white", fg="blue", font=("Helvetica", 18))
    lb_procedimental.place(x=40, y=280)
    entry_procedimental = Entry(nueva_ventana, bg="white", fg="blue", font=("Times New Roman", 15), width=6)
    entry_procedimental.focus_set()
    entry_procedimental.place(x=275, y=280)
    # actitudinal
    lb_actitudinal = Label(nueva_ventana, text="actitudinal 10% = ", bg="white", fg="blue", font=("Helvetica", 18))
    lb_actitudinal.place(x=40, y=310)
    entry_actitudinal = Entry(nueva_ventana, bg="white", fg="blue", font=("Times New Roman", 15), width=6)
    entry_actitudinal.focus_set()
    entry_actitudinal.place(x=225, y=310)
    # autoevaluacion
    lb_autoevaluacion = Label(nueva_ventana, text="autoevaluacion 10% = ", bg="white", fg="blue", font=("Helvetica", 18))
    lb_autoevaluacion.place(x=40, y=340)
    entry_autoevaluacion = Entry(nueva_ventana, bg="white", fg="blue", font=("Times New Roman", 15), width=6)
    entry_autoevaluacion.focus_set()
    entry_autoevaluacion.place(x=275, y=340)
    # bimestral
    lb_bimestral = Label(nueva_ventana, text="bimestral 20% = ", bg="white", fg="blue", font=("Helvetica", 18))
    lb_bimestral.place(x=40, y=370)
    entry_bimestral = Entry(nueva_ventana, bg="white", fg="blue", font=("Times New Roman", 15), width=6)
    entry_bimestral.focus_set()
    entry_bimestral.place(x=220, y=370)

    # boton para convertir
    bt_convertir = Button(nueva_ventana,text="Calcular", command=convertir)
    bt_convertir.place(x=220, y=410, width=150, height=100)

# funcion de calcular la nota definitiva
def convertir():
        messagebox.showinfo("Nota Difinitiva", "Operacion realizada")

        # variables notas
        entry_proce_def = float(entry_procedimental.get())
        entry_cog_def = float(entry_cognitivo.get())
        entry_auto_def = float(entry_autoevaluacion.get())
        entry_acti_def = float(entry_actitudinal.get())
        entry_bime_def = float(entry_bimestral.get())

        entry_not_final = (0.3*entry_proce_def) + (0.3*entry_cog_def) + (0.1*entry_auto_def) + (0.1*entry_acti_def) + (0.2*entry_bime_def)

        if entry_not_final < 30:
                messagebox.showinfo("Resultado", "El alumno reprobo la asignatura  xd  "+str(entry_not_final))
        else:
                messagebox.showinfo("Resultado", "El alumno aprobo la asignatura xd  "+str(entry_not_final))

            

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
lb_logo = Label(frame_entrada, bg="white")
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

# Botón de ingresar a las notas
btn_ingresar = Button(frame_entrada, text="Ingresar nts", command=abrir_nueva_ventana, bg="blue", fg="white", font=("Helvetica", 16))
btn_ingresar.place(x=150, y=350)

# Boton de ingresar al imc
btn_ingresar = Button(frame_entrada, text="Ingresar al imc", command=abrir_nueva_ventana2, bg="blue", fg="white", font=("Helvetica", 16))
btn_ingresar.place(x=290, y=350)
# Ejecutar el bucle de la aplicación
ventana_principal.mainloop()