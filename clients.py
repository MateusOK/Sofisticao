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

    ################ POSTER  ###############

    # Dashboard - Title

    title_poster = ctk.CTkLabel(root, text="Clientes", font=ctk.CTkFont(
        family="Nunito", size=20, weight="bold"), fg_color="white", text_color="black")
    title_poster.place(relx=0.6, rely=0.040, anchor=tkinter.CENTER)

    client__scroll = ClientScroll(
        master=root, width=560, height=500, bg_color="white", fg_color="white")
    client__scroll.place(x=500, y=150)

    root.mainloop()


clientsWindow()
