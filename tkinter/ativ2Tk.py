import tkinter as tk
root = tk.Tk()

message = tk.Label(root, text="Hello",font=("Comic Sans",15), fg = "white",background="green")
message.pack(anchor="n",side='left')
message2 = tk.Label(root, text="world",font=("Comic Sans",15), fg = "white",background="blue")
message2.pack(anchor="n", side='left')
message3 = tk.Label(root, text="Hello",font=("Comic Sans",15), fg = "white",background="red")
message3.pack(anchor="n", side='left')

root.mainloop()