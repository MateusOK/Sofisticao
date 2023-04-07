import tkinter
import customtkinter as ctk
from PIL import Image

root = ctk.CTk()  # create CTk window like you do with the Tk window
root.geometry("1280x720")
root.resizable(False, False)
root.config(background="#FFFFFF")

division = ctk.CTkFrame(root, bg_color="white", width=250,
                        height=1450,  fg_color="#E0E0E0")
division.place(relx=0, rely=0, anchor=tkinter.W)


# images
logo_image = ctk.CTkImage(light_image=Image.open("assets\\dog_logo.png"))
side_image = ctk.CTkImage(light_image=Image.open("assets\\side_line.png"))
dash_logo = ctk.CTkImage(light_image=Image.open(
    "assets\\dashboard_logo_white.png"))
client_logo = ctk.CTkImage(light_image=Image.open("assets\\client_logo.png"))
services_logo = ctk.CTkImage(
    light_image=Image.open("assets\\services_logo.png"))
animals_logo = ctk.CTkImage(light_image=Image.open("assets\\animals_logo.png"))
exit_logo = ctk.CTkImage(light_image=Image.open("assets\\exit_logo.png"))

# labels
# logo_label = ctk.CTkLabel(frame, image=logo_image)
# side_line_label = ctk.CTkLabel(frame, image=side_image)
# title = ctk.CTkLabel(root, text="Sofisticão",font=ctk.CTkFont(family="Nunito", weight="bold", size=25))

# buttons
dash_button = ctk.CTkButton(root, text="Dashboard", image=dash_logo, fg_color="#27AE60",
                            corner_radius=5, height=35, width=180, bg_color="#F2F2F2",  font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"))
client_button = ctk.CTkButton(root, text="       Clientes", text_color="black", image=client_logo, corner_radius=7,
                              fg_color="white", height=35, width=180, bg_color="#E0E0E0",  font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"))
services_button = ctk.CTkButton(root, image=services_logo, text="      Serviços", text_color="black", corner_radius=7,
                                fg_color="white", height=35, width=180, bg_color="#E0E0E0",  font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"))
animals_button = ctk.CTkButton(root, image=animals_logo, text="        Animais", text_color="black", corner_radius=7,
                               fg_color="white", height=35, width=180, bg_color="#E0E0E0",  font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"))
exit_button = ctk.CTkButton(root, image=exit_logo, text="  Sair", text_color="black", corner_radius=7,
                            fg_color="white", height=35, width=180, bg_color="#E0E0E0", compound="right", font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"))


############### CONTAINER - BOX ###########################

# container
container = ctk.CTkFrame(root, bg_color="white", width=790,
                         height=180, border_color="#D9D9D9", border_width=1, fg_color="white")
container.place(relx=0.6, rely=0.5, anchor=tkinter.CENTER)


# logo - image
logo_image = ctk.CTkImage(light_image=Image.open(
    "assets\dashboard__container\logo_container.png"), size=(50, 50))
logo_label = ctk.CTkLabel(root, text="", image=logo_image, fg_color="white")
logo_label.place(relx=0.32, rely=0.46, anchor=tkinter.CENTER)


# title - container
animal_title = ctk.CTkLabel(root, text="Nome do animal", font=ctk.CTkFont(
    family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#292929")
animal_title.place(relx=0.395, rely=0.478, anchor=tkinter.CENTER)

# subtitle - container
owner_title = ctk.CTkLabel(root, text="Nome do dono", font=ctk.CTkFont(
    family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#6A6A6A")
owner_title.place(relx=0.392, rely=0.478, anchor=tkinter.CENTER)


# status - container
status_text = ctk.CTkLabel(root, text="Status: ", font=ctk.CTkFont(
    family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#292929")
animal_title.place(relx=0.395, rely=0.449, anchor=tkinter.CENTER)

status_text.place(relx=0.325, rely=0.55, anchor=tkinter.CENTER)

# in progress - status - container
in_progress_text = ctk.CTkLabel(root, text="em andamento", font=ctk.CTkFont(
    family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#F2994A")
in_progress_text.place(relx=0.393, rely=0.55, anchor=tkinter.CENTER)

# owner - container
owner_text = ctk.CTkLabel(root, text="Dono: ", font=ctk.CTkFont(
    family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#292929")
owner_text.place(relx=0.324, rely=0.580, anchor=tkinter.CENTER)

# waiting - owner - container
waiting_text = ctk.CTkLabel(root, text="Aguardando", font=ctk.CTkFont(
    family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#F2994A")
waiting_text.place(relx=0.385, rely=0.580, anchor=tkinter.CENTER)


# division - container
division = ctk.CTkFrame(root, bg_color="white", width=2,
                        height=95,  fg_color="#DCDCDC")
division.place(relx=0.453, rely=0.5, anchor=tkinter.CENTER)


# animal_info- container
title_information = ctk.CTkLabel(root, text="Animal: Gato  Sexo: Masculino  Idade: 8 anos", font=ctk.CTkFont(
    family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#292929")
title_information.place(relx=0.595, rely=0.448, anchor=tkinter.CENTER)


# animal_description - container
description_information_1 = ctk.CTkLabel(root, text="Procedimento feito Lorem ipsum dolor sit amet, consectetur adipiscing elit.", font=ctk.CTkFont(
    family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#717171")
description_information_1.place(relx=0.682, rely=0.478, anchor=tkinter.CENTER)

description_information_2 = ctk.CTkLabel(root, text="Sed sodales quam sed tortor sodales, vel vestibulum ligula euismod", font=ctk.CTkFont(
    family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#717171")
description_information_2.place(relx=0.661, rely=0.508, anchor=tkinter.CENTER)


description_information_3 = ctk.CTkLabel(root, text="Interdum et malesuada fames ac ante ipsum.", font=ctk.CTkFont(
    family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#717171")
description_information_3.place(relx=0.592, rely=0.538, anchor=tkinter.CENTER)

# price - container
price_text = ctk.CTkLabel(root, text="R$ 75,00", font=ctk.CTkFont(
    family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#292929")
price_text.place(relx=0.858, rely=0.4, anchor=tkinter.CENTER)

circle_price = ctk.CTkImage(light_image=Image.open(
    "assets\dashboard__container\circle_price.png"), size=(10, 10))
circle_price_label = ctk.CTkLabel(
    root, text="", image=circle_price, fg_color="white")
circle_price_label.place(relx=0.895, rely=0.4, anchor=tkinter.CENTER)

# posicionamento na tela

# logo_label.place(x=60, y=20)
# side_line_label.place(x=15,y=300)
dash_button.place(x=40, y=300)
client_button.place(x=40, y=350)
services_button.place(x=40, y=400)
animals_button.place(x=40, y=450)
exit_button.place(x=40, y=600)


root.mainloop()
