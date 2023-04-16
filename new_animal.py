import tkinter
import customtkinter as ctk
from PIL import Image
from components.menu import Menu

def newAnimalWindow():
    root = ctk.CTk()  # create CTk window like you do with the Tk window
    root.geometry("1280x720")
    root.resizable(False, False)
    root.config(background="#FFFFFF")

    menuContainer = Menu(master=root, width=250, height=1450, txt_color="white", fg_color="#FFA826")
    menuContainer.grid(row=0, column=0)

    #images
    save_logo = ctk.CTkImage(light_image=Image.open("assets\\salvar_logo.png"))


    #radioButtons
    radio_var = tkinter.IntVar(root)
    masc = ctk.CTkRadioButton(root, text="Masculino", variable=radio_var, value=1, bg_color="white", 
                              fg_color="#EA8C00", text_color="black", hover_color="#EA8C00", radiobutton_height=17, radiobutton_width=17)
    femn = ctk.CTkRadioButton(root, text="Feminino", variable=radio_var, value=2, bg_color="white", 
                              fg_color="#EA8C00", text_color="black", hover_color="#EA8C00", radiobutton_height=17, radiobutton_width=17)

    #buttons
    save_button = ctk.CTkButton(root, image=save_logo, text="  Salvar", text_color="white", corner_radius=7,
                                fg_color="#FFA826", height=40, width=200, bg_color="#E0E0E0", font=ctk.CTkFont(family="Nunito", size=15, weight="bold"), hover_color="#F2800D", cursor="hand2")


    #entrys
    client_cpf_input = ctk.CTkEntry(root, placeholder_text="CPF", bg_color="white", fg_color="white", 
                              width=300, height=40, corner_radius=8, text_color="black")
    animal_name_input = ctk.CTkEntry(root, placeholder_text="Nome", bg_color="white", fg_color="white", 
                              width=300, height=40, corner_radius=8, text_color="black")
    deficiencias_input = ctk.CTkEntry(root, placeholder_text="Deficiências", bg_color="white", fg_color="white", 
                              width=605, height=70, corner_radius=8, text_color="black")
    intolerancias_input = ctk.CTkEntry(root, placeholder_text="Intolerâncias", bg_color="white", fg_color="white", 
                              width=605, height=70, corner_radius=8, text_color="black")
    idade_input = ctk.CTkEntry(root, placeholder_text="Anos", bg_color="white", fg_color="white", 
                              width=165, height=40, corner_radius=8, text_color="black")
    idade_prox_input = ctk.CTkEntry(root, placeholder_text="Meses", bg_color="white", fg_color="white", 
                              width=165, height=40, corner_radius=8, text_color="black")
    data_input = ctk.CTkEntry(root, placeholder_text="01/01/23", bg_color="white", fg_color="white", 
                              width=165, height=40, corner_radius=8, text_color="black")


    #labels
    new_service_text = ctk.CTkLabel(root, text="Novo animal", font=ctk.CTkFont(family="Nunito", size=25, weight="bold"), 
                              bg_color="white", text_color="#292929")
    client_cpf_text = ctk.CTkLabel(root, text="CPF do cliente", font=ctk.CTkFont(family="Nunito", size=12, weight="bold"), 
                              bg_color="white", text_color="#292929")
    animal_name_text = ctk.CTkLabel(root, text="Nome do animal", font=ctk.CTkFont(family="Nunito", size=12, weight="bold"), 
                              bg_color="white", text_color="#292929")
    deficiencias_text = ctk.CTkLabel(root, text="Deficiências", font=ctk.CTkFont(family="Nunito", size=12, weight="bold"), 
                              bg_color="white", text_color="#292929")
    intolerancias_text = ctk.CTkLabel(root, text="Intolerâncias", font=ctk.CTkFont(family="Nunito", size=12, weight="bold"), 
                              bg_color="white", text_color="#292929")
    idade_text = ctk.CTkLabel(root, text="Idade aproximada (anos)", font=ctk.CTkFont(family="Nunito", size=12, weight="bold"), 
                              bg_color="white", text_color="#292929")
    idade_prox_text = ctk.CTkLabel(root, text="Idade aproximada (meses)", font=ctk.CTkFont(family="Nunito", size=12, weight="bold"), 
                              bg_color="white", text_color="#292929")
    data_text = ctk.CTkLabel(root, text="Data de nascimento", font=ctk.CTkFont(family="Nunito", size=12, weight="bold"), 
                              bg_color="white", text_color="#292929")
    sexo_text = ctk.CTkLabel(root, text="Sexo", font=ctk.CTkFont(family="Nunito", size=12, weight="bold"), 
                              bg_color="white", text_color="#292929")
    



    # posicionamento na tela


    #texts
    new_service_text.place(x=500, y=160)
    client_cpf_text.place(x=500, y=200)
    animal_name_text.place(x=805, y=200)
    deficiencias_text.place(x=500, y=275)
    intolerancias_text.place(x=500, y=380)
    idade_text.place(x=670, y=480)
    idade_prox_text.place(x=837, y=480)
    data_text.place(x=500, y=480)
    sexo_text.place(x=1010, y=480)

    #inputs
    client_cpf_input.place(x=500, y=230)
    animal_name_input.place(x=805, y=230)
    deficiencias_input.place(x=500, y=305)
    intolerancias_input.place(x=500, y=410)
    idade_input.place(x=668, y=510)
    data_input.place(x=500, y=510)
    idade_prox_input.place(x=835, y=510)

    #radiobuttons
    masc.place(x=1010, y=508)
    femn.place(x=1010, y=530)

    #buttons
    save_button.place(x=910, y=600)

    root.mainloop()
newAnimalWindow()