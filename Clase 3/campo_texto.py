import tkinter as tk 
from tkinter import ttk


root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Campo de Texto")

# Acá se crea el widget
campo_texto = tk.Text(root, height=8)
campo_texto.pack()

# Acá se ingresa texto
# ojo con el 1.0 que es medio cantina 
campo_texto.insert("1.0", "Viva la santa federación!!")

#Acá leemos el texto
variable = campo_texto.get("1.0", "end")
print(variable)

root.mainloop()