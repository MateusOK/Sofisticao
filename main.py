from tkinter import *

root = Tk()

root.title("Login - Sofisticão")

root.config(background='#FFFFFF')

#root.geometry("{}x{}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

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

# Crie um rótulo para o texto
text_label = Label(frame, text="Meu texto aqui")

# Posicione as imagens e o texto na janela
left_label.pack(side=LEFT)
logo_label.place(x=600)# adicione um espaço de 10 pixels entre o texto e as imagens
right_label.pack(side=RIGHT)

root.mainloop()
