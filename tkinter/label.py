import tkinter as tk


root = tk.Tk()

# place a label on the root window
message = tk.Label(root, text="Hello, World!")
message.pack()

message.config(text='malakoi')

# keep the window displaying
root.mainloop()
