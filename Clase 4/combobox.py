import tkinter as tk
from tkinter import ttk


# Función adosada al combo
def cambiar_seleccion(event):
    print("Hoy es", dia_semana.get()) # Acá leo el combo
    print("Pero lo vamos a cambiar a ...")
    dia_semana.set("Viernes") # Acá seteo el combo
    print(dia_semana.current())  # Esto puede devolver -1 si el usuario tipea su propio valor.


root = tk.Tk()
root.title("Widget Examples")

# Acá viene el selector
dia_seleccionado = tk.StringVar()
dia_semana = ttk.Combobox(root, textvariable=dia_seleccionado)
dia_semana["values"] = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes")
dia_semana["state"] = "readonly"  # "normal" es para que se puedan agregar valores.
dia_semana.pack()
dia_semana.bind("<<ComboboxSelected>>", cambiar_seleccion)

root.mainloop()

print(dia_seleccionado.get(), "fue seleccionado.")