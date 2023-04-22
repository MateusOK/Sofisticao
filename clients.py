import tkinter
import customtkinter as ctk
from PIL import Image
from components.menu import *
from components.scrollClient import ClientScroll


def clientsWindow():
    root = ctk.CTk()  # create CTk window like you do with the Tk window
    root.geometry("1280x720")
    root.resizable(False, False)
    root.config(background="#FFFFFF")

    root.iconbitmap("assets\\icon.ico")
    root.title("Clientes")

    menuContainer = Menu(master=root, width=250, height=1450)
    menuContainer.grid(row=0, column=0)

    # buttons
    menuContainer.dashButton(
        **padrao, image=menuContainer.dash_logo, master=root)
    menuContainer.clientButton(bg_color="#E0E0E0", fg_color="#FFA826",
                               text_color="white", image=menuContainer.client_logo_white, master=root)
    menuContainer.servicesButton(
        **padrao, image=menuContainer.services_logo, master=root)
    menuContainer.animalsButton(
        **padrao, image=menuContainer.animals_logo, master=root)
    menuContainer.exitButton(master=root)

    ################ POSTER  ###############

    search_logo = ctk.CTkImage(light_image=Image.open(
        "assets\\client__page\\search.png"))

    search = ctk.CTkEntry(root, bg_color="white", border_color="#C9C9C9", fg_color="white",
                          placeholder_text="Cleiton Rasta", text_color="black", width=485, height=48)
    search.place(x=505, y=70)

    btn_search = ctk.CTkButton(root, text="", image=search_logo, width=80, height=48,
                               bg_color="white", fg_color="#FFA826", hover_color="#FF9D0A", cursor="hand2")
    btn_search.place(x=1000, y=70)

    results_text = ctk.CTkLabel(root, text="5 resultados", font=ctk.CTkFont(
        family="Nunito", size=13, weight="bold"), fg_color="white", text_color="#A4A4A4")
    results_text.place(x=1000, y=120)

    # Scroll - Container

    title_poster = ctk.CTkLabel(root, text="Clientes", font=ctk.CTkFont(
        family="Nunito", size=20, weight="bold"), fg_color="white", text_color="black")
    title_poster.place(relx=0.6, rely=0.040, anchor=tkinter.CENTER)

    client__scroll = ClientScroll(
        master=root, width=560, height=450, bg_color="white", fg_color="white")
    client__scroll.place(x=500, y=150)

    # Button - Add

    def openNewClient():
        root.destroy()
        from new_client import newClientWindow
        newClientWindow() 


    add_image = ctk.CTkImage(light_image=Image.open(
        "assets\\client__page\\add-icon.png"))

    add_button = ctk.CTkButton(root, text="Novo", image=add_image, font=ctk.CTkFont(
        family="Nunito", size=13, weight="bold"), fg_color="#FFA826", bg_color="white" ,text_color="#FFFFFF", hover_color="#FF9D0A", command=openNewClient)
    add_button.place(x=910, y=625)

    root.mainloop()
