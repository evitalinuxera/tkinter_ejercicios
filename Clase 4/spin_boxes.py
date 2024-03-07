import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Ejemplos de Widgets - Spinbox")


valor_inicial = tk.StringVar(value=20)
spin_box = tk.Spinbox(
    root,
    from_=0,
    to=30,
    textvariable=valor_inicial,
    wrap=False)
# spin_box = tk.Spinbox(root, values=(5, 10, 15, 20, 25, 30), textvariable=valor_inicial, wrap=False)
# También se pueden usar valores fijos en lugar de un deslizante.

spin_box.pack()

print(spin_box.get())  # Esto generalmente se hace con un botón

root.mainloop()