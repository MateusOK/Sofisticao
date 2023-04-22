from tkinter import *
import customtkinter
from PIL import Image
from components.animalCard import AnimalCard


class AnimalScroll(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        cardBox = AnimalCard(master=self)
        cardBox2 = AnimalCard(master=self)
        cardBox3 = AnimalCard(master=self)
        cardBox4 = AnimalCard(master=self)
        cardBox5 = AnimalCard(master=self)
        cardBox.grid(row=0, column=0, pady=5)
        cardBox2.grid(row=1, column=0, pady=5)
        cardBox3.grid(row=2, column=0, pady=5)
        cardBox4.grid(row=3, column=0, pady=5)
        cardBox5.grid(row=4, column=0, pady=5)
