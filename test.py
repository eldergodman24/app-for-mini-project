import time
import tkinter
import tkinter as tk
from tkinter import *
import customtkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root=customtkinter.CTk()
root.geometry("1080x980")
def slider_event(value):
    print(value)
slider = customtkinter.CTkSlider(master=root, from_=0, to=100, command=slider_event)
slider.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
def login():
    global frame
    user_name=StringVar()
    frame=customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both",expand=True)

    label=customtkinter.CTkLabel(master=frame, text="Login System")
    label.pack(pady=12,padx=10)
    ulabel = customtkinter.CTkLabel(frame, text="Username",text_color="white", fg_color='transparent')
    ulabel.pack(pady=50,padx=50)
    ulabel.place(relx=0.35,rely=0.08)
    entry1 = customtkinter.CTkEntry(master=frame,textvariable=user_name, placeholder_text="Username")
    entry1.pack(pady=12,padx=10)
    plabel = customtkinter.CTkLabel(frame, text="Password",text_color="white", fg_color='transparent')
    plabel.pack(pady=50,padx=50)
    plabel.place(relx=0.35,rely=0.14)
    entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password",show="*")
    entry2.pack(pady=12,padx=10)

    button=customtkinter.CTkButton(master=frame, text="Login")
    button.pack(pady=12,padx=10)

    button2=customtkinter.CTkButton(master=frame,
                                   text="Signup",
                                   text_color="white",
                                   fg_color="transparent",
                                   hover_color= "red",
                                   command=lambda :sign_up())
    button2.pack(pady=10,padx=10)

def sign_up():
    frame.destroy()
    time.sleep(1)
    frame2=customtkinter.CTkFrame(master=root)
    frame2.pack(pady=20, padx=60, fill="both", expand=True)
    label=customtkinter.CTkLabel(master=frame2, text="Sign Up")
    label.pack(pady=12,padx=10)

    #button=customtkinter.CTkButton(master=frame2, text="SignUp")
    #button.pack(pady=12,padx=10)

login()
root.mainloop()