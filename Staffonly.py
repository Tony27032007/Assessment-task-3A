from gg import *
import customtkinter as ctk
import cv2


def detect_qr_code(img):
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img)
    if data:
        return [(data, bbox)]
    return []

appqr = ctk.CTk(fg_color="white")
appqr.geometry("720x450")
appqr.title("CineMax")
appqr.resizable(True, True)

def create_text():
    global l, p
    l="tony2732007@gmail.com"
    p=27032007
#     l=ctk.CTkEntry(appqr, placeholder_text="Email", width=260, height=50, corner_radius=25, font=("Arial",22))
#     l.place(relx=0.5, rely=0.4, anchor="center")
#     p=ctk.CTkEntry(appqr, placeholder_text="Password", show="·" ,width=260, height=50, corner_radius=25, font=("Arial",22))
#     p.place(relx=0.5, rely=0.6, anchor="center")



def clear_window(window):
    for child in window.winfo_children():
        child.destroy()
    

def loginin():
    try:
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}"
        payload = {
            "email": l,
            "password": p,
            "returnSecureToken": True
        }
        response = requests.post(url, json=payload)
        data = response.json()
        if "idToken" in data:
            clear_window(appqr)
            
            # Create scanning status UI
            status_label = ctk.CTkLabel(appqr, text="Scan Ticket QR Code", 
                                        font=("Arial Rounded MT Bold", 24))
            status_label.pack(pady=20)
            
            status_info = ctk.CTkLabel(appqr, text="Scanning...", 
                               font=("Arial", 18), text_color="#1F6AA5")
            status_info.pack(pady=10)
            
            # Update UI to show we're ready to scan
            appqr.update()
            
            # Start camera
            cap = cv2.VideoCapture(0)
            scanning = True
            
            def verify_ticket(ticket_id):
            
                try:
                    # Check if the ticket ID exists in the database
                    ticket_doc = db.collection("tic").get()
                    
                    clear_window(appqr)
                    
                    if ticket_doc.exists:
                        # Ticket found
                        result_label = ctk.CTkLabel(appqr, text="✓ VALID TICKET", 
                                                  font=("Arial Bold", 26), text_color="#008000")
                        result_label.pack(pady=20)
                        
                        ticket_info = ctk.CTkLabel(appqr, text=f"Ticket ID: {ticket_id}", 
                                                 font=("Arial", 18))
                        ticket_info.pack(pady=10)
                    else:
                        # Ticket not found
                        result_label = ctk.CTkLabel(appqr, text="✗ INVALID TICKET", 
                                                  font=("Arial Bold", 26), text_color="#FF0000")
                        result_label.pack(pady=20)
                        
                        ticket_info = ctk.CTkLabel(appqr, text="Ticket not found in database", 
                                                 font=("Arial", 18))
                        ticket_info.pack(pady=10)
                    
                    # Buttons for next actions
                    buttons_frame = ctk.CTkFrame(appqr, fg_color="transparent")
                    buttons_frame.pack(pady=20, fill="x")
                    
                    scan_button = ctk.CTkButton(buttons_frame, text="Scan Another", 
                                              command=lambda: [clear_window(appqr), loginin()], 
                                              width=200, height=40, corner_radius=25,
                                              font=("Arial", 18))
                    scan_button.pack(side="left", padx=20, expand=True)
                    
                    exit_button = ctk.CTkButton(buttons_frame, text="Exit", 
                                              command=appqr.quit, 
                                              width=200, height=40, corner_radius=25,
                                              font=("Arial", 18), fg_color="#6B6B6B")
                    exit_button.pack(side="right", padx=20, expand=True)
                    
                except Exception as e:
                    clear_window(appqr)
                    error_label = ctk.CTkLabel(appqr, text="Error verifying ticket", 
                                             font=("Arial Bold", 24), text_color="#FF0000")
                    error_label.pack(pady=20)
                    
                    error_detail = ctk.CTkLabel(appqr, text=str(e), 
                                              font=("Arial", 16))
                    error_detail.pack(pady=10)
                    
                    retry_button = ctk.CTkButton(appqr, text="Try Again", 
                                               command=lambda: [clear_window(appqr), loginin()], 
                                               width=200, height=40, corner_radius=25,
                                               font=("Arial", 18))
                    retry_button.pack(pady=20)
            
            # Update periodically to keep UI responsive
            while scanning:
                ret, frame = cap.read()
                if not ret:
                    break
                
                decoded_objects = detect_qr_code(frame)
                for obj in decoded_objects:
                    data = obj.data.decode('utf-8')
                    print("QR Code Data:", data)
                    
                    # Draw rectangle around QR code
                    points = obj.polygon
                    if len(points) == 4:
                        cv2.line(frame, points[0], points[1], (0, 255, 0), 3)
                        cv2.line(frame, points[1], points[2], (0, 255, 0), 3)
                        cv2.line(frame, points[2], points[3], (0, 255, 0), 3)
                        cv2.line(frame, points[3], points[0], (0, 255, 0), 3)
                    
                    cv2.imshow('QR Code Scanner', frame)
                    cv2.waitKey(500)  # Show the frame for a moment with the green outline
                    
                    scanning = False
                    cap.release()
                    cv2.destroyAllWindows()
                    
                    # Assume the QR code data is the ticket ID
                    verify_ticket(data)
                    return
                
                # Draw the frame in an OpenCV window
                cv2.imshow('QR Code Scanner', frame)
                
                # Check for key press and process Tkinter events to keep UI responsive
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                appqr.update_idletasks()
                appqr.update()
            
            # Clean up
            cap.release()
            cv2.destroyAllWindows()
        else:
            raise Exception(data.get("error", {}).get("message", "Unknown error"))
    except Exception as e:
        wrong = ctk.CTkLabel(appqr, text="Wrong Username or Password", text_color="red", font=("Arial Rounded MT Bold",22))
        wrong.place(relx=0.5, rely=0.85, anchor="center")

create_text()
inlog = ctk.CTkButton(appqr, text="Login", command=loginin, width=260, height=50, corner_radius=25, font=("Arial Rounded MT Bold",22))
inlog.place(relx=0.5, rely=0.75, anchor="center")

appqr.mainloop()