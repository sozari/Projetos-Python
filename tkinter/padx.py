import tkinter as tk

root = tk.Tk()
root.geometry('400x500')
# place a label on the root window
message = tk.Label(root, text="Hello",font=("Comic Sans",20), fg = "blue",background="black")
message.pack(padx = (0, 200))
message2 = tk.Label(root, text="world",font=("Comic Sans",20), fg = "blue",background="red")
message2.pack(padx="20px")
# keep the window displaying
root.mainloop()