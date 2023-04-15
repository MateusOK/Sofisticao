import tkinter
import customtkinter
from PIL import Image




class Menu(customtkinter.CTkFrame):
     def __init__(self, master, txt_color, fg_color, **kwargs):
        super().__init__(master, **kwargs)
        self.txt_color = txt_color
        self.fg_color = fg_color

        division = customtkinter.CTkFrame(self, bg_color="white", width=250,
                                height=1450,  fg_color="#E0E0E0")
        division.place(relx=0, rely=0, anchor=tkinter.W)

        side_line = customtkinter.CTkFrame(self, bg_color="white", width=4,
                                height=170,  fg_color="#FFA826")
        side_line.place(x=15, y=310)


        #commands
        def sair():
            master.destroy()

        def openClient():
            master.destroy()
            from clients import clientsWindow
            clientsWindow()

        def openServices():
            master.destroy()
            from services import servicesWindow
            servicesWindow()

        # images
        logo = customtkinter.CTkImage(light_image=Image.open("assets\\logo.png"), size=(200,160))
        dash_logo = customtkinter.CTkImage(light_image=Image.open(
            "assets\\dashboard_logo_white.png"))
        client_logo = customtkinter.CTkImage(light_image=Image.open("assets\\client_logo.png"))
        services_logo = customtkinter.CTkImage(
            light_image=Image.open("assets\\services_logo.png"))
        animals_logo = customtkinter.CTkImage(light_image=Image.open("assets\\animals_logo.png"))
        exit_logo = customtkinter.CTkImage(light_image=Image.open("assets\\exit_logo.png"))

        # labels
        main_logo = customtkinter.CTkLabel(self, text="" ,image=logo, bg_color="#E0E0E0")

        # buttons
        dash_button = customtkinter.CTkButton(self, text="Dashboard", image=dash_logo, fg_color=self.fg_color,
                                    corner_radius=5, height=35, width=180, bg_color="#F2F2F2",  font=customtkinter.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D")
        client_button = customtkinter.CTkButton(self, text="       Clientes", text_color=self.txt_color, image=client_logo, corner_radius=7,
                                    fg_color=self.fg_color, height=35, width=180, bg_color="#E0E0E0",  font=customtkinter.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D", command=openClient)
        services_button = customtkinter.CTkButton(self, image=services_logo, text="      Serviços", text_color="black", corner_radius=7,
                                        fg_color=self.fg_color, height=35, width=180, bg_color="#E0E0E0",  
                                        font=customtkinter.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D", command=openServices)
        animals_button = customtkinter.CTkButton(self, image=animals_logo, text="        Animais", text_color="black", corner_radius=7,
                                    fg_color=self.fg_color, height=35, width=180, bg_color="#E0E0E0",  font=customtkinter.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D")
        exit_button = customtkinter.CTkButton(self, image=exit_logo, text="  Sair", text_color="black", corner_radius=7,
                                    fg_color=self.fg_color, height=35, width=180, bg_color="#E0E0E0", compound="right", font=customtkinter.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D", command=sair)

        main_logo.place(x=30, y=60)
        dash_button.place(x=40, y=300)
        client_button.place(x=40, y=350)
        services_button.place(x=40, y=400)
        animals_button.place(x=40, y=450)
        exit_button.place(x=40, y=600)