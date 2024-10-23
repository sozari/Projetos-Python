import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Minha primeira GUI')
root.geometry('400x300')

label = tk.Label(root, text='Olá, Tkinter!')
label.pack(pady=10)

button = tk.Button(root, text='Clique em mim', command=lambda: print('Botão clicado!'))
button.pack(pady=10)

root.mainloop()
