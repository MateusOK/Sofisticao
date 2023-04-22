import tkinter
import customtkinter as ctk
from PIL import Image
from components.menu import *
from components.scrollAnimals import AnimalScroll


def animalWindow():
    root = ctk.CTk()  # create CTk window like you do with the Tk window
    root.geometry("1280x720")
    root.resizable(False, False)
    root.config(background="#FFFFFF")

    root.iconbitmap("assets\\icon.ico")
    root.title("Animais")


    menuContainer = Menu(master=root, width=250, height=1450)
    menuContainer.grid(row=0, column=0)

    # buttons
    menuContainer.dashButton(**padrao, image=menuContainer.dash_logo, master=root)
    menuContainer.clientButton(**padrao, image=menuContainer.client_logo, master=root)
    menuContainer.servicesButton(**padrao, image=menuContainer.services_logo, master=root)
    menuContainer.animalsButton(bg_color="#E0E0E0", fg_color="#FFA826", text_color="white", image=menuContainer.animals_logo_white, master=root)
    menuContainer.exitButton(master=root)

    title_poster = ctk.CTkLabel(root, text="Animais", font=ctk.CTkFont(
        family="Nunito", size=20, weight="bold"), fg_color="white", text_color="black")
    title_poster.place(relx=0.6, rely=0.040, anchor=tkinter.CENTER)

    search_logo = ctk.CTkImage(light_image=Image.open(
        "assets\\client__page\\search.png"))

    # Search Bar

    search = ctk.CTkEntry(root, bg_color="white", border_color="#C9C9C9", fg_color="white",
                          placeholder_text="Bixanuuu apelão", text_color="black", width=680, height=48)
    search.place(x=325, y=70)

    btn_search = ctk.CTkButton(root, text="", image=search_logo, width=141, height=48,
                               bg_color="white", fg_color="#FFA826", hover_color="#FF9D0A", cursor="hand2")
    btn_search.place(x=1020, y=70)

    results_text = ctk.CTkLabel(root, text="5 resultados", font=ctk.CTkFont(
        family="Nunito", size=13, weight="bold"), fg_color="white", text_color="#A4A4A4")
    results_text.place(x=1080, y=120)

    # Scroll - Container

    boxContainer = AnimalScroll(master=root, width=825,
                                height=500, bg_color="white", fg_color="white")
    boxContainer.place(relx=0.58, rely=0.558, anchor=tkinter.CENTER)

    # Button - Add

    def openNewAnimal():
        root.destroy()
        from new_animal import newAnimalWindow
        newAnimalWindow()


    add_image = ctk.CTkImage(light_image=Image.open(
        "assets\\client__page\\add-icon.png"))

    add_button = ctk.CTkButton(root, text="Adicionar", image=add_image, font=ctk.CTkFont(
        family="Nunito", size=15, weight="bold"), height=35, fg_color="#FFA826", bg_color="white" ,text_color="#FFFFFF", hover_color="#FF9D0A", command=openNewAnimal)
    add_button.place(x=1010, y=670)

    root.mainloop()