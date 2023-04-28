from tkinter import *

Ventana_principal = Tk ()

Ventana_principal.title("Noruega")
Ventana_principal.geometry("800x400")
Ventana_principal.resizable(False,False)
Ventana_principal.config(bg="red")

frame_blanco = Frame(Ventana_principal)
frame_blanco.config(bg="white", height=200, width=50)
frame_blanco.place(x=375, y=100)

frame_blanco2=Frame(Ventana_principal)
frame_blanco2.config(bg="white", height=50, width=200)
frame_blanco2.place(x=300,y=175)

Ventana_principal.mainloop()