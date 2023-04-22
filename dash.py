import tkinter
import customtkinter as ctk
from PIL import Image
from components.scrollContainer import MyFrame
from components.menu import *

def dashWindow():
    root = ctk.CTk()  # create CTk window like you do with the Tk window
    root.geometry("1280x720")
    root.resizable(False, False)
    root.config(background="#FFFFFF")

    menuContainer = Menu(master=root, width=250, height=1450)
    menuContainer.grid(row=0, column=0)

    #buttons
    menuContainer.dashButton(bg_color="#E0E0E0", fg_color="#FFA826", text_color="white",image=menuContainer.dash_logo_white, master=root)
    menuContainer.clientButton(**padrao, image=menuContainer.client_logo, master=root)
    menuContainer.servicesButton(**padrao, image=menuContainer.services_logo, master=root)
    menuContainer.animalsButton(**padrao, image=menuContainer.animals_logo, master=root)
    menuContainer.exitButton(master=root)
   
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

  

    root.mainloop()