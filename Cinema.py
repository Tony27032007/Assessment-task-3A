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
    l=ctk.CTkEntry(right_frame, placeholder_text="Email", width=260, height=50, corner_radius=25, font=("Arial",22))
    l.place(relx=0.5, rely=0.45, anchor="center")
    p=ctk.CTkEntry(right_frame, placeholder_text="Password", show="·" ,width=260, height=50, corner_radius=25, font=("Arial",22))
    p.place(relx=0.5, rely=0.55, anchor="center")


def clear_window(window):
    for child in window.winfo_children():
        child.destroy()
    
def login():
    def loginin():
        try:
            url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}"
            payload = {
                "email": l.get(),
                "password": p.get(),
                "returnSecureToken": True
            }
            response = requests.post(url, json=payload)
            data = response.json()
            if "idToken" in data:
                usremail = l.get()
                clear_window(root)
                from homes import home_page
                home_page(usremail)
            else:
                raise Exception(data.get("error", {}).get("message", "Unknown error"))
        except Exception as e:
            wrong = ctk.CTkLabel(right_frame, text="Wrong Username or Password", text_color="red", font=("Arial Rounded MT Bold",22))
            wrong.place(relx=0.5, rely=0.85, anchor="center")
                
    
    global button1, button2
    button1.destroy()
    button2.destroy()
    global button3 , l, p
    global x
    x=0.75
    def forgotpass():
        clear_window(right_frame)
        email_entry = ctk.CTkEntry(
            right_frame, placeholder_text="Enter Email", width=260, height=50, corner_radius=25, font=("Arial",22)
        )
        email_entry.place(relx=0.5, rely=0.45, anchor="center")

        def send_reset():
            try:
                url = f"https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key={FIREBASE_API_KEY}"
                payload = {
                    "requestType": "PASSWORD_RESET",
                    "email": email_entry.get()
                }
                response = requests.post(url, json=payload)
                data = response.json()
                if "email" in data:
                    msg = ctk.CTkLabel(
                        right_frame, text="Check your email for the reset link.", text_color="green", font=("Arial Rounded MT Bold", 18)
                    )
                    msg.place(relx=0.5, rely=0.65, anchor="center")
                    right_frame.after(3000)
                    clear_window(right_frame)
                    render_auth(45,55)
                else:
                    raise Exception(data.get("error", {}).get("message", "Unknown error"))
            except Exception as e:
                msg = ctk.CTkLabel(
                    right_frame, text="Failed to send reset email.", text_color="red", font=("Arial Rounded MT Bold",18)
                )
                msg.place(relx=0.5, rely=0.65, anchor="center")

        reset_btn = ctk.CTkButton(
            right_frame, text="Send Reset Email", command=send_reset, corner_radius=25, width=260, height=50, font=("Arial Rounded MT Bold",22)
        )
        reset_btn.place(relx=0.5, rely=0.55, anchor="center")

    y=0.45
    
    button3 = ctk.CTkButton(right_frame, text="Login", bg_color="transparent" ,command=loginin, corner_radius=25, width=260, height=50, font=("Arial Rounded MT Bold",22))
    button3.place(rely=y, relx=0.5, anchor="center")
    
    while y<0.65:
        y=y+0.0065
        button3.place_configure(rely=y)
        root.update_idletasks()
        root.after(1)
    create_text()
    rsp = ctk.CTkButton(right_frame, text="Forgot Password?", bg_color="transparent" ,command=forgotpass, corner_radius=25, width=260, height=50, font=("Arial Rounded MT Bold",22))
    rsp.place(rely=x, relx=0.5, anchor="center")
def signup():
    def signingup():
        try:
            url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={FIREBASE_API_KEY}"
            payload = {
                "email": l.get(),
                "password": p.get(),
                "returnSecureToken": True
            }
            response = requests.post(url, json=payload)
            data = response.json()
            if "idToken" in data:
                usremail = l.get()
                
                user = auth.get_user_by_email(usremail)
                uid = user.uid

                
                db.collection("customer").document(uid).set({
                    "email": usremail,
                    "firstname": "Provide First Name",
                    "lastname": "Provide Last Name",
                    "phone": "Provide Phone Number",
                    "ticID": None
                })

                clear_window(root)
                from homes import home_page
                home_page(usremail)
            else:
                raise Exception(data.get("error", {}).get("message", "Unknown error"))
        except Exception as e:
            wrong = ctk.CTkLabel(
                right_frame,
                text="Sign Up failed.",
                text_color="red",
                font=("Arial Rounded MT Bold", 18)
            )
            wrong.place(relx=0.5, rely=0.85, anchor="center")


    
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
    button1.place(rely=float(a)/100, relx=0.5, anchor="center")
    button2 = ctk.CTkButton(right_frame, text="Sign Up", bg_color="transparent" ,command=signup, corner_radius=25,width=260,border_color="#3987f5", border_width=4, fg_color="transparent", height=50, font=("Arial Rounded MT",22))
    button2.place(rely=float(b)/100, relx=0.5, anchor="center")



render_auth(45,55)
root.mainloop()

