from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = Tk()

root.title("Login - Sofisticão")

root.config(background='#FFFFFF')


# window size
root.resizable(False, False)

root.maxsize(width=1280, height=720)

root.minsize(width=1280, height=720)


# Crie um frame para conter as imagens e o texto
frame = Frame(root)
frame.pack(fill=BOTH, expand=True)

# Carregue as imagens
left_image = PhotoImage(file="assets\leftImage.png")
right_image = PhotoImage(file="assets\\rightImage.png")
logo = PhotoImage(file="assets\dog_logo.png")

# Crie rótulos para exibir as imagens
left_label = Label(frame, image=left_image)
right_label = Label(frame, image=right_image)
logo_label = Label(frame, image=logo)
title = ttk.Label(frame, text="Sofisticão",
                  font="Nunito 35 bold", bootstyle="success")
email_input = ttk.Entry(frame, bootstyle=SUCCESS, width=25, font="Arial 18")
email_text = ttk.Label(frame, text="Email",
                       font="Nunito 12 bold", bootstyle=SUCCESS)
password_input = ttk.Entry(frame, bootstyle=SUCCESS,
                           width=25, font="Arial 18", show="*")
password_text = ttk.Label(
    frame, text="Senha", font="Nunito 12 bold", bootstyle=SUCCESS)
check = ttk.Checkbutton(frame, text="Continuar conectado", bootstyle="success")
senha_esquece = Label(frame, text="Esqueci minha senha",
                      font="Nunito 8 bold underline")
entrar_button = ttk.Button(frame, text="Entrar", bootstyle=SUCCESS, width=52)

# Crie um rótulo para o texto
text_label = Label(frame, text="Meu texto aqui")

# Posicione as imagens e o texto na janela
left_label.pack(side=LEFT)
# adicione um espaço de 10 pixels entre o texto e as imagens
logo_label.place(x=565, y=140)
right_label.pack(side=RIGHT)
email_input.place(x=465, y=400)
title.place(x=520, y=300)
email_text.place(x=470, y=370)
password_input.place(x=465, y=485)
password_text.place(x=465, y=455)
check.place(x=465, y=560)
senha_esquece.place(x=680, y=557)
entrar_button.place(x=465, y=600)

root.mainloop()
