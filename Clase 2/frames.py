import tkinter as tk 
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")


# Frames
sidebar = ttk.Frame(root)
sidebar.pack(side="left", expand=True, fill="both")

ppal = ttk.Frame(root)
ppal.pack(side="right", expand=True, fill="both")

# Contenidos y encabezado
menu = tk.Label(sidebar, text="Menú costado", background="Red")
menu.pack(side="top", expand=True, fill="both")

encabezado = tk.Label(ppal, text="Encabezado", background="White")
encabezado.pack(side="top", fill="x", expand=False)

contenido = tk.Label(ppal, text="Contenido", background="Green")
contenido.pack(side="top", fill="both", expand=True)

root.mainloop()