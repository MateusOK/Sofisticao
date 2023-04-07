import tkinter
import customtkinter as ctk
from PIL import Image


root = ctk.CTk()  # create CTk window like you do with the Tk window
root.geometry("1280x720")
root.resizable(False, False)
root.config(background="#FFFFFF")


# container
container = ctk.CTkFrame(root, bg_color="white", width=790,
                         height=158, border_color="#D9D9D9", border_width=3,  fg_color="white")
container.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


# logo image
logo_image = ctk.CTkImage(light_image=Image.open(
    "assets\dashboard__container\logo_container.png"), size=(50, 50))
logo_label = ctk.CTkLabel(root, text="", image=logo_image)
logo_label.place(relx=0.22, rely=0.46, anchor=tkinter.CENTER)


# title at container
animal_title = ctk.CTkLabel(root, text="Nome do animal")
animal_title.place(relx=0.28, rely=0.45, anchor=tkinter.CENTER)
root.mainloop()
