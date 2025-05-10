import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("system")
if ctk.get_appearance_mode() == "Light":
    ctk.set_default_color_theme("dark-blue")
    root = ctk.CTk(fg_color="white")
    root.iconbitmap("film_roll.ico")
else:
    ctk.set_default_color_theme("blue")
    root = ctk.CTk(fg_color="black")
    root.iconbitmap("Untitled.ico") 
root.geometry("1920x1080")
root.title("CineMax")
root.resizable(True, True)