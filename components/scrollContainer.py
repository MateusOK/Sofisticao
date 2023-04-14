import tkinter
import customtkinter
from PIL import Image
from components.card import Card
from components.blueCard import BlueCard

class MyFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        cardBox = Card(master=self)
        cardBox2 = BlueCard(master=self)
        cardBox3 = Card(master=self)
        cardBox.grid(row=0, column=0)
        cardBox2.grid(row=1, column=0)
        cardBox3.grid(row=2, column=0)