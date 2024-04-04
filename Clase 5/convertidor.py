import tkinter as tk
from tkinter import ttk

# Función de conversión
# El try es por si le damos al botón de calcular antes 
# de poner algún valor en el campo de ingreso.
def calcular_pies(*args):
    try:
        value = float(valor_en_metros.get())
        valor_en_pies.set('%.3f' % (value * 3.28084))
    except ValueError:
        pass

root = tk.Tk()
root.title("Calculador de distancias")

# Declaramos las variables
valor_en_pies = tk.StringVar()
valor_en_metros = tk.StringVar()

# Frame ppal
main = ttk.Frame(root, padding="30 15 30 15")
main.pack()

# Acá va todo el frame de metros y su contenido
frame_metros = ttk.Frame(main)
frame_metros.pack(fill="both")

etiqueta_metros = ttk.Label(frame_metros, text="metros")
etiqueta_metros.pack(side="left", padx=5, pady=5)

input_metros = ttk.Entry(frame_metros, width=10, textvariable=valor_en_metros)
input_metros.pack(side="left", padx=5, pady=5)
input_metros.focus()


# Acá va todo el frame de pies y su contenido
frame_pies = ttk.Frame(main)
frame_pies.pack(fill="both")

etiqueta_pies = ttk.Label(frame_pies, text="pies")
etiqueta_pies.pack(side="left", padx=5, pady=5)

pies_display = ttk.Label(frame_pies, textvariable=valor_en_pies)
pies_display.pack(side="left", padx=5, pady=5)

# Acá el botón que llama a la función de conversión
calc_button = ttk.Button(main, text="Calcular", command=calcular_pies)
calc_button.pack(padx=5, pady=5, expand=True, fill="both")

# Esto es por si usamos el botón o el ENTER
root.bind("<Return>", calcular_pies)
root.bind("<KP_Enter>", calcular_pies)

root.mainloop()