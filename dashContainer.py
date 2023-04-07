import tkinter
import customtkinter as ctk
from PIL import Image


root = ctk.CTk()  # create CTk window like you do with the Tk window
root.geometry("1280x720")
root.resizable(False, False)
root.config(background="#FFFFFF")


# container
container = ctk.CTkFrame(root, bg_color="white", width=790,
                         height=180, border_color="#D9D9D9", border_width=1, fg_color="white")
container.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


# logo - image
logo_image = ctk.CTkImage(light_image=Image.open(
    "assets\dashboard__container\logo_container.png"), size=(50, 50))
logo_label = ctk.CTkLabel(root, text="", image=logo_image, fg_color="white")
logo_label.place(relx=0.22, rely=0.46, anchor=tkinter.CENTER)


# title - container
animal_title = ctk.CTkLabel(root, text="Nome do animal", font=ctk.CTkFont(
    family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#292929")
animal_title.place(relx=0.295, rely=0.478, anchor=tkinter.CENTER)

# subtitle - container
owner_title = ctk.CTkLabel(root, text="Nome do dono", font=ctk.CTkFont(
    family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#6A6A6A")
owner_title.place(relx=0.292, rely=0.478, anchor=tkinter.CENTER)


# status - container
status_text = ctk.CTkLabel(root, text="Status: ", font=ctk.CTkFont(
    family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#292929")
animal_title.place(relx=0.295, rely=0.449, anchor=tkinter.CENTER)

status_text.place(relx=0.225, rely=0.55, anchor=tkinter.CENTER)

# in progress - status - container
in_progress_text = ctk.CTkLabel(root, text="em andamento", font=ctk.CTkFont(
    family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#F2994A")
in_progress_text.place(relx=0.293, rely=0.55, anchor=tkinter.CENTER)

# owner - container
owner_text = ctk.CTkLabel(root, text="Dono: ", font=ctk.CTkFont(
    family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#292929")
owner_text.place(relx=0.224, rely=0.580, anchor=tkinter.CENTER)

# waiting - owner - container
waiting_text = ctk.CTkLabel(root, text="Aguardando", font=ctk.CTkFont(
    family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#F2994A")
waiting_text.place(relx=0.285, rely=0.580, anchor=tkinter.CENTER)


# division - container
division = ctk.CTkFrame(root, bg_color="white", width=2,
                        height=95,  fg_color="#DCDCDC")
division.place(relx=0.353, rely=0.5, anchor=tkinter.CENTER)


# animal_info- container
title_information = ctk.CTkLabel(root, text="Animal: Gato  Sexo: Masculino  Idade: 8 anos", font=ctk.CTkFont(
    family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#292929")
title_information.place(relx=0.495, rely=0.448, anchor=tkinter.CENTER)


# animal_description - container
description_information_1 = ctk.CTkLabel(root, text="Procedimento feito Lorem ipsum dolor sit amet, consectetur adipiscing elit.", font=ctk.CTkFont(
    family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#717171")
description_information_1.place(relx=0.582, rely=0.478, anchor=tkinter.CENTER)

description_information_2 = ctk.CTkLabel(root, text="Sed sodales quam sed tortor sodales, vel vestibulum ligula euismod", font=ctk.CTkFont(
    family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#717171")
description_information_2.place(relx=0.561, rely=0.508, anchor=tkinter.CENTER)


description_information_3 = ctk.CTkLabel(root, text="Interdum et malesuada fames ac ante ipsum.", font=ctk.CTkFont(
    family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#717171")
description_information_3.place(relx=0.492, rely=0.538, anchor=tkinter.CENTER)

# price - container
price_text = ctk.CTkLabel(root, text="R$ 75,00", font=ctk.CTkFont(
    family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#292929")
price_text.place(relx=0.758, rely=0.4, anchor=tkinter.CENTER)

circle_price = ctk.CTkImage(light_image=Image.open(
    "assets\dashboard__container\circle_price.png"), size=(10, 10))
circle_price_label = ctk.CTkLabel(
    root, text="", image=circle_price, fg_color="white")
circle_price_label.place(relx=0.795, rely=0.4, anchor=tkinter.CENTER)


root.mainloop()
