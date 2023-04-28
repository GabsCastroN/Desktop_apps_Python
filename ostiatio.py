from tkinter import *

Ventana_principal = Tk()
Ventana_principal.title("OSTIA TIO")
Ventana_principal.geometry("600x600")
Ventana_principal.resizable(False,False)

frame_Rojo = Frame (Ventana_principal)
frame_Rojo.config(bg="red", width=600, height=150,)
frame_Rojo.place(x=0, y=0)

frame_Amarillo = Frame (Ventana_principal)
frame_Amarillo.config(bg="yellow", width=600, height=300,)
frame_Amarillo.place(x=0, y=150)


frame_rojo = Frame (Ventana_principal)
frame_rojo.config(bg="red", width=600, height=150,)
frame_rojo.place(x=0, y=450)

frame_Negro = Frame (Ventana_principal)
frame_Negro.config(bg="black", width=100, height=100,)
frame_Negro.place(x=250, y=250)


Ventana_principal.mainloop()