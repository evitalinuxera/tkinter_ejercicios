import tkinter as tk
from tkinter import ttk

def saludar():
    print(f"Hola {nombre.get() or 'a todos'}")

# Defino ventana ppal
root = tk.Tk()

# Acá defino las variables
nombre = tk.StringVar()

# Armo los frames
superior = tk.Frame(root)
superior.pack(side="top", fill="x", expand=True)

inferior = tk.Frame(root)
inferior.pack(side="top", fill="x", expand=True, padx=10, pady=10)

# Acá van los widgets de entrada
nombre_etiqueta = ttk.Label(superior, text="Nombre: ")
nombre_etiqueta.pack(side="left", padx=(0, 10))
nombre_entrada = ttk.Entry(superior, width=15, textvariable=nombre)
nombre_entrada.pack(side="left")
nombre_entrada.focus()

# Widgets de botones
boton_saludo = ttk.Button(inferior, text="Saludar", command=saludar)
boton_saludo.pack(side="left", fill="x", padx=(0,20), expand=True)

boton_salir = ttk.Button(inferior, text="Salir", command=root.destroy)
boton_salir.pack(side="left", fill="x", padx=(20,0), expand=True)

# Loop Principal
root.mainloop()