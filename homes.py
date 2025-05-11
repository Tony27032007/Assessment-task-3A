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
            tabview._segmented_button.configure(fg_color="white" , bg_color="white" , text_color="white", corner_radius=0, width=0, height=0, font=("Arial",0), border_width=0)
            home = tabview.add("home")
            buy = tabview.add("buy")
            myaccount = tabview.add("myaccount")
            tabview.set("home")            
            thelogo = ctk.CTkImage(light_image=Image.open("film roll.png"), dark_image=Image.open("Untitled.png"),size=(120, 120))
            logohome = ctk.CTkLabel(root, text="", image=thelogo)            
            logohome.place(relx=0.075, rely=0.06, anchor="center")
            def update_buttons(tab_name):
                  tabview.set(tab_name)
                  home_button.configure(fg_color="#08376B", text_color="#FFFFFF")
                  buy_button.configure(fg_color="#08376B", text_color="#FFFFFF")
                  myaccount_button.configure(fg_color="#08376B", text_color="#FFFFFF")
                  
                  if tab_name == "home":
                      home_button.configure(fg_color="#FFFFFF", text_color="#08376B")
                  elif tab_name == "buy":
                      buy_button.configure(fg_color="#FFFFFF", text_color="#08376B")
                  elif tab_name == "myaccount":
                      myaccount_button.configure(fg_color="#FFFFFF", text_color="#08376B")

            global home_button, buy_button, myaccount_button
            upper_frame = ctk.CTkFrame(root, height=80, width=1280, fg_color="#08376B", bg_color="transparent", corner_radius=30)
            upper_frame.place(anchor="n", relx=0.5, rely=0.01, relwidth=0.7)
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
                def filmframe(self,parent,text1):
                    self.label = ctk.CTkLabel(parent, text=text1, text_color="#08376B", font=("Arial Rounded MT Bold",27), justify="left")
                    self.label.pack(side="top", expand=True, pady=30, anchor="w")
                    self._frame = ctk.CTkScrollableFrame(parent, fg_color="transparent", bg_color="transparent", width=1920, height=350, orientation="horizontal")
                    self._frame._scrollbar.grid_remove()
                    self._frame.pack(side="top", fill="x", expand=False)

                    class WebImage:
                        def __init__(self, url):
                            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Safari/605.1.15'})
                            with urllib.request.urlopen(url) as u:
                                raw_data = u.read()
                            #self.image = tk.PhotoImage(data=base64.encodebytes(raw_data))
                            image = Image.open(io.BytesIO(raw_data))
                            self.image = ctk.CTkImage(image, size=(200, 300))

                        def get(self):
                            return self.image
                    # for i in range(50):
                    thelogo = WebImage("https://drive.google.com/file/d/1p1_vhTTbPIVU9q8-Ypu9K-cpnmt-7Ka9/view?usp=sharing").get()
                    logohome = ctk.CTkLabel(self._frame, text="", image=thelogo)            
                    logohome.pack(side="left", expand=True, padx=20, anchor="w")


            NowShowing.filmframe(NowShowing, home_frame, "Now Showing")


            
            buy_frame = ctk.CTkScrollableFrame(buy, fg_color="transparent", bg_color="transparent", width=1920, height=1000)
            buy_frame._scrollbar.grid_remove()
            buy_frame.place(anchor="s", relx=0.5, rely=1, relwidth=1, relheight=0.98)
            myaccount_frame = ctk.CTkScrollableFrame(myaccount, fg_color="transparent", bg_color="transparent", width=1920, height=1000)
            myaccount_frame._scrollbar.grid_remove()
            myaccount_frame.place(anchor="s", relx=0.5, rely=1, relwidth=1, relheight=0.98)
            

            
            
home.home_page()
root.mainloop()
