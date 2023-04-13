import tkinter
import customtkinter as ctk
from PIL import Image

def newClientWindow():
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

    # images
    logo = ctk.CTkImage(light_image=Image.open("assets\\logo.png"), size=(200,160))
    dash_logo = ctk.CTkImage(light_image=Image.open(
        "assets\\dashboard_logo.png"))
    client_logo = ctk.CTkImage(light_image=Image.open("assets\\clients_logo_white.png"))
    services_logo = ctk.CTkImage(
        light_image=Image.open("assets\\services_logo.png"))
    animals_logo = ctk.CTkImage(light_image=Image.open("assets\\animals_logo.png"))
    exit_logo = ctk.CTkImage(light_image=Image.open("assets\\exit_logo.png"))
    save_logo = ctk.CTkImage(light_image=Image.open("assets\\salvar_logo.png"))
    quit_logo = ctk.CTkImage(light_image=Image.open("assets\\quit.png"))
    

    # labels
    main_logo = ctk.CTkLabel(root, text="" ,image=logo, bg_color="#E0E0E0")

    # buttons
    dash_button = ctk.CTkButton(root, text="Dashboard", image=dash_logo, fg_color="white", text_color="black",
                                corner_radius=5, height=35, width=180, bg_color="#F2F2F2",  font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D", command=openDash)
    client_button = ctk.CTkButton(root, text="       Clientes", image=client_logo, corner_radius=7,
                                fg_color="#F2800D", height=35, width=180, bg_color="#E0E0E0",  font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D")
    services_button = ctk.CTkButton(root, image=services_logo, text="      Serviços", text_color="black", corner_radius=7,
                                    fg_color="white", height=35, width=180, bg_color="#E0E0E0",  font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D")
    animals_button = ctk.CTkButton(root, image=animals_logo, text="        Animais", text_color="black", corner_radius=7,
                                fg_color="white", height=35, width=180, bg_color="#E0E0E0",  font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D")
    exit_button = ctk.CTkButton(root, image=exit_logo, text="  Sair", text_color="black", corner_radius=7,
                                fg_color="white", height=35, width=180, bg_color="#E0E0E0", compound="right", font=ctk.CTkFont(family="Open Sans", size=12, weight="bold"), hover_color="#F2800D", command=sair)
    save_button = ctk.CTkButton(root, image=save_logo, text="  Salvar", text_color="white", corner_radius=7,
                                fg_color="#FFA826", height=35, width=200, bg_color="#E0E0E0", font=ctk.CTkFont(family="Nunito", size=15, weight="bold"), hover_color="#F2800D", cursor="hand2")
    quit_button = ctk.CTkButton(root, image=quit_logo, text="", text_color="white",
                                fg_color="white", height=5, width=5, bg_color="white", hover_color="white")


    #entrys
    name_input = ctk.CTkEntry(root, placeholder_text="Nome", bg_color="white", fg_color="white", 
                              width=300, height=40, corner_radius=8, text_color="black")
    CPF_input = ctk.CTkEntry(root, placeholder_text="CPF", bg_color="white", fg_color="white", 
                              width=300, height=40, corner_radius=8, text_color="black")
    celular_input = ctk.CTkEntry(root, placeholder_text="Número", bg_color="white", fg_color="white", 
                              width=175, height=40, corner_radius=8, text_color="black")
    data_input = ctk.CTkEntry(root, placeholder_text="Data", bg_color="white", fg_color="white", 
                              width=120, height=40, corner_radius=8, text_color="black")
    endereco_input = ctk.CTkEntry(root, placeholder_text="Endereço", bg_color="white", fg_color="white", 
                              width=300, height=40, corner_radius=8, text_color="black")
    cidade_input = ctk.CTkEntry(root, placeholder_text="Cidade", bg_color="white", fg_color="white", 
                              width=200, height=40, corner_radius=8, text_color="black")
    estado_input = ctk.CTkEntry(root, placeholder_text="SP", bg_color="white", fg_color="white", 
                              width=95, height=40, corner_radius=8, text_color="black")
    CEP_input = ctk.CTkEntry(root, placeholder_text="CEP", bg_color="white", fg_color="white", 
                              width=300, height=40, corner_radius=8, text_color="black")


    #labels
    new_client_text = ctk.CTkLabel(root, text="Novo Cliente", font=ctk.CTkFont(family="Nunito", size=25, weight="bold"), 
                              bg_color="white", text_color="#292929")
    name_text = ctk.CTkLabel(root, text="Nome", font=ctk.CTkFont(family="Nunito", size=12, weight="bold"), 
                              bg_color="white", text_color="#292929")
    cpf_text = ctk.CTkLabel(root, text="CPF", font=ctk.CTkFont(family="Nunito", size=12, weight="bold"), 
                              bg_color="white", text_color="#292929")
    celular_text = ctk.CTkLabel(root, text="Celular", font=ctk.CTkFont(family="Nunito", size=12, weight="bold"), 
                              bg_color="white", text_color="#292929")
    data_text = ctk.CTkLabel(root, text="Data de nasc.", font=ctk.CTkFont(family="Nunito", size=12, weight="bold"), 
                              bg_color="white", text_color="#292929")
    endereco_text = ctk.CTkLabel(root, text="Endereço", font=ctk.CTkFont(family="Nunito", size=12, weight="bold"), 
                              bg_color="white", text_color="#292929")
    cidade_text = ctk.CTkLabel(root, text="Cidade", font=ctk.CTkFont(family="Nunito", size=12, weight="bold"), 
                              bg_color="white", text_color="#292929")
    estado_text = ctk.CTkLabel(root, text="Estado", font=ctk.CTkFont(family="Nunito", size=12, weight="bold"), 
                              bg_color="white", text_color="#292929")
    cep_text = ctk.CTkLabel(root, text="CEP", font=ctk.CTkFont(family="Nunito", size=12, weight="bold"), 
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
    save_button.place(x=905, y=450)
    quit_button.place(x=1080, y=100)

    #texts
    new_client_text.place(x=500, y=160)
    name_text.place(x=500, y=200)
    cpf_text.place(x=805, y=200)
    celular_text.place(x=500, y=275)
    data_text.place(x=680, y=275)
    endereco_text.place(x=805, y=275)
    cidade_text.place(x=500, y=355)
    estado_text.place(x=705, y=355)
    cep_text.place(x=805, y=355)

    #inputs
    name_input.place(x=500, y=230)
    CPF_input.place(x=805, y=230)
    celular_input.place(x=500, y=305)
    data_input.place(x=679, y=305)
    endereco_input.place(x=805, y=305)
    cidade_input.place(x=500, y=385)
    estado_input.place(x=705, y=385)
    CEP_input.place(x=805, y=385)

    root.mainloop()