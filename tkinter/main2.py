import tkinter as tk


root = tk.Tk()
root.geometry('400x500')

# place a label on the root window
message = tk.Label(root, text="Hello, World!", font=("arial",50), fg= 'blue', background= 'red')
message.pack(side="bottom", expand=True)
btn = tk.Button(root, text='Clique aqui!')
btn.pack(side='bottom', expand=True)
message2 = tk.Label(root, text="Hello, World!", font=("arial",50), fg= 'blue', background= 'red')
message2.pack(side="top", expand=True)
root.config(bg="yellow")


# keep the window displaying
root.mainloop()
