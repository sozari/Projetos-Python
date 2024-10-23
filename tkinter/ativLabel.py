import tkinter as tk

root = tk.Tk()
root.geometry('300x200')

label = tk.Label(root, text="0")
label.pack(pady=10)

# Variável global para armazenar o contador
x = 0

def on_button_click():
    global x
    x += 1  # Incrementa o valor de x
    label.config(text=str(x))  # Atualiza o texto do label

def zera():
    global x
    x = 0
    label.config(text=str(x))

# Botão que chama a função on_button_click
button = tk.Button(root, text="Clique em mim", command=on_button_click)
button.pack(pady=10)

button = tk.Button(root, text="Clique para zerar", command=zera)
button.pack(pady=10)

root.mainloop()
