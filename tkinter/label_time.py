import tkinter as tk
import time

root = tk.Tk()

message = tk.Label(root, text="Hello, World!")
message.pack()



while True:
    message.config(text='malakoi')
    root.update()  # Força a atualização da interface
    time.sleep(1)
        
    message.config(text='1')
    root.update()
    time.sleep(1)
        
    message.config(text='2')
    root.update()
    time.sleep(1)

    message.config(text='3')
    root.update()
    time.sleep(1)



