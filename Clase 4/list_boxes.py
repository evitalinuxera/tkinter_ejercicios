import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Ejemplos widgets - listboxes")

lenguajes_programacion = ("C", "Go", "JavaScript", "Perl", "Python", "Rust")

lenguajes = tk.StringVar(value=lenguajes_programacion)
lenguajes_select = tk.Listbox(root, listvariable=lenguajes, height=6)
lenguajes_select.pack(padx=10, pady=10)

lenguajes_select["selectmode"] = "extended"  # Permitir selección múltiple, "browse" es un nombre horrible pero es la contraparte

def cambio_de_seleccion(event):
    selecciones_hechas = lenguajes_select.curselection()
    for i in selecciones_hechas:
        print(lenguajes_select.get(i))


lenguajes_select.bind("<<ListboxSelect>>", cambio_de_seleccion)
root.mainloop()