import tkinter
import customtkinter as ctk
from PIL import Image

root = ctk.CTk()  # create CTk window like you do with the Tk window
root.geometry("1280x720")
root.resizable(False, False)
root.config(background="#FFFFFF")

division = ctk.CTkFrame(root, bg_color="white", width=250,
                        height=1450,  fg_color="#E0E0E0")
division.place(relx=0, rely=0, anchor=tkinter.W)




#images
logo_image = ctk.CTkImage(light_image=Image.open("assets\\dog_logo.png"))
side_image = ctk.CTkImage(light_image=Image.open("assets\\side_line.png"))
dash_logo = ctk.CTkImage(light_image=Image.open("assets\\dashboard_logo_white.png"))
client_logo = ctk.CTkImage(light_image=Image.open("assets\\client_logo.png"))
services_logo = ctk.CTkImage(light_image=Image.open("assets\\services_logo.png"))
animals_logo = ctk.CTkImage(light_image=Image.open("assets\\animals_logo.png"))
exit_logo = ctk.CTkImage(light_image=Image.open("assets\\exit_logo.png"))

#labels
# logo_label = ctk.CTkLabel(frame, image=logo_image)
# side_line_label = ctk.CTkLabel(frame, image=side_image)
#title = ctk.CTkLabel(root, text="Sofisticão",font=ctk.CTkFont(family="Nunito", weight="bold", size=25))

#buttons
dash_button = ctk.CTkButton(root, text="Dashboard", image=dash_logo, fg_color="#27AE60",
                            corner_radius=5, height=35, width=180, bg_color="#F2F2F2")
client_button = ctk.CTkButton(root, text="       Clientes", text_color="black", image=client_logo, corner_radius=7, 
                              fg_color="white", height=35, width=180, bg_color="#E0E0E0")
services_button  = ctk.CTkButton(root, image=services_logo, text="      Serviços", text_color="black", corner_radius=7,
                                  fg_color="white", height=35, width=180, bg_color="#E0E0E0")
animals_button  = ctk.CTkButton(root, image=animals_logo, text="        Animais", text_color="black", corner_radius=7,
                                  fg_color="white", height=35, width=180, bg_color="#E0E0E0")
exit_button  = ctk.CTkButton(root, image=exit_logo, text="  Sair", text_color="black", corner_radius=7,
                                  fg_color="white", height=35, width=180, bg_color="#E0E0E0", compound="right")






#posicionamento na tela

# logo_label.place(x=60, y=20)
# side_line_label.place(x=15,y=300)
dash_button.place(x=40, y=300)
client_button.place(x=40, y=350)
services_button.place(x=40, y=400)
animals_button.place(x=40, y=450)
exit_button.place(x=40, y=600)




root.mainloop()