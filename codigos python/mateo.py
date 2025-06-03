import tkinter as tk
from tkinter import ttk

def abrir_hoja():
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Mensaje")
    nueva_ventana.geometry("200x100")

    etiqueta = ttk.Label(nueva_ventana, text="Te quiero", font=("Arial", 16))
    etiqueta.pack(expand=True)


root = tk.Tk()
root.title("Ventana principal")
root.geometry("300x150")

boton = ttk.Button(root, text="Ir a la hoja", command=abrir_hoja)
boton.pack(expand=True)

root.mainloop()