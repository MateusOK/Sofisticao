from tkinter import *
import customtkinter
from PIL import Image


class ClientCard(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # container
        container = customtkinter.CTkFrame(self, bg_color="white", width=540,
                                           height=160, border_color="#D9D9D9", border_width=1, fg_color="white")
        container.grid(row=0, column=0)

        # logo - user
        logo_image = customtkinter.CTkImage(light_image=Image.open(
            "assets\\client__page\\user.png"))
        logo_label = customtkinter.CTkLabel(
            self, text="", image=logo_image, fg_color="white")
        logo_label.place(x=23, y=15)

        # title - user
        animal_title = customtkinter.CTkLabel(self, text="Cleiton Rasta, 24 anos", font=customtkinter.CTkFont(
            family="Open Sans", size=16), fg_color="white", text_color="#292929")
        animal_title.place(x=50, y=15)

        # logo - map
        logo_image = customtkinter.CTkImage(light_image=Image.open(
            "assets\\client__page\\location.png"))
        logo_label = customtkinter.CTkLabel(
            self, text="", image=logo_image, fg_color="white")
        logo_label.place(x=23, y=50)

        # title - map
        animal_title = customtkinter.CTkLabel(self, text="Registro - SP, 11900-000", font=customtkinter.CTkFont(
            family="Open Sans", size=16), fg_color="white", text_color="#292929")
        animal_title.place(x=50, y=48)

        # logo - location
        logo_image = customtkinter.CTkImage(light_image=Image.open(
            "assets\\client__page\\location__icon.png"))
        logo_label = customtkinter.CTkLabel(
            self, text="", image=logo_image, fg_color="white")
        logo_label.place(x=23, y=85)

        # title - location
        animal_title = customtkinter.CTkLabel(self, text="Avenida bom dia e cia ai papai esqueça, 2258, Bairro maneiro", font=customtkinter.CTkFont(
            family="Open Sans", size=16), fg_color="white", text_color="#292929")
        animal_title.place(x=50, y=85)

        # logo - telephone
        logo_image = customtkinter.CTkImage(light_image=Image.open(
            "assets\\client__page\\telephone.png"))
        logo_label = customtkinter.CTkLabel(
            self, text="", image=logo_image, fg_color="white")
        logo_label.place(x=23, y=120)

        # title - telephone
        animal_title = customtkinter.CTkLabel(self, text="(13) 9648-9955", font=customtkinter.CTkFont(
            family="Open Sans", size=16), fg_color="white", text_color="#292929")
        animal_title.place(x=50, y=120)

        # text - right
        animal_title = customtkinter.CTkLabel(self, text="Cliente desde 11 de setembro de 2022", font=customtkinter.CTkFont(
            family="Open Sans", size=12, weight="bold"), fg_color="white", text_color="#A4A4A4")
        animal_title.place(x=300, y=125)

        # logo - dog
        logo_image = customtkinter.CTkImage(light_image=Image.open(
            "assets\\client__page\\logo.png"))
        logo_label = customtkinter.CTkLabel(
            self, text="", image=logo_image, fg_color="white")
        logo_label.place(x=450, y=15)

        # title - dog
        animal_title = customtkinter.CTkLabel(self, text="2 pets", font=customtkinter.CTkFont(
            family="Open Sans", size=16), fg_color="white", text_color="#292929")
        animal_title.place(x=475, y=15)
