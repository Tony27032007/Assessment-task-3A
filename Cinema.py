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
right_frame = ctk.CTkFrame(root, height=1080, width=640, fg_color="#08376B", bg_color="#08376B")
right_frame.pack(side="right", expand=False, fill="y")
left_frame = ctk.CTkFrame(root, height=1080, width=1280, fg_color="transparent", bg_color="transparent")
left_frame.pack(side="left", expand=False, fill="y")
my_logo = ctk.CTkImage(light_image=Image.open("logo.png"), dark_image=Image.open("logo-dark.png"),size=(720, 720))
logo = ctk.CTkLabel(left_frame, text="", image=my_logo)
logo.place(relx=0.45, rely=0.5, anchor="center")

button1=None
button2=None

def login():
    l=ctk.CTkEntry(right_frame, placeholder_text="Username", width=260, height=50, corner_radius=25, font=("Arial",22))
    l.place(relx=0.5, rely=0.45, anchor="center")
    p=ctk.CTkEntry(right_frame, placeholder_text="Password", width=260, height=50, corner_radius=25, font=("Arial",22))
    p.place(relx=0.5, rely=0.55, anchor="center")
    global button1, button2
    button1.destroy()
    button2.destroy()
    render_auth(70,None)
def signup():
    l=ctk.CTkEntry(right_frame, placeholder_text="Username", width=260, height=50, corner_radius=25, font=("Arial",22))
    l.place(relx=0.5, rely=0.5, anchor="center")
    p=ctk.CTkEntry(right_frame, placeholder_text="Password", width=260, height=50, corner_radius=25, font=("Arial",22))
    p.place(relx=0.5, rely=0.6, anchor="center")
    global button1, button2
    button1.destroy()
    button2.destroy()
    render_auth(None,70)

    
def render_auth(a,b):
    global button1, button2
    button1 = ctk.CTkButton(right_frame, fg_color="#3987f5", text="Login", bg_color="transparent" ,command=login, corner_radius=25, width=260, height=50, font=("Arial Rounded MT Bold",22))
    button1.place(rely=float(a)/100, relx=0.5, anchor="center")
    button2 = ctk.CTkButton(right_frame, text="Sign Up", bg_color="transparent" ,command=signup, corner_radius=25,width=260,border_color="#3987f5", border_width=4, fg_color="transparent", height=50, font=("Arial Rounded MT",22))
    button2.place(rely=float(b)/100, relx=0.5, anchor="center")
        

render_auth(45,55)


root.mainloop()

