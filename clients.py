import tkinter
import customtkinter as ctk
from PIL import Image
from new_client import newClientWindow

def clientsWindow():
    root = ctk.CTk()  # create CTk window like you do with the Tk window
    root.geometry("1280x720")
    root.resizable(False, False)
    root.config(background="#FFFFFF")

    division = ctk.CTkFrame(root, bg_color="white", width=250,
                            height=1450,  fg_color="#E0E0E0")
    division.place(relx=0, rely=0, anchor=tkinter.W)

    side_line = ctk.CTkFrame(root, bg_color="white", width=4,
                            height=170,  fg_color="#FFA826")
    side_line.place(x=15, y=310)


    #commands
    def sair():
        root.destroy()
    
    def openClient():
        root.destroy()
        newClientWindow()

    # images
    logo = ctk.CTkImage(light_image=Image.open("assets\\logo.png"), size=(200,160))
    dash_logo = ctk.CTkImage(light_image=Image.open(
        "assets\\dashboard_logo.png"))
    client_logo = ctk.CTkImage(light_image=Image.open("assets\\clients_logo_white.png"))
    services_logo = ctk.CTkImage(
        light_image=Image.open("assets\\services_logo.png"))
    animals_logo = ctk.CTkImage(light_image=Image.open("assets\\animals_logo.png"))
    exit_logo = ctk.CTkImage(light_image=Image.open("assets\\exit_logo.png"))
    newButton_logo = ctk.CTkImage(light_image=Image.open("assets\\new.png"))

    # labels
    main_logo = ctk.CTkLabel(root, text="" ,image=logo, bg_color="#E0E0E0")

    # buttons
    dash_button = ctk.CTkButton(root, text="Dashboard", image=dash_logo, fg_color="white", text_color="black", 
                                corner_radius=5, height=35, width=180, bg_color="#F2F2F2",  font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D")
    client_button = ctk.CTkButton(root, text="       Clientes", image=client_logo, corner_radius=7,
                                fg_color="#F2800D", height=35, width=180, bg_color="#E0E0E0",  font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D")
    services_button = ctk.CTkButton(root, image=services_logo, text="      Serviços", text_color="black", corner_radius=7,
                                    fg_color="white", height=35, width=180, bg_color="#E0E0E0",  font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D")
    animals_button = ctk.CTkButton(root, image=animals_logo, text="        Animais", text_color="black", corner_radius=7,
                                fg_color="white", height=35, width=180, bg_color="#E0E0E0",  font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D")
    exit_button = ctk.CTkButton(root, image=exit_logo, text="  Sair", text_color="black", corner_radius=7,
                                fg_color="white", height=35, width=180, bg_color="#E0E0E0", compound="right", font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D", command=sair)
    new_button = ctk.CTkButton(root, image=newButton_logo, text="  Novo", corner_radius=7,fg_color="#FFA826",
                                 height=35, width=180, bg_color="white", font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D", command=openClient)

    ################ POSTER  ###############

    # Dashboard - Title

    title_poster = ctk.CTkLabel(root, text="Clientes", font=ctk.CTkFont(
        family="Nunito", size=20, weight="bold"), fg_color="white", text_color="black")
    title_poster.place(relx=0.6, rely=0.040, anchor=tkinter.CENTER)



    ############### CONTAINER - BOX ###############

    # container
    container = ctk.CTkFrame(root, bg_color="white", width=825,
                            height=189, border_color="#D9D9D9", border_width=1, fg_color="white")
    container.place(relx=0.6, rely=0.5, anchor=tkinter.CENTER)


    # logo - image
    logo_image = ctk.CTkImage(light_image=Image.open(
        "assets\dashboard__container\logo_container.png"), size=(75, 100))
    logo_label = ctk.CTkLabel(root, text="", image=logo_image, fg_color="white")
    logo_label.place(relx=0.32, rely=0.46, anchor=tkinter.CENTER)


    # title - container
    animal_title = ctk.CTkLabel(root, text="Nome do animal", font=ctk.CTkFont(
        family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#292929")
    animal_title.place(x=11.5, y=-25, anchor=tkinter.CENTER)

    # subtitle - container
    owner_title = ctk.CTkLabel(root, text="Dono:", font=ctk.CTkFont(
        family="Open Sans", size=14, weight="bold"), fg_color="white", text_color="#6A6A6A")
    owner_title.place(relx=0.371, rely=0.445, anchor=tkinter.CENTER)

    owner_title_placeholder = ctk.CTkLabel(root, text="Lorem Ipsum", font=ctk.CTkFont(
        family="Open Sans", size=14), fg_color="white", text_color="#6A6A6A")
    owner_title_placeholder.place(relx=0.420, rely=0.445, anchor=tkinter.CENTER)

    contact_title = ctk.CTkLabel(root, text="Contato:", font=ctk.CTkFont(
        family="Open Sans", size=14, weight="bold"), fg_color="white", text_color="#6A6A6A")
    contact_title.place(relx=0.377, rely=0.473, anchor=tkinter.CENTER)


    contact_title_placeholder = ctk.CTkLabel(root, text="(13) 9684-4814", font=ctk.CTkFont(
        family="Open Sans", size=14), fg_color="white", text_color="#6A6A6A")
    contact_title_placeholder.place(relx=0.441, rely=0.473, anchor=tkinter.CENTER)

    date_icon=ctk.CTkImage(light_image=Image.open(
        "assets\dashboard__container\calendar.png"), size=(16, 16))
    date_label = ctk.CTkLabel(root, text="", image=date_icon, fg_color="white")
    date_label.place(relx=0.361, rely=0.510, anchor=tkinter.CENTER)


    date_text = ctk.CTkLabel(root, text="14/04/2023", font=ctk.CTkFont(
        family="Open Sans", size=14, weight="bold"), fg_color="white", text_color="#292929")
    date_text .place(relx=0.397, rely=0.511, anchor=tkinter.CENTER)

    clock_icon = ctk.CTkImage(light_image=Image.open(
        "assets\dashboard__container\clock.png"), size=(16, 16))
    clock_label = ctk.CTkLabel(root, text="", image=clock_icon, fg_color="white")
    clock_label.place(relx=0.442, rely=0.511, anchor=tkinter.CENTER)
    
    clock_text = ctk.CTkLabel(root, text="14h00", font=ctk.CTkFont(
        family="Open Sans", size=14, weight="bold"), fg_color="white", text_color="#292929")
    clock_text.place(relx=0.468, rely=0.511, anchor=tkinter.CENTER)

    # status - container
    animal_title.place(relx=0.395, rely=0.449, anchor=tkinter.CENTER)

    status_text = ctk.CTkFrame(root, bg_color="#F2994A",  fg_color="#F2994A", width=71, height=2)
    status_text.place(relx=0.325, rely=0.575, anchor=tkinter.CENTER)

    # in progress - status - container
    in_progress_text = ctk.CTkLabel(root, text="Em andamento", font=ctk.CTkFont(
        family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#F2994A")
    in_progress_text.place(relx=0.405, rely=0.575, anchor=tkinter.CENTER)



    # division - container
    division = ctk.CTkFrame(root, bg_color="white", width=3,
                            height=95,  fg_color="#DCDCDC")
    division.place(relx=0.490, rely=0.465, anchor=tkinter.CENTER)


    # animal_info- container
    description_title = ctk.CTkLabel(root, text="Descrição: ", font=ctk.CTkFont(
        family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#717171")
    description_title.place(relx=0.536, rely=0.413, anchor=tkinter.CENTER)


    # animal_description - container
    description_information_1 = ctk.CTkLabel(root, text="Procedimento feito Lorem ipsum dolor sit amet, consectetur adipiscing", font=ctk.CTkFont(
        family="Open Sans", size=16), fg_color="white", text_color="#717171")
    description_information_1.place(relx=0.7, rely=0.450, anchor=tkinter.CENTER)

    description_information_2 = ctk.CTkLabel(root, text="elit. Sed sodales quam sed tortor sodales, vel vestibulum ligula euismod.", font=ctk.CTkFont(
        family="Open Sans", size=16), fg_color="white", text_color="#717171")
    description_information_2.place(relx=0.708, rely=0.480, anchor=tkinter.CENTER)

    # Animal informations

    # Animal
    animal_title_description = ctk.CTkLabel(root, text="Animal: Gato", font=ctk.CTkFont(
        family="Open Sans", size=16), fg_color="white", text_color="#292929")
    animal_title_description.place(relx=0.540, rely=0.525, anchor=tkinter.CENTER)

    # Gender
    gender_title_description = ctk.CTkLabel(root, text="Sexo: Masculino", font=ctk.CTkFont(
        family="Open Sans", size=16), fg_color="white", text_color="#292929")
    gender_title_description.place(relx=0.7, rely=0.525, anchor=tkinter.CENTER)

    # Age
    age_title_description = ctk.CTkLabel(root, text="Idade: 8 anos", font=ctk.CTkFont(
        family="Open Sans", size=16), fg_color="white", text_color="#292929")
    age_title_description.place(relx=0.865, rely=0.525, anchor=tkinter.CENTER)

    # price - container
    price_text = ctk.CTkLabel(root, text="Preço da consulta", font=ctk.CTkFont(
        family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="black")
    price_text.place(relx=0.795, rely=0.575, anchor=tkinter.CENTER)

    price_value = ctk.CTkLabel(root, text="R$75,00", font=ctk.CTkFont(
        family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#F2994A")
    price_value.place(relx=0.880, rely=0.575, anchor=tkinter.CENTER)

    # posicionamento na tela

    #logo
    main_logo.place(x=30, y=60)
    
    #buttons
    dash_button.place(x=40, y=300)
    client_button.place(x=40, y=350)
    services_button.place(x=40, y=400)
    animals_button.place(x=40, y=450)
    exit_button.place(x=40, y=600)
    new_button.place(x=700, y=600)


    root.mainloop()