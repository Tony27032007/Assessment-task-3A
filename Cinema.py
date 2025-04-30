import customtkinter as ctk
ctk.set_appearance_mode("system")
root = ctk.CTk()
root.geometry("1920x1080")
root.title("CineMax")
if ctk.get_appearance_mode() == "Light":
    ctk.set_default_color_theme("dark-blue")
    left_frame = ctk.CTkFrame(root, height=1080, width=360, fg_color="#08376B", bg_color="#08376B")
    root.iconbitmap("film_roll.ico")
else:
    ctk.set_default_color_theme("blue")
    root.iconbitmap("Untitled.ico")
    left_frame = ctk.CTkFrame(root, height=1080, width=360, fg_color="#2F90B0", bg_color="#2F90B0")

root.grid_columnconfigure(0, weight=1)


def clicked():
    l=ctk.CTkLabel(root, text="clicked")
    l.grid(row=1, column=0, padx=20, pady=20)

button = ctk.CTkButton(root, text="Click Me", command=clicked)
button.grid(row=0, column=0, padx=20, pady=20)
root.mainloop()

