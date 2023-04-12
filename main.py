import tkinter
import customtkinter as ctk
from PIL import Image
from tkinter import PhotoImage


root = ctk.CTk()  # create CTk window like you do with the Tk window
root.geometry("1280x720")
root.resizable(False, False)
root.config(background="#FFFFFF")


# Carregue as imagens
logo = ctk.CTkImage(light_image=Image.open("assets\\dog_logo_login.png"), size=(250,250))
left_image = PhotoImage(file="assets\\leftImage.png")
right_image = PhotoImage(file="assets\\rightImage.png")



# # Crie rótulos para exibir as imagens
logo_label = ctk.CTkLabel(root, text="", image=logo, bg_color="white")
left_label = ctk.CTkLabel(root, text="", image=left_image, bg_color="white")
right_label = ctk.CTkLabel(root, text="", image=right_image, bg_color="white")
email_input = ctk.CTkEntry(root, bg_color="white", fg_color="white", placeholder_text="Email", text_color="black", width=250, height=30)
email_text = ctk.CTkLabel(root, text="Email", bg_color="white", text_color="#F2800D", font=ctk.CTkFont(family="Nunito", size=12, weight="bold"))
password_input = ctk.CTkEntry(root, placeholder_text="Senha", show="*", fg_color="white", bg_color="white", text_color="black", width=250, height=30)
password_text = ctk.CTkLabel(root, text="Senha", bg_color="white", text_color="#F2800D", font=ctk.CTkFont(family="Nunito", size=12, weight="bold"))
check = ctk.CTkCheckBox(root, text="Continuar conectado" , bg_color="white", fg_color="#F2800D", text_color="black", 
                        border_color="#F2800D", hover_color="#F2800D", checkbox_height=20, checkbox_width=20, 
                        font=ctk.CTkFont(family="Nunito", size=12))
senha_esquece = ctk.CTkLabel(root, text="Esqueci minha senha", font=ctk.CTkFont(family="Nunito", size=10), bg_color="white", text_color="black")
# entrar_button = ttk.Button(frame, text="Entrar", bootstyle=SUCCESS, width=52)

# Crie um rótulo para o texto

#Posicionamento da e laterais
logo_label.place(x=520, y=100)
left_label.grid(row=0, column=0)
right_label.place(x=1050,y=0)

#Posicionamento dos inputs
email_input.place(x=520, y=400)
password_input.place(x=520, y=470)

#Posicionamento dos texts
email_text.place(x=522, y=370)
password_text.place(x=522, y=440)
check.place(x=520, y=510)
senha_esquece.place(x=650, y=505)

root.mainloop()
