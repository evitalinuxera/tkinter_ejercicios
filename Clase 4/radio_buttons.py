import tkinter as tk
from tkinter import ttk

# -- Configuración solo para win$. No sé si funciona --
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
# -- * --

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Radio Button Widget")

storage_variable = tk.StringVar()

opcion_1 = ttk.Radiobutton(
	root,
	text="Opción 1",
	variable=storage_variable,
	value="Primera opción"
)

opcion_2 = ttk.Radiobutton(
	root,
	text="Opcion 2",
	variable=storage_variable,
	value="Segunda opción"
)

opcion_3 = ttk.Radiobutton(
	root,
	text="Opción 3",
	variable=storage_variable,
	value="Tercera opción"
)

opcion_1.pack()
opcion_2.pack()
opcion_3.pack()


root.mainloop()

print(storage_variable.get(), "fue seleccionada.")