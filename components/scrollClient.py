from tkinter import *
import customtkinter
from components.clientCard import ClientCard


class ClientScroll(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        cardBox = ClientCard(master=self)
        cardBox_2 = ClientCard(master=self)
        cardBox_3 = ClientCard(master=self)
        cardBox_4 = ClientCard(master=self)
        cardBox_5 = ClientCard(master=self)
        cardBox.grid(row=0, column=0)
        cardBox_2.grid(row=1, column=0)
        cardBox_3.grid(row=2, column=0)
        cardBox_4.grid(row=3, column=0)
        cardBox_5.grid(row=4, column=0)
