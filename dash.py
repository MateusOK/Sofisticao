from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = Tk()

root.title("Dashboard - Sofisticão")

root.config(background="#FFFFFF")


# window size
root.resizable(False, False)
root.maxsize(width=1280, height=720)
root.minsize(width=1280, height=720)

frame = Frame(root)
frame.pack(fill=BOTH, expand=True)


#images
logo_image = PhotoImage(file="assets\\dog_logo.png")
side_image = PhotoImage(file="assets\\side_line.png")
dash_logo = PhotoImage(file="assets\\dashboard_logo.png")

#labels
logo_label = Label(frame, image=logo_image)
side_line_label = Label(frame, image=side_image)
title = ttk.Label(frame, text="Sofisticão", font="Nunito 25 bold", bootstyle="success")

#buttons
dash_button = Button(frame, text="Dashboard", font="OpenSans 16 bold", fg="#FFFFFF", image=dash_logo, compound=LEFT)




#posicionamento na tela
logo_label.place(x=60, y=20)
title.place(x=40, y=180)
side_line_label.place(x=20,y=300)
dash_button.pack()



root.mainloop()