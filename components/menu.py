import tkinter
import customtkinter as ctk
from PIL import Image

#parametros padrao
padrao = {"fg_color" : "white", "bg_color" : "#E0E0E0", "text_color" : "black"} 

class Menu(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        division = ctk.CTkFrame(self, bg_color="white", width=250,
                                height=1450,  fg_color="#E0E0E0")
        division.place(relx=0, rely=0, anchor=tkinter.W)

        side_line = ctk.CTkFrame(self, bg_color="white", width=4,
                                height=170,  fg_color="#FFA826")
        side_line.place(x=15, y=310)

                # images
        logo = ctk.CTkImage(light_image=Image.open("assets\\logo.png"), size=(200,160))

        # labels
        main_logo = ctk.CTkLabel(self, text="" ,image=logo, bg_color="#E0E0E0")
        main_logo.place(x=30, y=60)

        #logos
        self.dash_logo = ctk.CTkImage(light_image=Image.open("assets\\dashboard_logo.png"))
        self.client_logo = ctk.CTkImage(light_image=Image.open("assets\\client_logo.png"))
        self.services_logo = ctk.CTkImage(light_image=Image.open("assets\\services_logo.png"))
        self.animals_logo = ctk.CTkImage(light_image=Image.open("assets\\animals_logo.png"))
        self.exit_logo = ctk.CTkImage(light_image=Image.open("assets\\exit_logo.png"))

        #white_logos
        self.dash_logo_white = ctk.CTkImage(light_image=Image.open("assets\\dashboard_logo_white.png"))
        self.client_logo_white = ctk.CTkImage(light_image=Image.open("assets\\clients_logo_white.png"))
        self.services_logo_white = ctk.CTkImage(light_image=Image.open("assets\\services_logo_white.png"))
        self.animals_logo_white = ctk.CTkImage(light_image=Image.open("assets\\animals_logo_white.png"))

    # outside of __init__
    def dashButton(self, master, fg_color, bg_color, text_color, image):
        self.dash_button = ctk.CTkButton(master, text="Dashboard", image=image, fg_color=fg_color,    
                    corner_radius=5, height=35, width=180, bg_color=bg_color,  font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D", text_color=text_color, command=lambda: self.openDash())
        self.dash_button.place(x=40, y=300)
    
    def clientButton(self, master, fg_color, bg_color, text_color, image):
        self.client_button = ctk.CTkButton(master, text="       Clientes", text_color=text_color, image=image, corner_radius=7,
                    fg_color=fg_color, height=35, width=180, bg_color=bg_color,  font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D", command=lambda: self.openClient())
        self.client_button.place(x=40, y=350)

    def servicesButton(self, master, fg_color, bg_color, text_color, image):
        self.services_button = ctk.CTkButton(master, text="      Serviços", text_color=text_color, image=image, corner_radius=7,
                    fg_color=fg_color, height=35, width=180, bg_color=bg_color,  
                    font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D", command=lambda: self.openServices())
        self.services_button.place(x=40, y=400)
    
    def animalsButton(self, master, fg_color, bg_color, text_color, image):

        self.animals_button = ctk.CTkButton(master, image=image, text="        Animais", text_color=text_color, corner_radius=7,
                    fg_color=fg_color, height=35, width=180, bg_color=bg_color,  
                    font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D", command=lambda: self.openAnimals())
        self.animals_button.place(x=40, y=450)

    def exitButton(self, master):

            self.exit_button = ctk.CTkButton(master, image=self.exit_logo, text="  Sair", text_color="black", corner_radius=7,
                    fg_color="white", height=35, width=180, bg_color="#E0E0E0", compound="right", 
                    font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D", command=lambda: self.sair())
            self.exit_button.place(x=40, y=600)
    
    
    
    
    


    #commands
    def openDash(self):
        self.master.destroy()
        from dash import dashWindow
        dashWindow()


    def openClient(self):
        self.master.destroy()
        from clients import clientsWindow
        clientsWindow()

    def openServices(self):
        self.master.destroy()
        from services import servicesWindow
        servicesWindow()

    def openAnimals(self):
        self.master.destroy()
        from animal import animalWindow
        animalWindow()

    def sair(self):
        self.master.destroy()
        from main import loginWindow
        loginWindow()