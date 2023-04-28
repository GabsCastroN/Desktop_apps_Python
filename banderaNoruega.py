from tkinter import *

Ventana_principal = Tk ()

Ventana_principal.title("Noruega")
Ventana_principal.geometry("800x400")
Ventana_principal.resizable(False,False)
Ventana_principal.config(bg="black")

frame_Rojo = Frame (Ventana_principal)
frame_Rojo.config(bg="red", width=800, height=400,)
frame_Rojo.place(x=0, y=0)

frame_blanco = Frame (Ventana_principal)
frame_blanco.config(bg="White", width=100, height=400)
frame_blanco.place(x=200, y=0)

frame_blanco2 = Frame(Ventana_principal)
frame_blanco2.config(bg="white", width=800, height=100)
frame_blanco2.place(x=0, y=150)

frame_azul2 = Frame(Ventana_principal)
frame_azul2.config(bg="blue4", width=800, height=50)
frame_azul2.place(x=0,y=175)

frame_azul = Frame(Ventana_principal)
frame_azul.config(bg="blue4", width=50, height=400)
frame_azul.place(x=225, y=0)


Ventana_principal.mainloop()