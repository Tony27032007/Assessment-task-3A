from root import root
import customtkinter as ctk
from PIL import Image
import csv
from gg import *
root=root
right_frame = ctk.CTkFrame(root, height=1080, width=640, fg_color="#08376B", bg_color="#08376B")
right_frame.pack(side="right", expand=False, fill="y")
left_frame = ctk.CTkFrame(root, height=1080, width=1280, fg_color="transparent", bg_color="transparent")
left_frame.pack(side="left", expand=False, fill="y")
my_logo = ctk.CTkImage(light_image=Image.open("logo.png"), dark_image=Image.open("logo-dark.png"),size=(720, 720))
logo = ctk.CTkLabel(left_frame, text="", image=my_logo)
logo.place(relx=0.45, rely=0.5, anchor="center")

button1=button2=button3=None
def destroyB():
    global button1, button2, button3
    button1.destroy()
    button2.destroy()
    button3.destroy()

def create_text():
    global l, p
    l=ctk.CTkEntry(right_frame, placeholder_text="Username", width=260, height=50, corner_radius=25, font=("Arial",22))
    l.place(relx=0.5, rely=0.45, anchor="center")
    p=ctk.CTkEntry(right_frame, placeholder_text="Password", width=260, height=50, corner_radius=25, font=("Arial",22))
    p.place(relx=0.5, rely=0.55, anchor="center")


def clear_window(window):
    for child in window.winfo_children():
        child.destroy()
    
def login():
    def loginin():
        with open('customer_data.csv', mode ='r')as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                if lines[0] == l.get() and lines[1] == p.get():
                    clear_window(root)
                    from homes import homes
                    homes.home_page()
                    break
                else:
                    wrong = ctk.CTkLabel(right_frame, text="Wrong Username or Password", text_color="red", font=("Arial Rounded MT Bold",22))
                    wrong.place(relx=0.5, rely=0.85, anchor="center")
    
    global button1, button2
    button1.destroy()
    button2.destroy()
    global button3
    y=0.45
    button3 = ctk.CTkButton(right_frame, text="Login", bg_color="transparent" ,command=loginin, corner_radius=25, width=260, height=50, font=("Arial Rounded MT Bold",22))
    button3.place(rely=y, relx=0.5, anchor="center")
    
    while y<0.65:
        y=y+0.0065
        button3.place_configure(rely=y)
        root.update_idletasks()
        root.after(1)
    create_text()
def signup():
    def signingup():
        with open('customer_data.csv', mode ='r')as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                if lines[0] == l.get():
                    existed = ctk.CTkLabel(right_frame, text="Username already exists", text_color="red", font=("Arial Rounded MT Bold",22))
                    existed.place(relx=0.5, rely=0.85, anchor="center")
                    create_text()
                    global button3
                    try:
                        button3.destroy()
                    except Exception:
                        pass
                    button3 = ctk.CTkButton(right_frame, text="Sign Up", bg_color="transparent", command=signingup, corner_radius=25, width=260, height=50, font=("Arial Rounded MT Bold",22))
                    button3.place(rely=0.65, relx=0.5, anchor="center")
                    return
        with open('customer_data.csv', mode ='a')as file:
            csvFile = csv.writer(file)
            csvFile.writerow([l.get(), p.get()])
        clear_window(root)
        from homes import homes
        homes.home_page()
    
    global button1, button2, button3
    button1.destroy()
    button2.destroy()
    global button3
    button3 = ctk.CTkButton(right_frame, text="Sign Up", bg_color="transparent" ,command=signingup, corner_radius=25, width=260, height=50, font=("Arial Rounded MT Bold",22))
    button3.place(rely=0.55, relx=0.5, anchor="center")
    global y
    y=0.55
    while y<0.65:
        y=y+0.0065
        button3.place_configure(rely=y)
        root.update_idletasks()
        root.after(1)
    create_text()
def render_auth(a,b):
    global button1, button2
    button1 = ctk.CTkButton(right_frame, fg_color="#3987f5", text="Login", bg_color="transparent" ,command=login, corner_radius=25, width=260, height=50, font=("Arial Rounded MT Bold",22))
    button1.place(rely=0.45, relx=0.5, anchor="center")
    button2 = ctk.CTkButton(right_frame, text="Sign Up", bg_color="transparent" ,command=signup, corner_radius=25,width=260,border_color="#3987f5", border_width=4, fg_color="transparent", height=50, font=("Arial Rounded MT",22))
    button2.place(rely=0.55, relx=0.5, anchor="center")

#make 2 buttons login and sign up on top of each other

render_auth(45,55)
root.mainloop()

