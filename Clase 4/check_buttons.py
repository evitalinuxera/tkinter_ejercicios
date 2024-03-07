import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Ejemplo de widgets")

# Como en los labels, podemos usar imágenes, texto o combinarlos.
check_button = ttk.Checkbutton(root, text="Marcame!")
check_button.pack()

check_button["state"] = "normal"  # "disabled" cuando no se usa


# Todas las opciones

seleccionado = tk.StringVar()

def print_la_actual():
    print(seleccionado.get())

check = tk.Checkbutton(
    root,
    text="Ejemplo de Check",
    variable=seleccionado,
    command=print_la_actual,
    onvalue="Encendido",
    offvalue="Apagado"
)

check.pack()


root.mainloop()