import tkinter
import customtkinter
from PIL import Image

class MyFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

         # container
        self.container = customtkinter.CTkFrame(self, bg_color="white", width=825,
                                height=189, border_color="#D9D9D9", border_width=1, fg_color="white")
        self.container.grid(row=0, column=0)


        # logo - image
        logo_image = customtkinter.CTkImage(light_image=Image.open(
            "assets\dashboard__container\logo_container.png"), size=(75, 100))
        self.logo_label = customtkinter.CTkLabel(self, text="", image=logo_image, fg_color="white")
        self.logo_label.grid(row=0, column=0, sticky=customtkinter.NW,padx=15, pady=37)

        
        # title - container
        animal_title = customtkinter.CTkLabel(self, text="Nome do animal", font=customtkinter.CTkFont(
            family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#292929")
        animal_title.grid(row=0, column=0, sticky=customtkinter.NW,padx=114, pady=36)
        
         # subtitle - container
        owner_title = customtkinter.CTkLabel(self, text="Dono:", font=customtkinter.CTkFont(
            family="Open Sans", size=14, weight="bold"), fg_color="white", text_color="#6A6A6A")
        owner_title.grid(row=0, column=0, sticky=customtkinter.NW,padx=114, pady=60)

        owner_title_placeholder = customtkinter.CTkLabel(self, text="Lorem Ipsum", font=customtkinter.CTkFont(
            family="Open Sans", size=14), fg_color="white", text_color="#6A6A6A")
        owner_title_placeholder.grid(row=0, column=0, sticky=customtkinter.NW,padx=157, pady=60)

        contact_title = customtkinter.CTkLabel(self, text="Contato:", font=customtkinter.CTkFont(
            family="Open Sans", size=14, weight="bold"), fg_color="white", text_color="#6A6A6A")
        contact_title.grid(row=0, column=0, sticky=customtkinter.NW,padx=114, pady=79)

        
        contact_title_placeholder = customtkinter.CTkLabel(self, text="(13) 9684-4814", font=customtkinter.CTkFont(
            family="Open Sans", size=14), fg_color="white", text_color="#6A6A6A")
        contact_title_placeholder.grid(row=0, column=0, sticky=customtkinter.NW,padx=175, pady=79)

        
        date_icon=customtkinter.CTkImage(light_image=Image.open(
            "assets\dashboard__container\calendar.png"), size=(16, 16))
        date_label = customtkinter.CTkLabel(self, text="", image=date_icon, fg_color="white")
        date_label.grid(row=0, column=0, sticky=customtkinter.SW,padx=114, pady=47)

        
        date_text = customtkinter.CTkLabel(self, text="14/04/2023", font=customtkinter.CTkFont(
            family="Open Sans", size=14, weight="bold"), fg_color="white", text_color="#292929")
        date_text.grid(row=0, column=0, sticky=customtkinter.SW,padx=133, pady=47)

        clock_icon = customtkinter.CTkImage(light_image=Image.open(
            "assets\dashboard__container\clock.png"), size=(16, 16))
        clock_label = customtkinter.CTkLabel(self, text="", image=clock_icon, fg_color="white")
        clock_label.grid(row=0, column=0, sticky=customtkinter.SW,padx=230, pady=47)

          
        clock_text = customtkinter.CTkLabel(self, text="14h00", font=customtkinter.CTkFont(
            family="Open Sans", size=14, weight="bold"), fg_color="white", text_color="#292929")
        clock_text.grid(row=0, column=0, sticky=customtkinter.SW,padx=251, pady=47)

        
        # status - container
        status_bar = customtkinter.CTkFrame(self, bg_color="#F2994A",  fg_color="#F2994A", width=71, height=2)
        status_bar.grid(row=0, column=0, sticky=customtkinter.SW,padx=15, pady=26.5)

        
        # in progress - status - container
        in_progress_text = customtkinter.CTkLabel(self, text="Em andamento", font=customtkinter.CTkFont(
            family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#F2994A")
        in_progress_text.grid(row=0, column=0, sticky=customtkinter.SW,padx=95, pady=14)

        # division - container
        division = customtkinter.CTkFrame(self, bg_color="white", width=3,
                                height=109,  fg_color="#DCDCDC")
        division.grid(row=0, column=0, sticky=customtkinter.NW,padx=319, pady=36)

           # animal_info- container
        description_title = customtkinter.CTkLabel(self, text="Descrição: ", font=customtkinter.CTkFont(
            family="Open Sans", size=16, weight="bold"), fg_color="white", text_color="#717171")
        description_title.grid(row=0, column=0, sticky=customtkinter.NW,padx=339, pady=36)

         # animal_description - container
        description_information_1 = customtkinter.CTkLabel(self, text="Procedimento feito Lorem ipsum dolor sit amet, consectetur adipiscing", font=customtkinter.CTkFont(
            family="Open Sans", size=14), fg_color="white", text_color="#717171")
        description_information_1.grid(row=0, column=0, sticky=customtkinter.S,padx=200, pady=56)

       


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.my_frame = MyFrame(master=self, width=825, height=210)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20)


app = App()
app.mainloop()