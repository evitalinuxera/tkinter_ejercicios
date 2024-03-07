import tkinter as tk 
from tkinter import ttk
from PIL import Image, ImageTk


root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Imagen")

imagen = Image.open("logo.png").resize((130, 120))
foto = ImageTk.PhotoImage(imagen)

etiqueta = ttk.Label(root, image=foto, padding=5, text="El logo más fierro del mundo", compound="top")
etiqueta.pack()


root.mainloop()