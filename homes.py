import customtkinter as ctk
from root import root
from PIL import Image
import urllib.request
import io
import base64
class home(ctk.CTkFrame):
    def home_page():
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
            


            
        buy_frame = ctk.CTkScrollableFrame(buy, fg_color="transparent", bg_color="transparent", width=1920, height=1000)
        buy_frame._scrollbar.grid_remove()
        buy_frame.place(anchor="s", relx=0.5, rely=1, relwidth=1, relheight=0.98)
        myaccount_frame = ctk.CTkScrollableFrame(myaccount, fg_color="transparent", bg_color="transparent", width=1920, height=1000)
        myaccount_frame._scrollbar.grid_remove()
        myaccount_frame.place(anchor="s", relx=0.5, rely=1, relwidth=1, relheight=0.98)     
home.home_page()
root.mainloop()