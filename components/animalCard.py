from tkinter import *
import customtkinter
from PIL import Image


class AnimalCard(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # container
        container = customtkinter.CTkFrame(self, bg_color="white", width=790,
                                           height=124, border_color="#D9D9D9", border_width=1, fg_color="white")
        container.grid(row=0, column=0)

        # logo - image
        logo_image = customtkinter.CTkImage(light_image=Image.open(
            "assets\\animals_page\\logo_icon.png"), size=(50, 50))
        logo_label = customtkinter.CTkLabel(
            self, text="", image=logo_image, fg_color="white")
        logo_label.grid(row=0, column=0,
                        sticky=customtkinter.NW, padx=15, pady=20)

        # title - container
        animal_title = customtkinter.CTkLabel(self, text="Nome do animal", font=customtkinter.CTkFont(
            family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#292929")
        animal_title.grid(
            row=0, column=0, sticky=customtkinter.NW, padx=80, pady=25)

        # subtitle - container
        owner_title = customtkinter.CTkLabel(self, text="Nome do dono", font=customtkinter.CTkFont(
            family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#6A6A6A")
        owner_title.grid(
            row=0, column=0, sticky=customtkinter.NW, padx=80, pady=45)

        contact_title = customtkinter.CTkLabel(self, text="Contato:", font=customtkinter.CTkFont(
            family="Open Sans", size=14, weight="bold"), fg_color="white", text_color="#6A6A6A")
        contact_title.place(x=600, y=95)

        contact_title_placeholder = customtkinter.CTkLabel(self, text="(13) 9684-4814", font=customtkinter.CTkFont(
            family="Open Sans", size=14), fg_color="white", text_color="#6A6A6A")
        contact_title_placeholder.place(x=665, y=95)

        date_text = customtkinter.CTkLabel(self, text="Último atendimento: 14/04/2022", font=customtkinter.CTkFont(
            family="Open Sans", size=14, weight="bold"), fg_color="white", text_color="#4E4E4E")
        date_text.grid(row=0, column=0, sticky=customtkinter.SW,
                       padx=10, pady=5)

        # division - container
        division = customtkinter.CTkFrame(self, bg_color="white", width=3,
                                          height=81,  fg_color="#DCDCDC")
        division.grid(row=0, column=0, sticky=customtkinter.NW,
                      padx=319, pady=10)

        # Animal informations

        # Animal
        animal_title_description = customtkinter.CTkLabel(self, text="Animal:", font=customtkinter.CTkFont(
            family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#292929")
        animal_title_description.place(x=337, y=25)

        animal__description = customtkinter.CTkLabel(self, text="Gato", font=customtkinter.CTkFont(
            family="Open Sans", size=16), fg_color="white", text_color="#292929")
        animal__description.place(x=400, y=25)

        # Gender
        gender_title_description = customtkinter.CTkLabel(self, text="Sexo:", font=customtkinter.CTkFont(
            family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#292929")
        gender_title_description.place(x=460, y=25)

        gender__description = customtkinter.CTkLabel(self, text="Masculino", font=customtkinter.CTkFont(
            family="Open Sans", size=16), fg_color="white", text_color="#292929")
        gender__description.place(x=510, y=25)

        # Age
        age_title_description = customtkinter.CTkLabel(self, text="Idade:", font=customtkinter.CTkFont(
            family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#292929")
        age_title_description.place(x=605, y=25)

        age__description = customtkinter.CTkLabel(self, text="8 anos", font=customtkinter.CTkFont(
            family="Open Sans", size=16), fg_color="white", text_color="#292929")
        age__description.place(x=660, y=25)

        # Deficiency
        deficiency_title_description = customtkinter.CTkLabel(self, text="Deficiências:", font=customtkinter.CTkFont(
            family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#292929")
        deficiency_title_description.place(x=337, y=45)

        deficiency__description = customtkinter.CTkLabel(self, text="Autismo", font=customtkinter.CTkFont(
            family="Open Sans", size=16), fg_color="white", text_color="#292929")
        deficiency__description.place(x=440, y=45)

        # Intolerance
        deficiency_title_description = customtkinter.CTkLabel(self, text="Intolerâncias:", font=customtkinter.CTkFont(
            family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#292929")
        deficiency_title_description.place(x=337, y=65)

        deficiency__description = customtkinter.CTkLabel(self, text="Medicamentos com base em folhas", font=customtkinter.CTkFont(
            family="Open Sans", size=16), fg_color="white", text_color="#292929")
        deficiency__description.place(x=445, y=65)
