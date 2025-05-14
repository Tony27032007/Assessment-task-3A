import customtkinter as ctk
from root import root
from PIL import Image
from gg import *
import qrcode
from datetime import *
from zoneinfo import *
def home_page(usremail):
    tabview = ctk.CTkTabview(root, height=1080, width=1920, fg_color="transparent", bg_color="transparent", corner_radius=25)
    tabview.place(anchor="n", relx=0.5, rely=0.01)
    tabview._segmented_button.grid_remove()
    home = tabview.add("home")
    buy = tabview.add("buy")
    myaccount = tabview.add("myaccount")
    tabview.set("home")            
    logohome = ctk.CTkLabel(root, text="", image=ctk.CTkImage(light_image=Image.open("film roll.png"), dark_image=Image.open("Untitled.png"),size=(90, 90)))            
    logohome.place(relx=0.075, rely=0.04, anchor="center")
    upper_frame = ctk.CTkFrame(root, height=80, width=1280, fg_color="#08376B", bg_color="transparent", corner_radius=30)
    upper_frame.place(anchor="n", relx=0.5, rely=0.01, relwidth=0.7)
    
    def update_buttons(tab_name):
        tabview.set(tab_name)
        home_button.configure(fg_color="#08376B", text_color="#FFFFFF", hover=True)
        buy_button.configure(fg_color="#08376B", text_color="#FFFFFF", hover=True)
        myaccount_button.configure(fg_color="#08376B", text_color="#FFFFFF", hover=True)
              
        if tab_name == "home":
            home_button.configure(fg_color="#FFFFFF", text_color="#08376B", hover=False)
        elif tab_name == "buy":
            buy_button.configure(fg_color="#FFFFFF", text_color="#08376B", hover=False)
        elif tab_name == "myaccount":
            myaccount_button.configure(fg_color="#FFFFFF", text_color="#08376B", hover=False)

    global home_button, buy_button, myaccount_button

    home_button = ctk.CTkButton(upper_frame, fg_color="#FFFFFF" , text="Home", text_color="#08376B", corner_radius=25, width=260, height=50, font=("Arial Rounded MT Bold",22), hover=False, command= lambda: update_buttons("home"))
    home_button.place(relx=0.2, rely=0.5, anchor="center")
    buy_button = ctk.CTkButton(upper_frame, fg_color="#08376B", text="Ticket", text_color="#FFFFFF", corner_radius=25, width=260, height=50, font=("Arial Rounded MT Bold",22), hover=True, command= lambda: update_buttons("buy"))
    buy_button.place(relx=0.5, rely=0.5, anchor="center")
    myaccount_button = ctk.CTkButton(upper_frame, fg_color="#08376B", text="My Account", text_color="#FFFFFF", corner_radius=25, width=260, height=50, font=("Arial Rounded MT Bold",22), hover=True, command= lambda: update_buttons("myaccount"))
    myaccount_button.place(relx=0.8, rely=0.5, anchor="center")
    global home_frame, buy_frame, myaccount_frame

    home_frame = ctk.CTkScrollableFrame(home, fg_color="transparent", bg_color="transparent", width=1920, height=1000)
    home_frame._scrollbar.grid_remove()
    home_frame.place(anchor="s", relx=0.5, rely=1, relwidth=1, relheight=0.98)
    class NowShowing(ctk.CTkScrollableFrame):
        def filmframe(self,parent,text1,n):
            self.label = ctk.CTkLabel(parent, text=text1, text_color="#08376B", font=("Arial Rounded MT Bold",27), justify="left")
            self.label.pack(side="top", expand=True, pady=30, anchor="w")
            self._frame = ctk.CTkScrollableFrame(parent, fg_color="transparent", bg_color="transparent", width=1920, height=350, orientation="horizontal")
            self._frame._scrollbar.grid_remove()
            self._frame.pack(side="top", fill="x", expand=False)
            for i in range(n,n+10):
                thelogo = ctk.CTkImage(Image.open("filmp/Film_"+str(i) + ".jpg"), size=(200, 300))
                thelogo2 = ctk.CTkImage(Image.open("filmp/Film_"+str(i) + ".jpg"), size=(300, 300))
                logohome = ctk.CTkButton(self._frame, text="", image=thelogo, fg_color="transparent", bg_color="transparent", hover=False, width=200, height=300, command=lambda i=i: self.film_details(i))
                logohome.pack(side="left", expand=True, fill="both", padx=20, anchor="w")
                # Define hover effects
                def on_enter(event, button=logohome, thelogo2=thelogo2):
                    button.configure(width=400, height=600, image=thelogo2)  # Increase size

                def on_leave(event, button=logohome, thelogo=thelogo):
                    button.configure(width=200, height=300, image=thelogo)  # Reset size

                # Bind hover events
                logohome.bind("<Enter>", on_enter)
                logohome.bind("<Leave>", on_leave)

    NowShowing.filmframe(NowShowing, home_frame, "Now Showing", 1)
    NowShowing.filmframe(NowShowing, home_frame, "Coming Soon", 11)
    NowShowing.filmframe(NowShowing, home_frame, "Top Rated", 21)
    NowShowing.filmframe(NowShowing, home_frame, "Most Popular", 31)
        
    ursid = auth.get_user_by_email(usremail)
        
    buy_frame = ctk.CTkFrame(buy, fg_color="transparent", bg_color="transparent", width=1920, height=1000)
    buy_frame.place(anchor="s", relx=0.5, rely=1, relwidth=1, relheight=0.98)

    
    user_doc = db.collection("customer").document(ursid.uid).get()
    user_data = user_doc.to_dict() if user_doc.exists else {}
    tic_id = user_data.get("ticID")

    if tic_id:
        ticket_doc = tic_id.get()
        if ticket_doc.exists:
            ticket = ticket_doc.to_dict()
            moviename_ref = ticket.get("screenID", None)
            if moviename_ref:
                moviename_doc = moviename_ref.get()
                moviename_data = moviename_doc.to_dict() if moviename_doc.exists else {}
                namemovie_ref = moviename_data.get("movieID", None)
                screen = moviename_data.get("screen", "Unknown")
                date_time = moviename_data.get("date-time", "Unknown").astimezone(ZoneInfo("Australia/Melbourne")).strftime("%Y-%m-%d %H:%M")
                if namemovie_ref:
                    namemovie_doc = namemovie_ref.get()
                    namemovie_data = namemovie_doc.to_dict() if namemovie_doc.exists else {}
                    movie = namemovie_data.get("name", "Unknown")
                else:
                    movie = "Unknown"
            else:
                movie = "Unknown"
                screen = "Unknown"
                date_time = "Unknown"
            seatnumber = ticket.get("seatnum", "Unknown")

            ticket_info = f"Movie: {movie}\nScreen: {screen}\nDate-Time: {date_time}\nSeat: {seatnumber}"
            ticket_label = ctk.CTkLabel(buy_frame, text=ticket_info, text_color="#08376B", font=("Arial Rounded MT Bold", 22), justify="left")
            ticket_label.place(relx=0.4, rely=0.3, anchor="center")

            # Generate QR code for ticID
            qr = qrcode.QRCode(box_size=6, border=2, error_correction=qrcode.constants.ERROR_CORRECT_H)
            qr.add_data(tic_id.id)
            qr.make(fit=True)
            qr_img = qr.make_image(fill_color="#08376B", back_color="white")
            qr_img = qr_img.resize((180, 180))
            from PIL import ImageTk
            qr_img_tk = ImageTk.PhotoImage(qr_img)

            qr_label = ctk.CTkLabel(buy_frame, text="", image=qr_img_tk)
            qr_label.image = qr_img_tk  # Keep a reference!
            qr_label.place(relx=0.7, rely=0.3, anchor="center")
        else:
            ticket_label = ctk.CTkLabel(buy_frame, text="No ticket info found.", text_color="red", font=("Arial Rounded MT Bold", 20))
            ticket_label.place(relx=0.5, rely=0.3, anchor="center")
    else:
        ticket_label = ctk.CTkLabel(buy_frame, text="No ticket purchased.", text_color="#909090", font=("Arial Rounded MT Bold", 20))
        ticket_label.place(relx=0.5, rely=0.3, anchor="center")

    myaccount_frame = ctk.CTkFrame(myaccount, fg_color="transparent", bg_color="transparent", width=1920, height=1000)
    myaccount_frame.place(anchor="s", relx=0.5, rely=1, relwidth=1, relheight=0.98) 

   
    ursid = auth.get_user_by_email(usremail)
    hiuser = ctk.CTkLabel(myaccount_frame, text="Hi " + usremail, text_color="#FFFFFF", fg_color="#08376B" , font=("Arial Rounded MT Bold",27), justify="left", width=300, height=50, corner_radius=25)
    hiuser.place(relx=0.5, rely=0.1, anchor="center")
    user_doc = db.collection("customer").document(ursid.uid).get()
    user_data = user_doc.to_dict() if user_doc.exists else {"create_user": "False"}

    first_name = user_data.get("firstname", "")
    last_name = user_data.get("lastname", "")
    phone = ursid.phone_number or user_data.get("phone", "")

    fname_entry = ctk.CTkEntry(myaccount_frame, placeholder_text="First Name", width=300, height=50, corner_radius=25, font=("Arial Rounded MT Bold",25))
    fname_entry.insert(0, first_name)
    fname_entry.configure(state="disabled", fg_color="#909090")
    fname_entry.place(relx=0.5, rely=0.2, anchor="center")

    lname_entry = ctk.CTkEntry(myaccount_frame, placeholder_text="Last Name", width=300, height=50, corner_radius=25, font=("Arial Rounded MT Bold",25))
    lname_entry.insert(0, last_name)
    lname_entry.configure(state="disabled", fg_color="#909090")
    lname_entry.place(relx=0.5, rely=0.3, anchor="center")

    phone_entry = ctk.CTkEntry(myaccount_frame, placeholder_text="Phone Number", width=300, height=50, corner_radius=25, font=("Arial Rounded MT Bold",25))
    phone_entry.insert(0, phone)
    phone_entry.configure(state="disabled", fg_color="#909090")
    phone_entry.place(relx=0.5, rely=0.4, anchor="center")

    def enable_edit():
        fname_entry.configure(state="normal", fg_color="#FFFFFF")
        lname_entry.configure(state="normal", fg_color="#FFFFFF")
        phone_entry.configure(state="normal", fg_color="#FFFFFF")
        save_btn.configure(state="normal", fg_color="#1F6AA5")
        update_btn.configure(state="disabled", fg_color="#909090")

    def save_details():
        new_fname = fname_entry.get()
        new_lname = lname_entry.get()
        new_phone = phone_entry.get()

        db.collection("customer").document(ursid.uid).set({
            "firstname": new_fname,
            "lastname": new_lname,
            "phone": int(new_phone)
        }, merge=True)
        try:
            auth.update_user(ursid.uid, phone_number=new_phone if new_phone else None)
        except Exception:
            pass
        
        fname_entry.configure(state="disabled", fg_color="#909090")
        lname_entry.configure(state="disabled", fg_color="#909090")
        phone_entry.configure(state="disabled", fg_color="#909090")
        save_btn.configure(state="disabled", fg_color="#909090")
        update_btn.configure(state="normal", fg_color="#1F6AA5")

    update_btn = ctk.CTkButton(myaccount_frame, text="Update Details", command=enable_edit, corner_radius=25, width=200, height=50, fg_color="#1F6AA5", text_color="#FFFFFF", font=("Arial",20))
    update_btn.place(relx=0.4, rely=0.5, anchor="center")

    save_btn = ctk.CTkButton(myaccount_frame, text="Save", command=save_details, corner_radius=25, width=200, state="disabled", height=50, fg_color="#909090", font=("Arial",20))
    save_btn.place(relx=0.6, rely=0.5, anchor="center")
home_page("tony2732007@gmail.com")
root.mainloop()