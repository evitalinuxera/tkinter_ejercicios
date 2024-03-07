import tkinter as tk
from tkinter import ttk

def saludar():
    print(f"Hola {nombre.get() or 'a todos'}")

# Defino ventana ppal
root = tk.Tk()

# Acá defino las variables
nombre = tk.StringVar()

# Acá van los widgets de entrada
nombre_etiqueta = ttk.Label(text="Nombre: ")
nombre_etiqueta.pack(side="left", padx=(0, 10))
nombre_entrada = ttk.Entry(width=15, textvariable=nombre)
nombre_entrada.pack(side="left")
nombre_entrada.focus()

# Widgets de botones
boton_saludo = ttk.Button(text="Saludar", command=saludar)
boton_saludo.pack(side="left")

boton_salir = ttk.Button(text="Salir", command=root.destroy)
boton_salir.pack(side="right")

# Loop Principal
root.mainloop()