# Hacer una ventana con una entrada de texto y un botón
# al apretar el botón, que una etiqueta cambie con lo que
# tiene la ventana

import tkinter as tk 
from tkinter import ttk

# Función de cambiar

def cambiar():
    etiqueta_text = texto.get()
    etiqueta.config(text=etiqueta_text)
    

# Ventana ppal
root = tk.Tk()

# Acá defino las variables
texto = tk.StringVar()

root.geometry("300x200")
root.resizable(False, False)
root.title("Ejercicio")

# Frames
superiorFr = ttk.Frame(root)
superiorFr.pack(side="top", fill="x", expand=True)

inferiorFr = ttk.Frame(root)
inferiorFr.pack(side="top", fill="x", expand=True)

# Widgets
entrada = ttk.Entry(superiorFr, textvariable=texto)
entrada.pack()

boton = ttk.Button(superiorFr, text="Cambiar", command=cambiar)
boton.pack()

etiqueta = ttk. Label(inferiorFr, text="ESTO VA A SER CAMBIADO")
etiqueta.pack()


root.mainloop()