import tkinter as tk

# Cria a janela principal
root = tk.Tk()
root.title("Minha primeira GUI")

# Cria um rótulo (label) e o coloca na janela
label = tk.Label(root, text="Olá, Tkinter!")
label.pack()


# Função que será chamada quando o botão for clicado
def on_button_click():
    label.config(text="Botão clicado!")

# Cria um botão e o coloca na janela
button = tk.Button(root, text="Clique em mim", command=on_button_click)
button.pack()


# Inicia o loop principal da interface
root.mainloop()
