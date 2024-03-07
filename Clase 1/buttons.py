import tkinter as tk
from tkinter import ttk

def saludar():
    print("Hola a todos")

root = tk.Tk()

boton_saludo = ttk.Button(text="Saludar", command=saludar)
boton_saludo.pack(side="left", fill="x", expand=True)

boton_salir = ttk.Button(text="Salir", command=root.destroy)
boton_salir.pack(side="left")


root.mainloop()