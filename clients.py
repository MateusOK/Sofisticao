import tkinter
import customtkinter as ctk
from PIL import Image
from new_client import newClientWindow
from components.menu import Menu
from components.scrollClient import ClientScroll


def clientsWindow():
    root = ctk.CTk()  # create CTk window like you do with the Tk window
    root.geometry("1280x720")
    root.resizable(False, False)
    root.config(background="#FFFFFF")

    menuContainer = Menu(master=root, width=250, height=1450,
                         txt_color="white", fg_color="#FFA826")
    menuContainer.grid(row=0, column=0)

   # Search bar

    search_logo = ctk.CTkImage(light_image=Image.open(
        "assets\\client__page\\search.png"))

    search = ctk.CTkEntry(root, bg_color="white", border_color="#C9C9C9", fg_color="white",
                          placeholder_text="Cleiton Rasta", text_color="black", width=485, height=48)
    search.place(x=505, y=70)

    btn_search = ctk.CTkButton(root, text="", image=search_logo, width=80, height=48,
                               bg_color="white", fg_color="#FFA826", hover_color="#FF9D0A")
    btn_search.place(x=1000, y=70)

    results_text = ctk.CTkLabel(root, text="5 resultados", font=ctk.CTkFont(
        family="Nunito", size=13, weight="bold"), fg_color="white", text_color="#A4A4A4")
    results_text.place(x=1000, y=120)

    # Scroll - Container

    title_poster = ctk.CTkLabel(root, text="Clientes", font=ctk.CTkFont(
        family="Nunito", size=20, weight="bold"), fg_color="white", text_color="black")
    title_poster.place(relx=0.6, rely=0.040, anchor=tkinter.CENTER)

    client__scroll = ClientScroll(
        master=root, width=560, height=500, bg_color="white", fg_color="white")
    client__scroll.place(x=500, y=150)

    root.mainloop()


clientsWindow()
