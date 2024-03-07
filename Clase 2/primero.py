import tkinter as tk 


root = tk.Tk()
root.geometry("600x400")

rect_1 = tk.Label(root, text="Rectángulo 1", background="green", foreground="white")
rect_1.pack(ipadx=10, ipady=10, fill="both", expand=True)

rect_2 = tk.Label(root, text="Rectángulo 2", background="red", foreground="white")
rect_2.pack(ipadx=10, ipady=10, fill="x", expand=True)

root.mainloop()