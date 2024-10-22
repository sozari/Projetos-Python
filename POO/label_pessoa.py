import tkinter as tk
import ativ_pessoa as p


root = tk.Tk()
root.geometry('400x300')
# place a label on the root window
message = tk.Label(root, text="Dados da Pessoa:", font=("Arial", 14))
message.pack(pady=20)

dados_pessoa = p.nome1.dados()
message_dados = tk.Label(root, text=dados_pessoa, font=("Arial", 12))
message_dados.pack(pady=10)



# keep the window displaying
root.mainloop()
