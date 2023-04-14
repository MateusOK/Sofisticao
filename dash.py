import tkinter
import customtkinter as ctk
from PIL import Image
from clients import clientsWindow
from services import servicesWindow
from components.scrollContainer import MyFrame


def dashWindow():
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
        clientsWindow()

    def openServices():
        root.destroy()
        servicesWindow()

    # images
    logo = ctk.CTkImage(light_image=Image.open("assets\\logo.png"), size=(200,160))
    dash_logo = ctk.CTkImage(light_image=Image.open(
        "assets\\dashboard_logo_white.png"))
    client_logo = ctk.CTkImage(light_image=Image.open("assets\\client_logo.png"))
    services_logo = ctk.CTkImage(
        light_image=Image.open("assets\\services_logo.png"))
    animals_logo = ctk.CTkImage(light_image=Image.open("assets\\animals_logo.png"))
    exit_logo = ctk.CTkImage(light_image=Image.open("assets\\exit_logo.png"))

    # labels
    main_logo = ctk.CTkLabel(root, text="" ,image=logo, bg_color="#E0E0E0")

    # buttons
    dash_button = ctk.CTkButton(root, text="Dashboard", image=dash_logo, fg_color="#F2800D",
                                corner_radius=5, height=35, width=180, bg_color="#F2F2F2",  font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D")
    client_button = ctk.CTkButton(root, text="       Clientes", text_color="black", image=client_logo, corner_radius=7,
                                fg_color="white", height=35, width=180, bg_color="#E0E0E0",  font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D", command=openClient)
    services_button = ctk.CTkButton(root, image=services_logo, text="      Serviços", text_color="black", corner_radius=7,
                                    fg_color="white", height=35, width=180, bg_color="#E0E0E0",  
                                    font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D", command=openServices)
    animals_button = ctk.CTkButton(root, image=animals_logo, text="        Animais", text_color="black", corner_radius=7,
                                fg_color="white", height=35, width=180, bg_color="#E0E0E0",  font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D")
    exit_button = ctk.CTkButton(root, image=exit_logo, text="  Sair", text_color="black", corner_radius=7,
                                fg_color="white", height=35, width=180, bg_color="#E0E0E0", compound="right", font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D", command=sair)


    ################ POSTER  ###############


    # Dashboard - Title

    title_poster = ctk.CTkLabel(root, text="Dashboard", font=ctk.CTkFont(
        family="Nunito", size=20, weight="bold"), fg_color="white", text_color="black")
    title_poster.place(relx=0.6, rely=0.040, anchor=tkinter.CENTER)


    # Scheduled
    poster_scheduled = ctk.CTkFrame(root, bg_color="white", width=250,
                                    height=180, border_color="#D9D9D9", border_width=1, fg_color="#EA8C00")
    poster_scheduled.place(relx=0.35, rely=0.2, anchor=tkinter.CENTER)

    value_scheduled = ctk.CTkLabel(root, text="8", font=ctk.CTkFont(
        family="Open Sans", size=80, weight="bold"), fg_color="#EA8C00", text_color="white")
    value_scheduled.place(relx=0.35, rely=0.180, anchor=tkinter.CENTER)

    description_scheduled = ctk.CTkLabel(root, text="Pets agendados", font=ctk.CTkFont(
        family="Open Sans", size=20, weight="bold"), fg_color="#EA8C00", text_color="white")
    description_scheduled.place(relx=0.35, rely=0.260, anchor=tkinter.CENTER)


    # Answered
    poster_answered = ctk.CTkFrame(root, bg_color="white", width=250,
                                height=180, border_color="#D9D9D9", border_width=1, fg_color="#FFA826")
    poster_answered.place(relx=0.580, rely=0.2, anchor=tkinter.CENTER)

    value_answered = ctk.CTkLabel(root, text="4", font=ctk.CTkFont(
        family="Open Sans", size=80, weight="bold"), fg_color="#FFA826", text_color="white")
    value_answered.place(relx=0.580, rely=0.180, anchor=tkinter.CENTER)

    description_answered = ctk.CTkLabel(root, text="Pets atendidos", font=ctk.CTkFont(
        family="Open Sans", size=20, weight="bold"), fg_color="#FFA826", text_color="white")
    description_answered.place(relx=0.580, rely=0.260, anchor=tkinter.CENTER)


    # Total
    poster_total = ctk.CTkFrame(root, bg_color="white", width=250,
                                height=180, border_color="#D9D9D9", border_width=1, fg_color="#F5B83D")
    poster_total.place(relx=0.81, rely=0.2, anchor=tkinter.CENTER)

    value_total = ctk.CTkLabel(root, text="82", font=ctk.CTkFont(
        family="Open Sans", size=80, weight="bold"), fg_color="#F5B83D", text_color="white")
    value_total.place(relx=0.81, rely=0.180, anchor=tkinter.CENTER)

    description_total = ctk.CTkLabel(root, text="Clientes totais", font=ctk.CTkFont(
        family="Open Sans", size=20, weight="bold"), fg_color="#F5B83D", text_color="white")
    description_total.place(relx=0.81, rely=0.260, anchor=tkinter.CENTER)


    ############### CONTAINER - BOX ###############


    boxContainer = MyFrame(master=root, width=825, height=400, bg_color="white", fg_color="white")
    boxContainer.place(relx=0.58, rely=0.650, anchor=tkinter.CENTER)

    # posicionamento na tela

    main_logo.place(x=30, y=60)
    dash_button.place(x=40, y=300)
    client_button.place(x=40, y=350)
    services_button.place(x=40, y=400)
    animals_button.place(x=40, y=450)
    exit_button.place(x=40, y=600)

    root.mainloop()

dashWindow()