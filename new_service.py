import tkinter
import customtkinter as ctk
from PIL import Image

def newServiceWindow():
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
    
    def openDash():
        root.destroy()
        from dash import dashWindow
        dashWindow()
    
    def backClients():
        root.destroy()
        from clients import clientsWindow
        clientsWindow()
    
    def backSerivces():
        root.destroy()
        from services import servicesWindow
        servicesWindow()

    # images
    logo = ctk.CTkImage(light_image=Image.open("assets\\logo.png"), size=(200,160))
    dash_logo = ctk.CTkImage(light_image=Image.open("assets\\dashboard_logo.png"))
    client_logo = ctk.CTkImage(light_image=Image.open("assets\\client_logo.png"))
    services_logo = ctk.CTkImage(light_image=Image.open("assets\\services_logo_white.png"))
    animals_logo = ctk.CTkImage(light_image=Image.open("assets\\animals_logo.png"))
    exit_logo = ctk.CTkImage(light_image=Image.open("assets\\exit_logo.png"))
    save_logo = ctk.CTkImage(light_image=Image.open("assets\\salvar_logo.png"))
    quit_logo = ctk.CTkImage(light_image=Image.open("assets\\quit.png"))
    

    # labels
    main_logo = ctk.CTkLabel(root, text="" ,image=logo, bg_color="#E0E0E0")

    # buttons
    dash_button = ctk.CTkButton(root, text="Dashboard", image=dash_logo, fg_color="white", text_color="black",
                                corner_radius=5, height=35, width=180, bg_color="#F2F2F2",  font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D", command=openDash)
    client_button = ctk.CTkButton(root, text="       Clientes", image=client_logo, corner_radius=7, text_color="black",
                                fg_color="white", height=35, width=180, bg_color="#E0E0E0",  font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D", command=backClients)
    services_button = ctk.CTkButton(root, image=services_logo, text="      Serviços", corner_radius=7,
                                    fg_color="#F2800D", height=35, width=180, bg_color="#E0E0E0",  
                                    font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D", command=backSerivces)
    animals_button = ctk.CTkButton(root, image=animals_logo, text="        Animais", text_color="black", corner_radius=7,
                                fg_color="white", height=35, width=180, bg_color="#E0E0E0",  font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D")
    exit_button = ctk.CTkButton(root, image=exit_logo, text="  Sair", text_color="black", corner_radius=7,
                                fg_color="white", height=35, width=180, bg_color="#E0E0E0", compound="right", font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D", command=sair)
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

    #logo
    main_logo.place(x=30, y=60)
    #buttons
    dash_button.place(x=40, y=300)
    client_button.place(x=40, y=350)
    services_button.place(x=40, y=400)
    animals_button.place(x=40, y=450)
    exit_button.place(x=40, y=600)
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