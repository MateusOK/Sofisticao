import tkinter
import customtkinter as ctk
from PIL import Image
from components.menu import *

def newServiceWindow():
    root = ctk.CTk()  # create CTk window like you do with the Tk window
    root.geometry("1280x720")
    root.resizable(False, False)
    root.config(background="#FFFFFF")

    root.iconbitmap("assets\\icon.ico")
    root.title("Novo Atendimento")

    menuContainer = Menu(master=root, width=250, height=1450)
    menuContainer.grid(row=0, column=0)
    
    #buttons
    menuContainer.dashButton(**padrao, image=menuContainer.dash_logo, master=root)
    menuContainer.clientButton(**padrao, image=menuContainer.client_logo, master=root)
    menuContainer.servicesButton(bg_color="#E0E0E0", fg_color="#FFA826", text_color="white", image=menuContainer.services_logo_white, master=root)
    menuContainer.animalsButton(**padrao, image=menuContainer.animals_logo, master=root)
    menuContainer.exitButton(master=root)

    def backSerivces():
        root.destroy()
        from services import servicesWindow
        servicesWindow()

    save_logo = ctk.CTkImage(light_image=Image.open("assets\\salvar_logo.png"))
    quit_logo = ctk.CTkImage(light_image=Image.open("assets\\quit.png"))

    save_button = ctk.CTkButton(root, image=save_logo, text="  Salvar", text_color="white", corner_radius=7,
                                fg_color="#FFA826", height=40, width=200, bg_color="#E0E0E0", font=ctk.CTkFont(family="Nunito", size=15, weight="bold"), hover_color="#F2800D", cursor="hand2")
    quit_button = ctk.CTkButton(root, image=quit_logo, text="", text_color="white",
                                fg_color="white", height=5, width=5, bg_color="white", hover_color="white", command=backSerivces)


    #entrys
    client_cpf_input = ctk.CTkEntry(root, placeholder_text="CPF", bg_color="white", fg_color="white", 
                              width=250, height=40, corner_radius=8, text_color="black")
    animal_name_input = ctk.CTkEntry(root, placeholder_text="Nome", bg_color="white", fg_color="white", 
                              width=250, height=40, corner_radius=8, text_color="black")
    time_input = ctk.CTkEntry(root, placeholder_text="1h", bg_color="white", fg_color="white", 
                              width=95, height=40, corner_radius=8, text_color="black")
    descricao_input = ctk.CTkEntry(root, placeholder_text="Descrição", bg_color="white", fg_color="white", 
                              width=605, height=100, corner_radius=8, text_color="black")
    preco_input = ctk.CTkEntry(root, placeholder_text="R$", bg_color="white", fg_color="white", 
                              width=150, height=40, corner_radius=8, text_color="black")
    hora_inicio_input = ctk.CTkEntry(root, placeholder_text="18H", bg_color="white", fg_color="white", 
                              width=150, height=40, corner_radius=8, text_color="black")


    #labels
    new_service_text = ctk.CTkLabel(root, text="Novo atendimento", font=ctk.CTkFont(family="Nunito", size=25, weight="bold"), 
                              bg_color="white", text_color="#292929")
    client_cpf_text = ctk.CTkLabel(root, text="CPF do cliente", font=ctk.CTkFont(family="Nunito", size=12, weight="bold"), 
                              bg_color="white", text_color="#292929")
    animal_name_text = ctk.CTkLabel(root, text="Nome do animal", font=ctk.CTkFont(family="Nunito", size=12, weight="bold"), 
                              bg_color="white", text_color="#292929")
    time_text = ctk.CTkLabel(root, text="Duração", font=ctk.CTkFont(family="Nunito", size=12, weight="bold"), 
                              bg_color="white", text_color="#292929")
    descricao_text = ctk.CTkLabel(root, text="Descrição", font=ctk.CTkFont(family="Nunito", size=12, weight="bold"), 
                              bg_color="white", text_color="#292929")
    preco_text = ctk.CTkLabel(root, text="Preço", font=ctk.CTkFont(family="Nunito", size=12, weight="bold"), 
                              bg_color="white", text_color="#292929")
    hora_inicio_text = ctk.CTkLabel(root, text="Horário de início", font=ctk.CTkFont(family="Nunito", size=12, weight="bold"), 
                              bg_color="white", text_color="#292929")
    



    # posicionamento na tela

    #buttons
    save_button.place(x=905, y=440)
    quit_button.place(x=1080, y=150)

    #texts
    new_service_text.place(x=500, y=160)
    client_cpf_text.place(x=500, y=200)
    animal_name_text.place(x=757, y=200)
    time_text.place(x=1013, y=200)
    descricao_text.place(x=500, y=275)
    preco_text.place(x=655, y=410)
    hora_inicio_text.place(x=500, y=410)

    #inputs
    client_cpf_input.place(x=500, y=230)
    animal_name_input.place(x=755, y=230)
    time_input.place(x=1010, y=230)
    descricao_input.place(x=500, y=305)
    preco_input.place(x=655, y=440)
    hora_inicio_input.place(x=500, y=440)

    root.mainloop()