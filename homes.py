import customtkinter as ctk
from root import root
from PIL import Image, ImageTk
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
    global home_frame, tic_frame, myaccount_frame

    home_frame = ctk.CTkScrollableFrame(home, fg_color="transparent", bg_color="transparent", width=1920, height=1000)
    home_frame._scrollbar.grid_remove()
    home_frame.place(anchor="s", relx=0.5, rely=1, relwidth=1, relheight=0.98)
    class NowShowing(ctk.CTkScrollableFrame):
        def __init__(self, parent):
            super().__init__(parent)
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
        def film_details(self, i):
            global movie_doc
            movie_doc =  db.collection("Movie").where("posfile", "==", "Film_" + str(i) + ".jpg").get()
            if movie_doc:
                movie_doc = movie_doc[0] 
                movie_data = movie_doc.to_dict()
                def buy_ticket(movie_data):
                    
                    theater_window = ctk.CTkToplevel(root)
                    theater_window.title(f"Select Seats - {movie_data.get('name')}")
                    theater_window.geometry("800x600")
                    theater_window.configure(fg_color="#2b2b2b")
                    theater_window.resizable(False, False)
                    
                    
                    screen_frame = ctk.CTkFrame(theater_window, fg_color="white", height=40, width=600, corner_radius=10)
                    screen_frame.place(relx=0.5, rely=0.05, anchor="center")
                    
                    screen_label = ctk.CTkLabel(screen_frame, text="SCREEN", text_color="black", font=("Arial Bold", 16))
                    screen_label.place(relx=0.5, rely=0.5, anchor="center")
                    
                    
                    content_frame = ctk.CTkFrame(theater_window, fg_color="transparent")
                    content_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.7)
                    
                    
                    
                    selected_seats = []
                    
                    
                    def toggle_seat(row, seat, button):
                        seat_id = f"{row}{seat}"
                        if seat_id in selected_seats:
                            selected_seats.remove(seat_id)
                            button.configure(fg_color="#909090")  
                        else:
                            selected_seats.append(seat_id)
                            button.configure(fg_color="#34C759")  
                        
                        
                        total = len(selected_seats) * 15.00
                        price_label.configure(text="Total: $" + str(total), font=("Arial Rounded BT Bold", 16), text_color="#FFFFFF")
                        
                        
                        if selected_seats:
                            confirm_button.configure(state="normal", fg_color="#1F6AA5")
                        else:
                            confirm_button.configure(state="disabled", fg_color="#909090")
                    
                    rows = 5  
                    seats_per_row = 8 
                    seat_buttons = {}

                    content_frame.columnconfigure(0, weight=1)  
                    for i in range(1, seats_per_row + 1):
                        content_frame.columnconfigure(i, weight=0) 
                    content_frame.columnconfigure(seats_per_row + 1, weight=1)  
                    seatnumbering=1
                    for row in range(1, rows + 1):
                    
                        for seat in range(1, seats_per_row + 1):
                            seat_button = ctk.CTkButton(content_frame, text=str(seatnumbering), width=40, height=30, fg_color="#3987f5", hover_color=("#FFFFFF","#000000"), corner_radius=5, command=lambda r=row, s=seat, b=None: toggle_seat(r, s, seat_buttons[(r,s)]))
                            seat_button.grid(row=row, column=seat, padx=10, pady=10)
                            seat_buttons[(row, seat)] = seat_button
                            seatnumbering=seatnumbering+1
                    
                    
                    empty_label = ctk.CTkLabel(content_frame, text="")
                    empty_label.grid(row=1, column=seats_per_row + 1)
                    
                    price_label = ctk.CTkLabel(theater_window, text="Total: $0.00", font=("Arial Bold", 16))
                    price_label.place(relx=0.5, rely=0.85, anchor="center")
                    
                    
                    def confirm_seats():
                        if not selected_seats:
                            return
                        
                        
                        payment_window = ctk.CTkToplevel(root)
                        payment_window.title("Payment Information")
                        payment_window.geometry("500x450")
                        payment_window.configure(fg_color="#2b2b2b")
                        payment_window.resizable(False, False)
                        payment_window.grab_set()  
                        
                        
                        header_frame = ctk.CTkFrame(payment_window, fg_color="#08376B", height=70)
                        header_frame.pack(fill="x", pady=(0, 20))
                        
                        header_label = ctk.CTkLabel(
                            header_frame,
                            text=f"{movie_data.get('name')}",
                            font=("Arial Bold", 18),
                            text_color="white"
                        )
                        header_label.place(relx=0.5, rely=0.5, anchor="center")
                        
                        
                        form_frame = ctk.CTkFrame(payment_window, fg_color="transparent")
                        form_frame.pack(fill="both", expand=True, padx=30, pady=10)
                        
                        
                        ctk.CTkLabel(form_frame, text="Card Number", font=("Arial", 14)).pack(anchor="w", pady=(10, 5))
                        card_number = ctk.CTkEntry(
                            form_frame, 
                            placeholder_text="XXXX XXXX XXXX XXXX",
                            width=400, 
                            height=40,
                            font=("Arial", 14)
                        )
                        card_number.pack(fill="x", pady=(0, 15))
                        
                        
                        card_details_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
                        card_details_frame.pack(fill="x", pady=(0, 15))
                        
                        
                        exp_frame = ctk.CTkFrame(card_details_frame, fg_color="transparent")
                        exp_frame.pack(side="left", fill="x", expand=True, padx=(0, 5))
                        
                        ctk.CTkLabel(exp_frame, text="Expiry Date (MM/YY)", font=("Arial", 14)).pack(anchor="w", pady=(0, 5))
                        expiry_date = ctk.CTkEntry(
                            exp_frame,
                            placeholder_text="MM/YY",
                            width=180,
                            height=40,
                            font=("Arial", 14)
                        )
                        expiry_date.pack(fill="x")
                        
                        
                        cvv_frame = ctk.CTkFrame(card_details_frame, fg_color="transparent")
                        cvv_frame.pack(side="right", fill="x", expand=True, padx=(5, 0))
                        
                        ctk.CTkLabel(cvv_frame, text="CVV", font=("Arial", 14)).pack(anchor="w", pady=(0, 5))
                        cvv = ctk.CTkEntry(
                            cvv_frame,
                            placeholder_text="123",
                            width=180,
                            height=40,
                            font=("Arial", 14),
                            show="•"
                        )
                        cvv.pack(fill="x")
                        
                        # Error message label
                        error_label = ctk.CTkLabel(
                            form_frame,
                            text="",
                            font=("Arial", 14),
                            text_color="#FF5555"
                        )
                        error_label.pack(pady=(10, 10))
                        
                        def process_payment():
                            
                            if len(card_number.get().replace(" ", "")) < 16:
                                error_label.configure(text="Please enter a valid card number")
                                return
                                
                            if not expiry_date.get() or len(expiry_date.get()) < 4:
                                error_label.configure(text="Please enter a valid expiry date")
                                return
                                
                            if not cvv.get() or len(cvv.get()) < 3:
                                error_label.configure(text="Please enter a valid CVV")
                                return
                            
                           
                            payment_window.destroy()
                            
                            
                            if i<=10:
                                scr = 1
                            elif i<=20:
                                scr = 2
                            elif i<=30:
                                scr = 3
                            else:
                                scr = 4

                            screen_ref = db.collection("screen").add({
                                "movieID": db.collection("Movie").document(movie_doc.id),
                                "screen": int(scr),
                                "date-time": datetime.now() + timedelta(days=1)  
                            })[1]  
                            
                            
                            seat_numbers = ", ".join(selected_seats)
                            ticket_ref = db.collection("tic").add({
                                "screenID": screen_ref,
                                "seatnum": int(seat_numbers),
                                "price": len(selected_seats) * 15.00
                            })[1]  
                            
                            
                            db.collection("customer").document(ursid.uid).update({
                                "ticID": ticket_ref
                            })
                            
                            
                            theater_window.destroy()
                            
                            
                            confirm_window = ctk.CTkToplevel(root)
                            confirm_window.title("Purchase Complete")
                            confirm_window.geometry("400x300")
                            
                            success_label = ctk.CTkLabel(
                                confirm_window,
                                text=f"Thank you for your purchase!\n\nMovie: {movie_data.get('name')}\nSeats: {seat_numbers}\nTotal: ${len(selected_seats) * 15.00:.2f}",
                                font=("Arial", 16)
                            )
                            success_label.pack(pady=20)
                            
                            ok_button = ctk.CTkButton(
                                confirm_window, 
                                text="View My Ticket",
                                command=lambda: [confirm_window.destroy(), update_buttons("buy"), ticket_info()],
                            )
                            ok_button.pack(pady=20)
                       
                        button_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
                        button_frame.pack(fill="x", pady=10)
                        
                        
                        pay_button = ctk.CTkButton(
                            button_frame,
                            text=f"Pay ${len(selected_seats) * 15.00:.2f}",
                            command=process_payment,
                            fg_color="#34C759",
                            hover_color="#2A9E48",
                            height=45,
                            corner_radius=25,
                            font=("Arial Bold", 16)
                        )
                        pay_button.pack(side="top", fill="x", pady=5)
                        
                        
                        cancel_button = ctk.CTkButton(
                            button_frame,
                            text="Cancel",
                            command=payment_window.destroy,
                            fg_color="#FF3B30",
                            hover_color="#D63129",
                            height=35,
                            corner_radius=25,
                            font=("Arial", 14)
                        )
                        cancel_button.pack(side="top", fill="x", pady=5)
                    confirm_button = ctk.CTkButton(theater_window, fg_color="white",text="Confirm Seats", text_color="#08376B", font=("Arial Rounded MT Bold", 16), width=200, height=40, corner_radius=10, command=confirm_seats)
                    confirm_button.configure(state="disabled")
                    confirm_button.place(relx=0.5, rely=0.9, anchor="center")
                def get_movie_description(movie_name):
                    api_key = "a9e02f57"  
                    url = f"http://www.omdbapi.com/?t={movie_name}&apikey={api_key}"
                    response = requests.get(url)
                    data = response.json()
                    if data.get("Response") == "True":
                        name = f"Title: {data.get('Title')}"
                        description = f"Description: {data.get('Plot')}"
                        release_date = f"Year: {data.get('Year')}"
                    else:
                        name = "Movie not found."
                        description = "Null"
                        release_date = "Null"

                    
                    details_window = ctk.CTkToplevel(root)
                    details_window.title(name)
                    details_window.geometry("600x400")
                    details_window.configure(resizeable=False, fg_color=("#FFFFFF", "#000000"), bg_color=("#FFFFFF", "#000000"))
                    
                    
                    details_label = ctk.CTkLabel(details_window, text=f"Name: {name}\nDescription: {description}\nRelease Date: {release_date}", text_color="#08376B", font=("SF Pro Rounded", 22), justify="left", wraplength=550)
                    details_label.pack(pady=20, fill="both")
                    buytic_btn = ctk.CTkButton(details_window, text="Buy Ticket→", command=lambda: buy_ticket(movie_data), fg_color="#1F6AA5", text_color="#FFFFFF", font=("Arial Rounded MT Bold", 20))
                    buytic_btn.pack(pady=10, padx=20, anchor="e")
                get_movie_description(movie_data.get("name"))

    
    now_showing = NowShowing(home_frame)
    now_showing.filmframe(home_frame, "Now Showing", 1)
    now_showing.filmframe(home_frame, "Coming Soon", 11)
    now_showing.filmframe(home_frame, "Top Rated", 21)
    now_showing.filmframe(home_frame, "Most Popular", 31)
        
    ursid = auth.get_user_by_email(usremail)
        
    tic_frame = ctk.CTkFrame(buy, fg_color="transparent", bg_color="transparent", width=1920, height=1000)
    tic_frame.place(anchor="s", relx=0.5, rely=1, relwidth=1, relheight=0.98)

    def ticket_info():
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
                ticket_label = ctk.CTkLabel(tic_frame, text=ticket_info, text_color="#08376B", font=("Arial Rounded MT Bold", 22), justify="left")
                ticket_label.place(relx=0.4, rely=0.3, anchor="center")

                # Generate QR code for ticID
                qr = qrcode.QRCode(box_size=6, border=2, error_correction=qrcode.constants.ERROR_CORRECT_H)
                qr.add_data(tic_id.id)
                qr.make(fit=True)
                qr_img = qr.make_image(fill_color="#08376B", back_color="white")
                qr_img = qr_img.resize((500, 500))
                
                qr_img_tk = ctk.CTkImage(qr_img, size=(400, 400))


                qr_label = ctk.CTkLabel(tic_frame, text="", image=qr_img_tk)
                qr_label.image = qr_img_tk  
                qr_label.place(relx=0.7, rely=0.3, anchor="center")
            else:
                ticket_label = ctk.CTkLabel(tic_frame, text="No ticket info found.", text_color="red", font=("Arial Rounded MT Bold", 20))
                ticket_label.place(relx=0.5, rely=0.3, anchor="center")
        else:
            ticket_label = ctk.CTkLabel(tic_frame, text="No ticket purchased.", text_color="#909090", font=("Arial Rounded MT Bold", 20))
            ticket_label.place(relx=0.5, rely=0.3, anchor="center")
    ticket_info()
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
# home_page("tonymasteri2703@gmail.com")
# root.mainloop()
# uncomment 2 lines above for testing purposes