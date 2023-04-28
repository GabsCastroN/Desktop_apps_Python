from tkinter import *
from tkinter import messagebox

#---------------------------------------------------------------------------------------------------------------
#Funciones App
#Ventana Principal  App
#---------------------------------------------------------------------------------------------------------------
#sumar
def sumar():
    pass
#borrar
def borrar():
    pass
#salir
def salir():
    messagebox.showinfo("Suma Enteros 1.0", "La app se va a cerrar")
    ventana_principal.destroy()

#Se Aclara Una Variable Llamada Ventana_Principal
ventana_principal = Tk()

#Titulo

ventana_principal.title("MonekyLand")
#Tamaño
ventana_principal.geometry("500x500")
#NoMaximizar? pipipipi
ventana_principal.resizable(False,False)
#Color
ventana_principal.config(bg="darkorchid")
#Frame Extra
frame_entrada= Frame (ventana_principal)
frame_entrada.config(bg="white", width=480, height=180,)
frame_entrada.place(x=10, y=10)

frame_operaciones = Frame (ventana_principal)
frame_operaciones.config(bg="white", width=480, height=125,)
frame_operaciones.place(x=10, y=200)

frame_resultado= Frame (ventana_principal)
frame_resultado.config(bg="white", width=480, height=155,)
frame_resultado.place(x=10, y=335)

#logo
logo=PhotoImage(file="img/escudo_colegio.png")
lb_logo = Label(frame_entrada, image=logo, bg=("white"))
lb_logo.place(x=70,y=40)

#titulo
titulo = Label (frame_entrada, text="Suma Enteros 1.0")
titulo.config(bg='White', fg="black", font="Arial, 16")
titulo.place(x=240, y=10)

#
lb_x = Label(frame_entrada, text = ("X = "))
lb_x.config(bg="white", fg=("blue"), font=("Helvetica", 18))
lb_x. place(x=240, y=60)

#caja de texto
entry_x = Entry(frame_entrada)
entry_x.config(bg="white", fg="blue", font=("times new roman", 18), width=6)
entry_x.place(x=290, y=60)
entry_x.focus_set()

entry_y = Entry(frame_entrada)
entry_y.config(bg="white", fg="blue", font=("times new roman", 18), width=6)
entry_y.place(x=290, y=120)
entry_y.focus_set()

lb_y = Label(frame_entrada, text = ("Y = "))
lb_y.config(bg="white", fg=("blue"), font=("Comic Sans", 18))
lb_y. place(x=240, y=120)

#boton sumar
bt_sumar = Button(frame_operaciones, text="sumar", command=sumar)
bt_sumar.place(x=45,y=35, width=100,height=30)

#boton borrar
bt_borrar = Button (frame_operaciones, text="Borrar", command=borrar)
bt_borrar.place(x=190, y=35, width= 100, heigh=30)

#boton salir
bt_salir = Button(frame_operaciones, text="Salir", command= salir)
bt_salir.place (x=335, y=35, width=100, height=30 )

#area de texo para los resultados
t_resultados = Text(frame_resultado)
t_resultados.config(bg="black", fg="green2", font=("courier, 20"))
t_resultados.place(x=10, y=10, width=460, height=160)
#Run
ventana_principal.mainloop()
