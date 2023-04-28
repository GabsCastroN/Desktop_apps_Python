from tkinter import *

Ventana_principal = Tk()
Ventana_principal.title("France qliao")
Ventana_principal.geometry("600x600")
Ventana_principal.resizable(False,False)

frame_azul = Frame (Ventana_principal)
frame_azul.config(bg="blue", width=200, height=600,)
frame_azul.place(x=0, y=0)

frame_blanco = Frame (Ventana_principal)
frame_blanco.config(bg="white", width=400, height=600,)
frame_blanco.place(x=200, y=0)


frame_rojo = Frame (Ventana_principal)
frame_rojo.config(bg="red", width=600, height=600,)
frame_rojo.place(x=400, y=0)

Ventana_principal.mainloop()