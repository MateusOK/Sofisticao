from tkinter import Tk
from tkinter.ttk import Style, Button

# Criar a janela principal
root = Tk()

# Criar uma instância do objeto Style
style = Style()

# Configurar o estilo do botão com bordas arredondadas
style.configure('Rounded.TButton', bordercolor='black',
                borderwidth=2, relief='raised', padding=5)
style.map('Rounded.TButton', background=[
          ('active', 'gray85'), ('pressed', 'gray75')])

# Criar o botão com o estilo configurado
button = Button(root, text='Botão com bordas arredondadas',
                style='Rounded.TButton')

# Exibir o botão na janela
button.pack()

# Iniciar o loop de eventos do tkinter
root.mainloop()
