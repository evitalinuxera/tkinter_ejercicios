import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Ejemplos de widgets")

label = ttk.Label(root, text="Soy el de arriba!", padding=20)
# label.config(font=("Segoe UI", 20))
label.pack()

main_sep = ttk.Separator(root, orient="horizontal")
main_sep.pack(fill="x")  # Si saco el fill, qué pasa?

label = ttk.Label(root, text="Soy el de abajo!", padding=20)
label.config(font=("Segoe UI", 20))
label.pack()

root.mainloop()