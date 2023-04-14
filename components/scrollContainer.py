import tkinter
import customtkinter
from PIL import Image
from card import Card

class MyFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        teste = Card(self)
        teste2 = Card(self)
        teste.grid(row=0, column=0)
        teste2.grid(row=1, column=0)

 

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.my_frame = MyFrame(master=self, width=825, height=210)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20)
app = App()
app.mainloop()