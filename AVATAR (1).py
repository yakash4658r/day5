from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="WELCOME TO PYTHON!!").grid(column=1, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=2)
ttk.Button(frm, text="Start", command=root.destroy).grid(column=0, row=2)
root.mainloop()