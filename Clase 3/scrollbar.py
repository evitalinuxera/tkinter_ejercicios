import tkinter as tk 
from tkinter import ttk


root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Barra Scroll")

# Acá se crea el widget
campo_texto = tk.Text(root, height=8)
campo_texto.pack(side="right")

# Acá viene el scroleo
scroleo = ttk.Scrollbar(root, orient="vertical", command=campo_texto.yview)
campo_texto["yscrollcommand"] = scroleo.set
scroleo.pack(side="right")

root.mainloop()