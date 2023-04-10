import customtkinter
import tkinter as tk
from tkinter import *
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root=customtkinter.CTk()
root.geometry("1080x980")
radio_var=IntVar()
def radiobutton_event():
    print("radiobutton toggled, current value:", radio_var.get())

frame=customtkinter.CTkFrame(master=root,width=200,height=200)
frame.pack(pady=100)
label = customtkinter.CTkLabel(master=frame, text="Question")
label.pack()
radiobutton_1 = customtkinter.CTkRadioButton(master=root, text="Option 1",
                                             command=radiobutton_event, variable= radio_var, value=1)
radiobutton_2 = customtkinter.CTkRadioButton(master=root, text="Option 2",
                                             command=radiobutton_event, variable= radio_var, value=2)
radiobutton_3 = customtkinter.CTkRadioButton(master=root, text="Option 3",
                                             command=radiobutton_event, variable= radio_var, value=3)
radiobutton_4 = customtkinter.CTkRadioButton(master=root, text="Option 4",
                                             command=radiobutton_event, variable= radio_var, value=4)
button = customtkinter.CTkButton(master=root, text="Submit",command=lambda :print("Option", radio_var.get()))
radiobutton_1.pack(padx=20, pady=10)
radiobutton_2.pack(padx=20, pady=10)
radiobutton_3.pack(padx=20, pady=10)
radiobutton_4.pack(padx=20, pady=10)
button.pack(pady=12, padx=10)
root.mainloop()